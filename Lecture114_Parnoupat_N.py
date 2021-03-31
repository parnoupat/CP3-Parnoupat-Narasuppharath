from forex_python.converter import *
import math
c = CurrencyRates()
c_code = CurrencyCodes()
def all_menu_list():
    currency_list = []
    all_currency = c.get_rates('USD')
    key_all_currency = all_currency.keys()
    for number, key in zip(range(len(key_all_currency)), key_all_currency):
        currency_list.append([number+1])
        currency_list[number].append(key)
    for i in range(len(currency_list)):
        print(currency_list[i][0], " : ", currency_list[i][1], end = " ///// ")
def frequency_menu_list():
    frequency_currency_list = ['USD', 'HKD', 'THB', 'EUR', 'CNY', 'JPY']
    print("Currency List".center(60, "-"))
    for list in range(len(frequency_currency_list)):
        print(frequency_currency_list[list], end = " //// ")
    print("")
    return frequency_currency_list
def isfloat(x):
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True
def isint(x):
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b
def start_currency_input():
    start_currency = input("ใส่สกุลเงินที่ท่านถืออยู่ :").upper()
    while start_currency not in frequency_currency_list:
        print("ใส่ไรมาเนี่ย")
        start_currency = input("ใส่สกุลเงินที่ท่านถืออยู่ :").upper()
    return start_currency
def start_amount_input():
    start_amount = input("ใส่จำนวนเงินที่ท่านมี :")
    while not isfloat(start_amount) or not isint(start_amount):
        print("ใส่ตัวเลขครับ")
        start_amount = input("ใส่จำนวนเงินที่ท่านมี :")
    start_amount = float(start_amount)
    return start_amount
def end_currency_input():
    end_currency = input("ต้องการเปลี่ยนเป็นเงินสกุล ? >>>").upper()
    while end_currency not in frequency_currency_list:
        print("ใส่ไรมาเนี่ย")
        end_currency = input("ใส่สกุลเงินที่ท่านถืออยู่ :").upper()
    return end_currency
def calculate_currency():
    start_currency = start_currency_input()
    start_amount = start_amount_input()
    end_currency = end_currency_input()

    exchange = c.convert(start_currency, end_currency, start_amount)
    int_exchange = math.floor(exchange)
    print("คุณสามารถแลกเงินสกุล", c_code.get_currency_name(end_currency), "ได้", int_exchange, c_code.get_symbol(end_currency), end=" ")

    dif_exchange = round(exchange - int_exchange, 2)
    reverse_rate = round(c.get_rate(end_currency, start_currency), 2)
    change_exchange = math.floor(dif_exchange * reverse_rate)
    print("และเหลือเงินทอน : ", change_exchange, c_code.get_symbol(start_currency))
frequency_currency_list = frequency_menu_list()
calculate_currency()

