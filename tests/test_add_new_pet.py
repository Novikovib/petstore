from libs.get_pet import get_pet
from libs.add_new_pet import add_new_pet
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
  "name": "Mus'ka20210930!@#$%^&*()12",
  "photoUrls": [kotik],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

@mark.sanity
@mark.regression
def test_add_new_pet(url=target_url, *args, **kwargs):
    """Tets is designed to verify adding new pet to Petstore"""
    jsn1, code1 = add_new_pet(url, data=json.dumps(body), headers=headers)
    assert jsn1['category']['id'] == 0, f"Category id '{jsn1['category']['id']}' is not == '0'"
    assert jsn1['category']['name'] == 'string', f"Category name '{jsn1['category']['name']}' is not == 'string'"
    assert jsn1['name'] == "Mus'ka20210930!@#$%^&*()12", f"Name '{jsn1['name']}' is not == 'Mus'ka20210930!@#$%^&*()12'"
    assert jsn1['photoUrls'][0] == kotik, f"photoUrls '{jsn1['photoUrls'][0]}' is not == '{kotik}'"
    assert jsn1['status'] == "available", f"status '{jsn1['status']}' is not == 'available'"
    assert code1 == 200, "Exception. Expected code: 200, actual {code1}"
    pet_id = jsn1['id']
    jsn3, code3 = get_pet(f"{url}/{str(pet_id)}")
    assert code3 == 200, "Exception. Pet is not found after addition"
    assert jsn1 == jsn3, "Should be the same data as after creation"


