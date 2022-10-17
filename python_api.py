import requests
# # get
# request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")
# # check the outcome of our API call
# status = request_bbc_status_code.status_code
# # let's check the header
# # print(request_bbc_status_code.headers)
# if status == 200:
#     print("success")
# else:
#     print("Unsuccessful")
# user input as postcode

url = "http://api.postcodes.io/postcodes/"
postcode = "e147le"
url_arg = url + postcode
response = requests.get(url_arg)
print(response.status_code)
print(response.content)
result_dict = response.json()
print(result_dict["result"])
print("The postcode is: "+ result_dict["result"]["postcode"])
longitude = result_dict["result"]["longitude"]
latitude = result_dict["result"]["longitude"]
print(f"the longitude is {longitude} and the latitude is {latitude}")

