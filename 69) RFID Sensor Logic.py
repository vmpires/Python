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

def ChequeBoots(boots):
    if boots:
        return boots
    return False


inputdict = {"employees": [
{"id": 1, "name":"Victor", "helmet": True, "jacket": True, "glasses": True, "boots": True},
{"id": 2, "name":"Jaci", "helmet": False, "jacket": False, "glasses": False, "boots": False},
{"id": 3, "name":"Deby", "helmet": True, "jacket": True, "glasses": True, "boots": True},
{"id": 4, "name":"Homer", "helmet": False, "jacket": False, "glasses": False, "boots": True}]}

inputlist = [[1, "Victor", True, True, True, True],[2, "Jaci", False , False, False, False],
[3, "Deby", True, True, False, False],[4, "Homer", False, False, False, True]]

# 1) Teste com FOR no Dict

for item in inputdict["employees"]:
    print(f"Funcionário: {item['id']} - {item['name']}")
    
    if ChequeHelmet(item["helmet"]) and \
        ChequeJacket(item["jacket"]) and \
            ChequeGlasses(item["glasses"]) and \
            ChequeBoots(item["boots"]):
        print ("Acesso permitido!")
    else:
        print("Acesso negado!")
        if not ChequeHelmet(item["helmet"]):
            print("O funcionário está sem capacete.")
        if not ChequeJacket(item["jacket"]):
            print("O funcionário está sem jaqueta.")
        if not ChequeGlasses(item["glasses"]):
            print("O funcionário está sem os óculos.")
        if not ChequeBoots(item["boots"]):
            print("O funcionário está sem as botas.")


# 2) Teste com FOR na List

for item in inputlist:
    print(f"Funcionário: {item[0]} - {item[1]}")
    
    if ChequeHelmet(item[2]) and \
        ChequeJacket(item[3]) and \
            ChequeGlasses(item[4]) and \
            ChequeBoots(item[5]):
        print ("Acesso permitido!")
    else:
        print("Acesso negado!")
        if not ChequeHelmet(item[2]):
            print("O funcionário está sem capacete.")
        if not ChequeJacket(item[3]):
            print("O funcionário está sem jaqueta.")
        if not ChequeGlasses(item[4]):
            print("O funcionário está sem os óculos.")
        if not ChequeBoots(item[5]):
            print("O funcionário está sem as botas.")


# 3) Teste com FOR no arquivo CSV

# 4) Teste com FOR no arquivo Excel

# 5) Teste com FOR no arquivo JSON