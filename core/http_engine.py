import requests

class HTTPEngine:
    def __init__(self, url):
        self.url = url

    def request(self):
        try:
            r = requests.get(self.url)
            print (str(r))
        except requests.exceptions.RequestException as e:
            print("Request Error: "+ str(e))

        

class HTTPResponse:
    return 0

class HTTPError:
    return 0




