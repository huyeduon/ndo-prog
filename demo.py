from config import nd_username, nd_password, nd_ip
from ndlogin import *
import yaml
import json
import requests
import urllib3
urllib3.disable_warnings()

# Display information about all current sites added on ND
def getSite():
    url = "https://" + nd_ip + "/api/v1/sites/"
    cookies = getToken(nd_ip, nd_username, nd_password)
    payload = ""
    headers = {
        'Content-Type': "application/json",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, cookies=cookies, data=payload, headers=headers, verify=False)    
    result = json.loads(response.text)
    return result

# Create a tenant on NDO and associate it to both sites.
def createTenant(tenantName):
    url = "https://" + nd_ip + "/api/v1/tenants/"
    cookies = getToken(nd_ip, nd_username, nd_password)
    data = {
            "displayName": tenantName,
            "name": tenantName,
            "siteAssociations":
            [
                {
                    "siteId": "625132ff1c3d5c069d4a79b1"
                },
                {
                    "siteId": "6251331b1c3d5c069d4a79b2"
                }
            ]
    }
    
    headers = {
        'Content-Type': "application/json",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    payload = json.dumps(data)
    requests.request("POST", url, cookies=cookies, data=payload, headers=headers, verify=False)    


def main():

    print("Get existing sites:")
    print(f"-----------------")
    # list of existing sites
    siteNames = getSite()
    siteList = siteNames['sites']
    for site in siteList:
        print(f"Site ID:",site["id"])
        print(f"Site Name:",site["name"])
        print(f"Site URL:",site["urls"])    
        print(f"==========*******==========")
    

    with open('ndoConfig.yaml', 'r') as file:
        # Load the YAML data from the file
        data = yaml.safe_load(file)
    print("Creating tenants on NDO...")
    for tenant in data["tenants"]:
        print(tenant)
        createTenant(tenant)
  

if __name__ == '__main__':
    main()