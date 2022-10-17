import requests
class Api:



    def check_postcode(code):
        url = "http://api.postcodes.io/postcodes/"
        tag = url + code
        response = requests.get(tag)
        if response.status_code == 200:
            return "Success"
        else:
            return "Please make sure you insert a correct postcode"

    def dis_url(code):
        url = "http://api.postcodes.io/postcodes/"
        tag = url + code
        return tag

    def show_postcode(code):
        url = "http://api.postcodes.io/postcodes/"
        tag = url + code

        if requests.get(tag).status_code == 200:
            response = requests.get(tag).json()["result"]
            print(response)
        else:
            print("Please make sure you insert correct postcode")
