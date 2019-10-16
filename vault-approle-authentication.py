##########################################################################################################################
# vault-approle-authentication
# https://github.com/troydieter/vault-approle-authentication
# Define secret_id and role_id in the loginJson
# Set requests.post and get for your Vault API endpoints
##########################################################################################################################

import sys
import requests, getpass

# Work in progress below
# import json
# stored_approle = {
# }

# with open('approle_creds.json', 'w') as json_file:
#    json.dump(stored_approle, json_file)

def getAWS_KEYS():
    try:
        #Make request to obtain a token for this execution
        headersLogin = {'Content-Type': 'application/json'}
        loginJson = {
            "secret_id": "",
	        "role_id": ""
        }
        r = requests.post("https://vault-api.contoso.com/v1/auth/approle/login", data={}, json=loginJson, headers=headersLogin)
        data = r.json()
        token = data['auth']["client_token"]

        headersKeys = {"X-Vault-Token": token}
        r = requests.get("https://vault-api.contoso.com/v1/aws/creds/approle-name", headers=headersKeys)
        data = r.json()

        return data["data"]["access_key"], data["data"]["secret_key"]
    except:
        return (str(sys.exc_info()))

if __name__ == "__main__":

    result = getAWS_KEYS()
    print(result)


