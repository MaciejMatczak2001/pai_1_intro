#!/usr/bin/python3
import urllib

import requests

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"


def checkHTTP(url_link):
    r = requests.get(url_link)
    if 400 <= r.status_code < 600:
        raise Exception("error")
    return r.json()


if __name__ == '__main__':
    print(checkHTTP(url))
