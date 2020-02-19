import os
import json
import sys
from pymongo import MongoClient
from tx.requests.utils import get

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
        config = get(pdsdpi_url_base(piid) + "/config")
        config = config.value
        config["piid"] = piid
        mongo_client[mongo_database][mongo_collection].insert_one({**config})
    return config
    

def _get_system_config():
    return _cache_system_config()

                     
def _put_system_config(body):
    _cache_system_config()
    return mongo_client[mongo_database][mongo_collection].update_one({"type":"system"}, {"$set": body}, upsert=True).modified_count

                     
def _get_plugin_config(piid):
    return _cache_plugin_config(piid)

                     
def _put_plugin_config(piid, body):
    _cache_plugin_config(piid)
    if "piid" in body:
        del body["piid"]
    return mongo_client[mongo_database][mongo_collection].update_one({"piid":piid}, {"$set": body}, upsert=True).modified_count


def _delete_plugin_config(piid):
    return mongo_client[mongo_database][mongo_collection].delete_one({"piid":piid}).deleted_count


def get_config():
    system_config = _get_system_config()
    print(system_config)
    sys.stdout.flush()
    plugin_ids = system_config["piids"]
    configs = []
    for plugin_id in plugin_ids:
        config = _get_plugin_config(plugin_id)
        configs.append(config)        
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

                     
def put_plugin_config(piid, body):
    _put_plugin_config(piid, body)
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
    return system_config["custom_units"]

                     
def put_custom_units(body):
    _put_system_config({
        "custom_units": body
    })
    return ""
        
