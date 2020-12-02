import requests
import json

json_get_headers = {
    "Accept": "application/json"
}

json_delete_headers = json_get_headers

json_put_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

json_post_headers = json_put_headers

selectors = [{
    "title": "Drug",
    "id": "dosing.rxCUI",
    "legalValues": {
        "type": "string",
        "enum": [
            {
                "value": "rxCUI:1596450",
                "title":"Gentamicin"
            }, {
                "value":"rxCUI:1114195"
            }, {
                "value":"rxCUI:1546356"
            }, {
                "value":"rxCUI:1364430"
            }, {
                "value":"rxCUI:1599538"
            }, {
                "value":"rxCUI:1927851"
            }
        ]
    }
}]

selectors2 = [{
    "title": "Drug2",
    "id": "dosing.rxCUI2",
    "legalValues": {
        "type": "string",
        "enum": [
            {
                "value": "rxCUI:1596450",
                "title":"Gentamicin2"
            }, {
                "value":"rxCUI:1114195"
            }, {
                "value":"rxCUI:1546356"
            }, {
                "value":"rxCUI:1364430"
            }, {
                "value":"rxCUI:1599538"
            }, {
                "value":"rxCUI:1927851"
            }
        ]
    }
}]


clinical_feature_variables = [
    {
        "id": "v0",
        "title": "t0",
        "why": "w0",
        "legalValues": {
            "type": "i0"
        }
    }, {
        "id": "v1",
        "title": "t1",
        "why": "w1",
        "legalValues": {
            "type": "i1"
        }
    }, {
        "id": "v2",
        "title": "t2",
        "why": "w2",
        "legalValues": {
            "type": "i2"
        }
    }
]

config = [{
    "piid": "pdspi-guidance-example",
    "pluginType": "g",
    "settingsDefaults": {"patientVariables": clinical_feature_variables},
}, {
    "piid": "pdspi-mapper-example",
    "pluginType": "m"
}, {
    "piid": "pdspi-fhir-example",
   "pluginType": "f"
}]

config_return = [{
    "piid": "pdspi-guidance-example",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": True
}, {
    "piid": "pdspi-mapper-example",
    "pluginType": "m",
    "enabled": True
}, {
    "piid": "pdspi-fhir-example",
    "pluginType": "f",
    "enabled": True
}]

post_config_return = [{
    "piid": "pdspi-guidance-example2",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": True
}, {
    "piid": "pdspi-mapper-example",
    "pluginType": "m",
    "enabled": True
}, {
    "piid": "pdspi-fhir-example",
    "pluginType": "f",
    "enabled": True
}]

post_config_return_2 = [{
    "piid": "pdspi-guidance-example2",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": True
}, {
    "piid": "pdspi-guidance-example",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": True
}, {
    "piid": "pdspi-mapper-example",
    "pluginType": "m",
    "enabled": True
}, {
    "piid": "pdspi-fhir-example",
    "pluginType": "f",
    "enabled": True
}]

config_enabled_return = [{
    "piid": "pdspi-mapper-example",
    "pluginType": "m",
    "enabled": True
}, {
    "piid": "pdspi-fhir-example",
    "pluginType": "f",
    "enabled": True
}]

config_disabled_return = [{
    "piid": "pdspi-guidance-example",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": False
}, {
    "piid": "pdspi-guidance-example2",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": False
}]

config_all_return = [{
    "piid": "pdspi-guidance-example2",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": False
}, {
    "piid": "pdspi-guidance-example",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": False
}, {
    "piid": "pdspi-mapper-example",
    "pluginType": "m",
    "enabled": True,
}, {
    "piid": "pdspi-fhir-example",
    "pluginType": "f",
    "enabled": True,
}]

config_factory_default_return = [{
    "piid": "pdspi-guidance-example",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": True
}, {
    "piid": "pdspi-mapper-example",
    "pluginType": "m",
    "enabled": True
}, {
    "piid": "pdspi-fhir-example",
    "pluginType": "f",
    "enabled": True
}]

config_factory_default_enabled_return = [{
    "piid": "pdspi-guidance-example",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": True
}, {
    "piid": "pdspi-mapper-example",
    "pluginType": "m",
    "enabled": True
}, {
    "piid": "pdspi-fhir-example",
    "pluginType": "f",
    "enabled": True
}]

config_factory_default_disabled_return = [{
    "piid": "pdspi-guidance-example2",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": False
}]

config_factory_default_all_return = [{
    "piid": "pdspi-guidance-example",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": True
}, {
    "piid": "pdspi-guidance-example2",
    "pluginType": "g",
    "settingsDefaults": {
        "patientVariables": clinical_feature_variables
    },
    "enabled": False
}, {
    "piid": "pdspi-mapper-example",
    "pluginType": "m",
    "enabled": True
}, {
    "piid": "pdspi-fhir-example",
    "pluginType": "f",
    "enabled": True
}]

selector_config_return = [{
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "g"
        }
    }],
    "plugin": {
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": True
    }
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "m"
        }
    }],
    "plugin": {
        "piid": "pdspi-mapper-example",
        "pluginType": "m",
        "enabled": True
    }
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "f"
        }
    }],
    "plugin": {
        "piid": "pdspi-fhir-example",
        "pluginType": "f",
        "enabled": True
    }
}]

post_selector_config_return = [{
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "g"
        }
    }],
    "plugin": {
        "piid": "pdspi-guidance-example2",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": True
    }
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "m"
        }
    }],
    "plugin": {
        "piid": "pdspi-mapper-example",
        "pluginType": "m",
        "enabled": True
    }
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "f"
        }
    }],
    "plugin": {
        "piid": "pdspi-fhir-example",
        "pluginType": "f",
        "enabled": True
    }
}]

post_selector_config_return_2 = [{
    "selectors": [{
        "id": "r1",
        "selectorValue": {
            "value": "s1"
        }
    }, {
        "id": "pluginType",
        "selectorValue": {
            "value": "g"
        }
    }],
    "plugin": {
        "piid": "pdspi-guidance-example2",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": True
    }
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "g"
        }
    }],
    "plugin": {
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": True
    }
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "m"
        }
    }],
    "plugin": {
        "piid": "pdspi-mapper-example",
        "pluginType": "m",
        "enabled": True
    }
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "f"
        }
    }],
    "plugin": {
        "piid": "pdspi-fhir-example",
        "pluginType": "f",
        "enabled": True
    }
}]

selector_config_enabled_return = [{
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "m"
        }
    }],
    "plugin": {
        "piid": "pdspi-mapper-example",
        "pluginType": "m",
        "enabled": True
    }
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "f"
        }
    }],
    "plugin": {
        "piid": "pdspi-fhir-example",
        "pluginType": "f",
        "enabled": True
    }
}]

selector_config_disabled_return = [{
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "g"
        }
    }],
    "plugin": {
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": False
    }
}]

selector_config_all_return = [{
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "g"
        }
    }],
    "plugin": {
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": False
    }
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "m"
        }
    }],
    "plugin": {
        "piid": "pdspi-mapper-example",
        "pluginType": "m",
        "enabled": True,
    }
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "f"
        }
    }],
    "plugin": {
        "piid": "pdspi-fhir-example",
        "pluginType": "f",
        "enabled": True,
    }
}]

selector_config_factory_default_return = [{
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "g"
        }
    }],
    "plugins": [{
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": True
    }]
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "m"
        }
    }],
    "plugins": [{
        "piid": "pdspi-mapper-example",
        "pluginType": "m",
        "enabled": True
    }]
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "f"
        }
    }],
    "plugins": [{
        "piid": "pdspi-fhir-example",
        "pluginType": "f",
        "enabled": True
    }]
}]

selector_config_factory_default_enabled_return = [{
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "g"
        }
    }],
    "plugins": [{
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": True
    }]
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "m"
        }
    }],
    "plugins": [{
        "piid": "pdspi-mapper-example",
        "pluginType": "m",
        "enabled": True
    }]
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "f"
        }
    }],
    "plugins": [{
        "piid": "pdspi-fhir-example",
        "pluginType": "f",
        "enabled": True
    }]
}]

selector_config_factory_default_disabled_return = [{
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "g"
        }
    }],
    "plugins": [{
        "piid": "pdspi-guidance-example2",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": False
    }]
}]

selector_config_factory_default_all_return = [{
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "g"
        }
    }],
    "plugins": [{
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": True
    }, {
        "piid": "pdspi-guidance-example2",
        "pluginType": "g",
        "settingsDefaults": {
            "patientVariables": clinical_feature_variables
        },
        "enabled": False
    }]
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "m"
        }
    }],
    "plugins": [{
        "piid": "pdspi-mapper-example",
        "pluginType": "m",
        "enabled": True
    }]
}, {
    "selectors": [{
        "id": "pluginType",
        "selectorValue": {
            "value": "f"
        }
    }],
    "plugins": [{
        "piid": "pdspi-fhir-example",
        "pluginType": "f",
        "enabled": True
    }]
}]

def bag_equal(a, b):
    t = list(b)
    for elem in a:
        if elem in t:
            t.remove(elem)
        else:
            return False
    return True


def test_get_config():
    result=requests.get("http://pdsconfig:8080/config", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), config_return)


def test_get_config_factory_default():
    result=requests.get("http://pdsconfig:8080/configFactoryDefault", headers=json_get_headers)
    assert result.status_code == 200

    assert bag_equal(result.json(), config_factory_default_return)
    

def test_get_config_enabled():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/config?status=enabled", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), config_enabled_return)

    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": True
    })
    

def test_get_config_disabled():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/config?status=disabled", headers=json_get_headers)
    assert result.status_code == 200

    assert bag_equal(result.json(), config_disabled_return)
    
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": True
    })
    

def test_get_config_all():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/config?status=all", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), config_all_return)
    
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": True
    })
    

def test_get_config_factory_default_enabled():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/configFactoryDefault?status=enabled", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), config_factory_default_enabled_return)

    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_get_config_factory_default_disabled():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/configFactoryDefault?status=disabled", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), config_factory_default_disabled_return)
    
    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_get_config_factory_default_all():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/configFactoryDefault?status=all", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), config_factory_default_all_return)
    
    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_get_plugin_config():
    result=requests.get("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_get_headers)

    assert result.status_code == 200
                
    assert result.json() == config_return[0]
    

def test_delete_plugin_config():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    assert result.status_code == 200
    result=requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    assert result.status_code == 200
    result=requests.get("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_get_headers)
                
    assert result.status_code == 200
    assert result.json() == config_return[0]


def test_get_plugin_config_disabled():
    result=requests.get("http://pdsconfig:8080/config/pdspi-guidance-example2", headers=json_get_headers)
    assert result.status_code == 200
                
    assert result.json() == {
        "piid": "pdspi-guidance-example2",
        "pluginType": "g",
        "settingsDefaults": {"patientVariables": clinical_feature_variables},
        "enabled": False
    }


def test_post_config_add_property():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    assert result.status_code == 200
    result=requests.get("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_get_headers)
                
    assert result.status_code == 200
    assert result.json() == {
        **config[0],
        "enabled": False
    }
    result=requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_post_config_override_property():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    assert result.status_code == 200
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": True
    })
    assert result.status_code == 200
    result=requests.get("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_get_headers)
                
    assert result.status_code == 200
    assert result.json() == config_return[0]
    result=requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_get_selector_config():
    result=requests.get("http://pdsconfig:8080/selectorConfig", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), selector_config_return)


def test_post_selector_config():
    requests.post("http://pdsconfig:8080/config/pdspi-guidance-example2", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example2",
        "pluginType": "g",
        "enabled": True
    })
    
    result=requests.post("http://pdsconfig:8080/selectorConfig", json=[{
        "selectors": [],
        "piid": "pdspi-guidance-example2"
    }], headers=json_post_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), post_selector_config_return)
    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example2", headers=json_delete_headers)
    requests.delete("http://pdsconfig:8080/selectorConfig", json=[{
        "selectors": [],
        "piid": "pdspi-guidance-example2"
    }], headers=json_delete_headers)


def test_post_selector_config_selectors():
    requests.post("http://pdsconfig:8080/config/pdspi-guidance-example2", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example2",
        "pluginType": "g",
        "enabled": True
    })
    
    result=requests.post("http://pdsconfig:8080/selectorConfig", json=[{
        "selectors": [{
            "id": "r1",
            "selectorValue": {
                "value": "s1"
            }
        }],
        "piid": "pdspi-guidance-example2"
    }], headers=json_post_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), post_selector_config_return_2)
    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example2", headers=json_delete_headers)
    requests.delete("http://pdsconfig:8080/selectorConfig", json=[{
        "selectors": [{
            "id": "r1",
            "selectorValue": {
                "value": "s1"
            }
        }],
        "piid": "pdspi-guidance-example2"
    }], headers=json_delete_headers)


def test_delete_selector_config():
    requests.post("http://pdsconfig:8080/config/pdspi-guidance-example2", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example2",
        "pluginType": "g",
        "enabled": True
    })
    
    result=requests.post("http://pdsconfig:8080/selectorConfig", json=[{
        "selectors": [],
        "piid": "pdspi-guidance-example2"
    }], headers=json_post_headers)

    result=requests.delete("http://pdsconfig:8080/selectorConfig", json=[{
        "selectors": [],
        "piid": "pdspi-guidance-example2"
    }], headers=json_delete_headers)

    assert result.status_code == 200
                
    assert bag_equal(result.json(), selector_config_return)

    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example2", headers=json_delete_headers)


def test_get_selector_config_factory_default():
    result=requests.get("http://pdsconfig:8080/selectorConfigFactoryDefault", headers=json_get_headers)
    assert result.status_code == 200

    assert bag_equal(result.json(), selector_config_factory_default_return)
    

def test_get_selector_config_enabled():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/selectorConfig?status=enabled", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), selector_config_enabled_return)

    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_get_selector_config_disabled():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/selectorConfig?status=disabled", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), selector_config_disabled_return)
    
    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_get_selector_config_all():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/selectorConfig?status=all", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), selector_config_all_return)
    
    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_get_selector_config_factory_default_enabled():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/selectorConfigFactoryDefault?status=enabled", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), selector_config_factory_default_enabled_return)

    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_get_selector_config_factory_default_disabled():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/selectorConfigFactoryDefault?status=disabled", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), selector_config_factory_default_disabled_return)
    
    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_get_selector_config_factory_default_all():
    result=requests.post("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_post_headers, json={
        "piid": "pdspi-guidance-example",
        "pluginType": "g",
        "enabled": False
    })
    result=requests.get("http://pdsconfig:8080/selectorConfigFactoryDefault?status=all", headers=json_get_headers)
    assert result.status_code == 200
                
    assert bag_equal(result.json(), selector_config_factory_default_all_return)
    
    requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_delete_headers)
    

def test_get_selectors():
    result=requests.get("http://pdsconfig:8080/selectors", headers=json_get_headers)
    assert result.status_code == 200
                
    assert result.json() == selectors

    
def test_put_selectors():
    result=requests.put("http://pdsconfig:8080/selectors", headers=json_put_headers, json=selectors2)
    assert result.status_code == 200
                
    result=requests.get("http://pdsconfig:8080/selectors", headers=json_get_headers)
    assert result.status_code == 200
                
    assert result.json() == selectors2
    

def test_ui():
    resp = requests.get("http://pdsconfig:8080/ui")

    assert resp.status_code == 200
