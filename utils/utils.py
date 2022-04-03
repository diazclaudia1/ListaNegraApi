import os

import requests

ERR_CODE = "TIMEOUT"


def post_err(url, payload):
    try:
        return requests.post(url, json=payload, timeout=int(os.getenv('SERVICE_TIMEOUT')))
    except requests.exceptions.HTTPError as err:
        print("Http Error:", err)
        return ERR_CODE
    except requests.exceptions.ConnectionError as err:
        print("Error Connecting:", err)
        return ERR_CODE
    except requests.exceptions.Timeout as err:
        print("Timeout Error:", err)
        return ERR_CODE
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
        return ERR_CODE


def get_err(url):
    try:
        return requests.get(url, timeout=int(os.getenv('SERVICE_TIMEOUT')))
    except requests.exceptions.HTTPError as err:
        print("Http Error:", err)
        return ERR_CODE
    except requests.exceptions.ConnectionError as err:
        print("Error Connecting:", err)
        return ERR_CODE
    except requests.exceptions.Timeout as err:
        print("Timeout Error:", err)
        return ERR_CODE
    except requests.exceptions.RequestException as er:
        print("OOps: Something Else", er)
        return ERR_CODE


def check_err(code):
    return code == ERR_CODE


def err_message():
    return os.getenv('MESSAGE_TIMEOUT'), 503
