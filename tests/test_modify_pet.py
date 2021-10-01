from libs.get_pet import get_pet
from libs.modify_pet import modify_pet
from libs.add_new_pet import add_new_pet
from libs.delete_pet import delete_pet
from pytest import mark
import json

target_url = "https://petstore.swagger.io/v2/pet"
kotik = "https://images.unsplash.com/photo-1615789591457-74a63395c990?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZG9tZXN0aWMlMjBjYXR8ZW58MHx8MHx8&ixlib=rb-1.2.1&w=1000&q=80"
body = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Bamby20210930!@#$%^&*()12",
  "photoUrls": [kotik],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

body2 = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Murzik20210930!@#$%^&*()12",
  "photoUrls": [kotik],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

add_post_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "api_key": "pinloader"
}



@mark.sanity
@mark.regression
def test_modify_pet(url=target_url, *args, **kwargs):
    """Test case to verify pet deletion from the store"""
    from time import sleep
    jsn1, code1 = add_new_pet(url, data=json.dumps(body), headers=add_post_headers)
    assert code1 == 200, "Exception. Expected code: 200, actual {code1}"
    pet_id = jsn1['id']
    jsn2, code2 = modify_pet(url, data=json.dumps(body2), headers=headers)
    assert code2 == 200, "Exception. Expected code: 200, actual {code2}"
    assert jsn2['id'] == jsn1['id'], f"Exception. Pet id from put jsn2['id'] must be the same as in post {jsn1['id']}"
    assert jsn2['name'] == "Murzik20210930!@#$%^&*()12", f"Exception name jsn2['id'] must be == Murzik20210930!@#$%^&*()12"
    sleep(30)
    jsn3, code3 = delete_pet(f"{url}/{str(pet_id)}", headers=headers)