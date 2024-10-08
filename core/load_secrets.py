import json
import os
import random


'''
Load secrets from secrets.json
'''

__secrets = None

HOME_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def __load_secrets_json():
    global __secrets
    try:
        with open(HOME_PATH + os.path.sep + 'secrets.json') as secrets_data_file:
            __secrets = json.load(secrets_data_file)
        return __secrets
    except Exception as e:
        print(f"Could not load secrets json: {str(e)}")

# load secrets randomly
def get_secrets():
    """
    return secrets
    """
    try:
        if __secrets is None:
            __load_secrets_json()
        if __secrets:
            username, password = random.choice(list(__secrets.items()))
            return username, password

    except Exception as e:
        print(f"Could not get secrets: {str(e)}")
