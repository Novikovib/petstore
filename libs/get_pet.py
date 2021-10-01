from requests import get


def get_pet(url, *args, **kwargs):
    """Function that gets users from site using get request
    and pick status code"""
    resp = get(url, *args, **kwargs)
    json_response = resp.json()
    return json_response, resp.status_code