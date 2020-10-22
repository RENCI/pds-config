import os
import json
import sys
from collections import defaultdict
from pymongo import MongoClient
from tx.requests.utils import get
import logging
import connexion

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mongodb_host = os.environ["MONGO_HOST"]
mongodb_port = int(os.environ["MONGO_PORT"])
mongo_database = os.environ["MONGO_DATABASE"]
mongo_collection = os.environ["MONGO_COLLECTION"]
mongo_username = os.environ["MONGO_NON_ROOT_USERNAME"]
mongo_password = os.environ["MONGO_NON_ROOT_PASSWORD"]
default_config = os.environ["DEFAULT_CONFIG"]
pds_host = os.environ["PDS_HOST"]
pds_port = os.environ["PDS_PORT"]
pds_version = os.environ["PDS_VERSION"]

def pdsdpi_url_base(plugin):
    return f"http://{pds_host}:{pds_port}/{pds_version}/plugin/{plugin}"

if default_config is not None and default_config != "":
    default_config = json.loads(default_config)

mongo_client = MongoClient(mongodb_host, mongodb_port, username=mongo_username, password=mongo_password, authSource=mongo_database)

# need to add redis lock
# need to add error handling
def _cache_system_config():
    config = mongo_client[mongo_database][mongo_collection].find_one({"type": "system"})
    if config is not None:
        del config["_id"]
        del config["type"]
    else:
        config = default_config
        mongo_client[mongo_database][mongo_collection].insert_one({"type": "system", **default_config})
    return config


def _cache_plugin_config(piid):
    config = mongo_client[mongo_database][mongo_collection].find_one({"piid": piid})
    if config is not None:
        del config["_id"]
    else:
        config = _get_plugin_config_factory_default(piid)
        mongo_client[mongo_database][mongo_collection].insert_one({**config}) # we had to create a new object here because MongoClient.insert_one adds and "_id" field to the dict
    return config


def _get_plugin_config_factory_default(piid):
    config = get(pdsdpi_url_base(piid) + "/config")
    config = config.value
    config["piid"] = piid
    if "enabled" not in config:
        config["enabled"] = True
    return config


def _get_system_config():
    return _cache_system_config()

                     
def _put_system_config(body):
    _cache_system_config()
    return mongo_client[mongo_database][mongo_collection].update_one({"type":"system"}, {"$set": body}, upsert=True).modified_count

                     
def _get_plugin_config(piid):
    return _cache_plugin_config(piid)

                     
def _post_plugin_config(piid, body):
    _cache_plugin_config(piid)
    if "piid" in body:
        del body["piid"]
    return mongo_client[mongo_database][mongo_collection].update_one({"piid":piid}, {"$set": body}, upsert=True).modified_count


def _delete_plugin_config(piid):
    return mongo_client[mongo_database][mongo_collection].delete_one({"piid":piid}).deleted_count


def post_config(body):
    system_config = _get_system_config()
    custom_rules = system_config["customRules"]
    system_config["customRules"] = body + custom_rules
    _put_system_config(system_config)

    return get_config()

def delete_config():
    body = request = connexion.request.json
    system_config = _get_system_config()
    custom_rules = system_config["customRules"]
    system_config["customRules"] = [custom_rule for custom_rule in custom_rules if custom_rule not in body]
    _put_system_config(system_config)

    return get_config()

def key_selector(selector):
    return {
        "id": selector["id"],
        "selectorValue": {
            "value": selector["selectorValue"]["value"]
        }
    }


# https://stackoverflow.com/questions/13264511/typeerror-unhashable-type-dict
def freeze(d):
    if isinstance(d, dict):
        return frozenset((freeze(key), freeze(value)) for key, value in d.items())
    elif isinstance(d, list):
        return tuple(freeze(value) for value in d)
    return d


def unfreeze(d):
    if isinstance(d, frozenset):
        return {unfreeze(key): unfreeze(value) for key, value in d}
    elif isinstance(d, tuple):
        return [unfreeze(value) for value in d]
    return d


def plugin_config_factory_default(plugin_id):
    config = _get_plugin_config_factory_default(plugin_id)
    settingsDefaults = config.get("settingsDefaults")
    if settingsDefaults is None:
        selectors = []
    else:
        selectors = settingsDefaults.get("pluginSelectors", [])

    plugin_type = config.get("pluginType")

    if plugin_type is not None:
        selectors.append({
            "id": "pluginType",
            "selectorValue": {
                "value": plugin_type
            }
        })

    return selectors, config


def plugin_config(plugin_id, custom_selectors=None):
    config = _get_plugin_config(plugin_id)
    if custom_selectors is None:
        settingsDefaults = config.get("settingsDefaults")
        if settingsDefaults is None:
            selectors = []
        else:
            selectors = settingsDefaults.get("pluginSelectors", [])
    else:
        selectors = list(custom_selectors)
    plugin_type = config.get("pluginType")

    if plugin_type is not None:
        selectors.append({
            "id": "pluginType",
            "selectorValue": {
                "value": plugin_type
            }
        })

    return selectors, config

    
def get_config(status="enabled"):
    system_config = _get_system_config()
    custom_rules = system_config["customRules"]
    plugin_ids = system_config["piids"]
    plugin_configs = defaultdict(list)
    plugin_config_items = [plugin_config(custom_rule["piid"], custom_rule["selectors"]) for custom_rule in custom_rules] + [plugin_config(plugin_id) for plugin_id in plugin_ids]

    for selectors, config in plugin_config_items:
        enabled = config["enabled"]
        if status == "all" or (status == "enabled" and enabled) or (status == "disabled" and not enabled):
            configs = plugin_configs[freeze(selectors)]
            if config not in configs:
                configs.append(config)
    
    configs = [{
        "selectors": unfreeze(selectors),
        "plugin": plugins[0]
    } for selectors, plugins in plugin_configs.items()]

    return configs

    

def get_config_factory_default(status="enabled"):
    system_config = _get_system_config()
    custom_rules = system_config["customRules"]
    plugin_ids = system_config["piids"]
    plugin_configs = defaultdict(list)
    plugin_config_items = [plugin_config_factory_default(plugin_id) for plugin_id in plugin_ids]

    for selectors, config in plugin_config_items:
        enabled = config["enabled"]
        if status == "all" or (status == "enabled" and enabled) or (status == "disabled" and not enabled):
            configs = plugin_configs[freeze(selectors)]
            if config not in configs:
                configs.append(config)
    
    configs = [{
        "selectors": unfreeze(selectors),
        "plugins": plugins
    } for selectors, plugins in plugin_configs.items()]

    return configs


def get_plugin_config(piid):
    if piid is None:
        system_config = _get_system_config()
        plugin_ids = system_config["plugin_ids"]
        configs = []
        for plugin_id in plugin_ids:
            config = _get_plugin_config(piid)
            configs.append(config)
        return configs
    else:
        return _get_plugin_config(piid)

                     
def post_plugin_config(piid, body):
    _post_plugin_config(piid, body)
    return ""

                     
def delete_plugin_config(piid):
    _delete_plugin_config(piid)
    return ""

                     
def get_selectors():
    system_config = _get_system_config()
    return system_config["selectors"]

                     
def put_selectors(body):
    _put_system_config({
        "selectors": body
    })
    return ""

                     
def get_custom_units():
    system_config = _get_system_config()
    return system_config["customUnits"]

                     
def put_custom_units(body):
    _put_system_config({
        "customUnits": body
    })
    return ""
        
