from libs.get_pet import get_pet
from pytest import mark
destination_url = "https://petstore.swagger.io/v2/pet/1"


@mark.regression
def test_get_get_by_id(url=destination_url):
    """Get pet by id"""
    json_req1, code1 = get_pet(url)
    assert code1 == 200, "Exception. Expected code: 200, actual {code1}"
    assert json_req1['id'] == 1, f"Id '{json_req1['id']}' is not == 1"
    assert json_req1['category']['id'] == 0, f"Pet category.id '{json_req1['category']['id']}' is not == 0"
    assert json_req1['name'] == "pet001", f"Pet name '{json_req1['name']}' is not == 'pet001'"
    assert json_req1['photoUrls'] == [], f"Pet photoUrls '{json_req1['photoUrls']}' is not == []"
    assert json_req1['tags'] == [], f"Pet tags '{json_req1['tags']}' is not == []"
    assert json_req1['status'] == 'ok', f"status '{json_req1['status']}' is not == 'ok'"



