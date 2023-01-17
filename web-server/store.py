import requests

def get_categories():
    req = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(req.status_code)
    print(req.text)
    print(type(req.text))

    # transforma el string en diccionarios 
    categories = req.json()
    for category in categories:
        print(category['name'])
