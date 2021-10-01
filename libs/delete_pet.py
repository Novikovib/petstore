from requests import delete


def delete_pet(url, *args, **kwargs):
    """Function to send request for pet deletion"""
    resp = delete(url, *args, **kwargs)
    json_response = resp.json()
    return json_response, resp.status_code