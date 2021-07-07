import json
import time

def ChequeHelmet(helmet):
    if helmet == "True":
        return True
    return False

def ChequeJacket(jacket):
    if jacket == "True":
        return True
    return False

def ChequeGlasses(glasses):
    if glasses == "True":
        return True
    return False

def ChequePhones(phones):
    if phones == "True":
        return True
    return False


with open ("jsonentry.json") as jsonfile:
    jsonfile = json.loads(jsonfile.read())

for item in jsonfile['messages']:
    time.sleep(3)
    print(f"Funcionário: {item['id']} - {item['name']}")
    
    if ChequeHelmet(item["helmet"]) and \
        ChequeJacket(item["jacket"]) and \
            ChequeGlasses(item["glasses"]) and \
            ChequePhones(item["phones"]):
        print ("Acesso permitido!")
    else:
        print("Acesso negado!")
        if not ChequeHelmet(item["helmet"]):
            print("O funcionário está sem o capacete.")
        if not ChequeJacket(item["jacket"]):
            print("O funcionário está sem a jaqueta de proteção.")
        if not ChequeGlasses(item["glasses"]):
            print("O funcionário está sem os óculos de proteção.")
        if not ChequePhones(item["phones"]):
            print("O funcionário está sem os fones de proteção.")
