import requests
# get
request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")
# check the outcome of our API call
status = request_bbc_status_code.status_code
# let's check the header
# print(request_bbc_status_code.headers)
if status == 200:
    print("success")
else:
    print("Unsuccessful")

