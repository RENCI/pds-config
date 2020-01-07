import requests

json_headers = {
    "Accept": "application/json"
}
json_put_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

config = {
    "aggregator_plugin_id": "agg0",
    "phenotype_mapping_plugin_id": "pds-phenotype-mapping0",
    "data_provider_plugin_id": "pdsdpi-mock-fhir0",
    "profile_plugin_id": "pds-profile0",
    "default_units": [{
        "clinical_feature_variable": "v0",
        "unit": "u0",
        "title": "t0"
    }],
    "model": [{
        "drug": "d0",
        "indications": [{
            "indication": "i0",
            "model_plugin_id": "m0"
        }]
    }]
}

def test_get_config():
    result=requests.put("http://pdsconfig:8080/config", headers=json_put_headers, json=config)
    result=requests.get("http://pdsconfig:8080/config", headers=json_headers)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == config
    

def test_ui():
    resp = requests.get("http://pdsconfig:8080/ui")

    assert resp.status_code == 200
            
