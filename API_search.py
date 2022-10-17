from API_class import Api as search


promt = True


while promt:
    p = search.check_postcode(input("Please type your postcode: "))
    print(p)
    if p == "Success":
        promt = False
promt2 = True
while promt2:
    p = search.show_postcode(input("Please type your postcode: "))
    print(p)
