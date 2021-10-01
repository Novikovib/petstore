from requests import put


def modify_pet(url, *args, **kwargs):
    """Function to add new pet via posting data
     on server"""
    resp = put(url, *args, **kwargs)
    json_response = resp.json()
    return json_response, resp.status_code