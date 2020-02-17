import requests

json_headers = {
    "Accept": "application/json"
}

json_put_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

custom_units = [{
    "id": "v0",
    "units": "u0"
}]

custom_units2 = [{
    "id": "v1",
    "units": "u1"
}]

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
    "requiredPatientVariables": clinical_feature_variables
}]

def test_get_config():
    result=requests.get("http://pdsconfig:8080/config", headers=json_headers)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == config
    

def test_get_plugin_config():
    result=requests.get("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_headers)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == config[0]
    

def test_put_config_add_property():
    result=requests.put("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_put_headers, json={
        "enabled": False
    })
    assert result.status_code == 200
    result=requests.get("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_headers)
                
    assert result.status_code == 200
    assert result.json() == {
        **config[0],
        "enabled": False
    }
    result=requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_headers)
    

def test_put_config_override_property():
    result=requests.put("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_put_headers, json={
        "enabled": False
    })
    assert result.status_code == 200
    result=requests.put("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_put_headers, json={
        "enabled": True
    })
    assert result.status_code == 200
    result=requests.get("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_headers)
                
    assert result.status_code == 200
    assert result.json() == {
        **config[0],
        "enabled": True
    }
    result=requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_headers)
    

def test_delete_config():
    result=requests.put("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_put_headers, json={
        "enabled": False
    })
    assert result.status_code == 200
    result=requests.delete("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_headers)
    assert result.status_code == 200
    result=requests.get("http://pdsconfig:8080/config/pdspi-guidance-example", headers=json_headers)
                
    assert result.status_code == 200
    assert result.json() == config[0]

def test_get_selectors():
    result=requests.get("http://pdsconfig:8080/selectors", headers=json_headers)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == selectors

def test_put_selectors():
    result=requests.put("http://pdsconfig:8080/selectors", headers=json_put_headers, json=selectors2)
    assert result.status_code == 200
                
    result=requests.get("http://pdsconfig:8080/selectors", headers=json_headers)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == selectors2


def test_get_custom_units():
    result=requests.get("http://pdsconfig:8080/customUnits", headers=json_headers)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == custom_units

def test_put_custom_units():
    result=requests.put("http://pdsconfig:8080/customUnits", headers=json_put_headers, json=custom_units2)
    assert result.status_code == 200

    result=requests.get("http://pdsconfig:8080/customUnits", headers=json_headers)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == custom_units2

    

def test_ui():
    resp = requests.get("http://pdsconfig:8080/ui")

    assert resp.status_code == 200
            
