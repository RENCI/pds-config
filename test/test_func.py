import requests

json_headers = {
    "Accept": "application/json"
}
json_put_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

config = {
    "aggregator_plugin_id": "agg",
    "phenotype_mapping_plugin_id": "pds-phenotype-mapping",
    "data_provider_plugin_id": "pdsdpi-mock-fhir",
    "model": {
        [{
            "drug": "d1",
            "indications": [
                {
                    "indication": "i1",
                    "model_plugin_id": "pdsmpi-ref"
                }
            ]
        }]
    }
}

def test_get_config():
    result=requests.put("http://pdsconfig:8080/config", headers=json_put_headers, json=config)
    result=requests.get("http://pdsconfig:8080/config", headers=json_headers)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == config
    
