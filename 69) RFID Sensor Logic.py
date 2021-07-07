import time

def ChequeHelmet(helmet):
    if helmet:
        return helmet
    return False

def ChequeJacket(jacket):
    if jacket:
        return jacket
    return False

def ChequeGlasses(glasses):
    if glasses:
        return glasses
    return False

def ChequePhones(phones):
    if phones:
        return phones
    return False


inputdict = {"employees": [
{"id": 1, "name":"Victor", "helmet": True, "jacket": True, "glasses": True, "phones": True},
{"id": 2, "name":"Jaci", "helmet": False, "jacket": False, "glasses": False, "phones": False},
{"id": 3, "name":"Deby", "helmet": True, "jacket": True, "glasses": True, "phones": True},
{"id": 4, "name":"Homer", "helmet": False, "jacket": False, "glasses": False, "phones": True}]}

inputlist = [[1, "Victor", True, True, True, True],[2, "Jaci", False , False, False, False],
[3, "Deby", True, True, False, False],[4, "Homer", False, True, True, True]]

# 1) Teste com FOR no Dict/Json

for item in inputdict["employees"]:
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


# 2) Teste com FOR na List

for item in inputlist:
    time.sleep(3)
    print(f"Funcionário: {item[0]} - {item[1]}")
    
    if ChequeHelmet(item[2]) and \
        ChequeJacket(item[3]) and \
            ChequeGlasses(item[4]) and \
            ChequePhones(item[5]):
        print ("Acesso permitido!")
    else:
        print("Acesso negado!")
        if not ChequeHelmet(item[2]):
            print("O funcionário está sem capacete.")
        if not ChequeJacket(item[3]):
            print("O funcionário está sem jaqueta.")
        if not ChequeGlasses(item[4]):
            print("O funcionário está sem os óculos.")
        if not ChequePhones(item[5]):
            print("O funcionário está sem os fones de proteção.")