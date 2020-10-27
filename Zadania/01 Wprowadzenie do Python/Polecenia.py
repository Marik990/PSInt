Lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
liczba_liter1 = "c"
liczba_liter2 = "ł"
# print("W tekście jest " + str(Lorem.count(liczba_liter1)) + f" liter {liczba_liter1} oraz " + str(Lorem.count(liczba_liter2)) + f" liter {liczba_liter2}")
# print(dir(Lorem))
# help(Lorem.join)

word = "Krzysztof Krawczyk"
# print(word[::-1])

listaOriginal = list(range(1, 11))
listaCopy = listaOriginal[5:11]
del listaOriginal[5:11]
# print(listaOriginal)
# print(listaCopy)

listaOriginal = listaOriginal + listaCopy
listaOriginal.insert(-1,0)
listaCopy = listaOriginal.copy()
listaCopy.sort(reverse=True)
# print(listaOriginal)
# print(listaCopy)

student1 = ("111111", "Jan", "Kowalski")
student2 = ("222222", "Adam", "Nowak")
student3 = ("333333", "Katarzyna", "Szczepaniak")
listaStudentow = [
    student1,
    student2,
    student3
]
#print(listaStudentow)

student1 = ("Jan", "Kowalski", 22,"j.kowalski@gmail.com", 1999, "adres1")
student2 = ("Adam", "Nowak", 23, "a.nowak@gmail.com", 1998, "adres2")
student3 = ("Katarzyna", "Szczepaniak", 22, "k.szczepaniak@gmail.com", 1999, "adres3")
listaStudentowDict = dict([("111111", student1), ("222222", student2), ("333333", student3)])
#print(listaStudentowDict)

telefony = [
    666555444,
    111222333,
    666555444,
    777666555,
    666555444,
    516259423
]
#print(telefony)
telefony = set(telefony)
#print(telefony)

for i in range(1, 11):
    print(i)

for i in range(100, 19, -5):
    print(i)