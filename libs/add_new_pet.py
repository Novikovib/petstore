from requests import post


def add_new_pet(url, *args, **kwargs):
    """Function to add new pet via posting data
     on server"""
    resp = post(url, *args, **kwargs)
    json_response = resp.json()
    return json_response, resp.status_code