import requests

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

r = requests.get(url)
response = r.json()


if __name__ == '__main__':
    print(response)
