# Login to ND
import requests
import json
import urllib3
urllib3.disable_warnings()

# return token
def getToken(nd_ip, nd_username, nd_password):
    url = "https://" + nd_ip + "/login"
    data = {
        "userName": nd_username,
        "userPasswd": nd_password,
        "domain": "DefaultAuth"
    }
    payload = json.dumps(data)
    headers = {
        'Content-Type': "application/json",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request(
        "POST", url, data=payload, headers=headers, verify=False)
    token = json.loads(response.text)

    cookies = {}
    cookies['AuthCookie'] = token['token']
    return cookies

def main():
    pass

if __name__ == "__main__":
    main()