print('{:^60}'.format("Witaj w programie do tworzenia listy dłużników!"))
print('{:^60}'.format("Możesz stworzyć listę osób, które wiszą ci hajs"))
print('{:^60}'.format("Wpisz \"stop\" aby zakończyć dodawanie dłużników do listy"))
print('{:^60}'.format("Lista zostanie wyświetlona na ekranie\n"))


def createdebtorslist():
    debtors = []
    while 0 < 1:
        name = input("Podaj imię: ")
        if name == "stop":
            break
        amount = input("Podaj kwotę długu(sama liczba): ")
        if amount == "stop":
            break
        debtor = {
            name: amount
        }
        debtors.append(debtor)
    return debtors


def printlist(givenlist):
    print("Lista: ")
    for i in givenlist:
        for key, value in i.items():
            print('{:<10}'.format(key) + " - " + value + "zł")


debtorslist = createdebtorslist()
printlist(debtorslist)
