def fun1(a_list, b_list):
    c_list = list()
    for i in range(0, len(a_list), 2):
        c_list.append(i)
    for i in range(1, len(b_list), 2):
        c_list.append(i)
    return c_list


def fun2(data_text):
    dict = {
        "length": len(data_text),
        "letters": list(data_text),
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower(),
    }
    return dict


def fun3(text, letter):
    return text.replace(letter, "")


def fun4(temperature_value, temperature_type):
    if temperature_type == "Fahrenheit":
        return (temperature_value * 1.8) + 32
    elif temperature_type == "Rankine":
        return (temperature_value + 273.15) * 1.8
    elif temperature_type == "Kelvin":
        return temperature_value + 273.15
    else:
        return "ERROR"

class Calculator:
    def add(self, a, b):
        return a + b
    def difference(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b

class ScienceCalculator(Calculator):
    def power(self, a, b):
        return pow(a, b)

def fun5(tekst):
    return tekst[::-1]

print(fun5("koteł"))
