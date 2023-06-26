from config import nd_username, nd_password, nd_ip
from ndlogin import *
import yaml
import json
import requests
import urllib3
urllib3.disable_warnings()


def getTenant():
    url = "https://" + nd_ip + "/api/v1/tenants/"
    cookies = getToken(nd_ip, nd_username, nd_password)
    headers = {
        'Content-Type': "application/json",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    payload = ""

    response = requests.request("GET", url, cookies=cookies, data=payload, headers=headers, verify=False)    
    result = json.loads(response.text)
    return result

# Delete
def deleteTenant(tenantId):
    shortUrl = "https://" + nd_ip + "/api/v1/tenants/"
    url = shortUrl + tenantId + "?msc-only=false&enableVersionCheck=true"
    cookies = getToken(nd_ip, nd_username, nd_password)
    payload = ""
    
    headers = {
        'Content-Type': "application/json",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    requests.request("DELETE", url, cookies=cookies, data=payload, headers=headers, verify=False)    


def main():

    result = getTenant()
    tenants = result["tenants"]

    deletingTenant = {}
    
    with open('ndoConfig.yaml', 'r') as file:
        # Load the YAML data from the file
        data = yaml.safe_load(file)

    for tenant in data["tenants"]:

        for t in tenants:
            if t['name'] == tenant:
                deletingTenant[tenant] = t['id']
    
    print(f"Deleting below tenants...")
    for tenantName in deletingTenant.keys():
        print(tenantName)
    for tenantId in deletingTenant.values():
        deleteTenant(tenantId)


if __name__ == '__main__':
    main()