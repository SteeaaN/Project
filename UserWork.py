from parms import *
import requests
from lxml import etree
import lxml.html


def printBalance(lg):
    cursor.execute(f"SELECT balance FROM users WHERE login= '{lg}'")
    print("Баланс:", cursor.fetchone()[0])


def printSaves(lg):
    cursor.execute(f"SELECT save FROM users WHERE login= '{lg}'")
    print("Отложено:", cursor.fetchone()[0])


def add(lg):
    amount = exiter()
    match amount:
        case 0:
            return
        case _:
            cursor.execute(f"SELECT balance FROM users WHERE login= '{lg}'")
            bal = cursor.fetchone()[0]
            db.execute(f"UPDATE users SET balance = {bal + amount} WHERE login= '{lg}'")
            db.commit()
            print("Успешно!")
            printBalance(lg)


def subtract(lg):
    amount = exiter()
    match amount:
        case 0:
            return
        case _:
            cursor.execute(f"SELECT balance FROM users WHERE login= '{lg}'")
            bal = cursor.fetchone()[0]
            match bal:
                case bal if bal < amount:
                    print("Недостаточно средств.")
                    subtract(lg)
                case _:
                    cursor.execute(f"SELECT balance FROM users WHERE login= '{lg}'")
                    bal = cursor.fetchone()[0]
                    db.execute(f"UPDATE users SET balance = {bal - amount} WHERE login= '{lg}'")
                    db.commit()
                    print("Успешно!")
                    printBalance(lg)


def saving(lg):
    amount = exiter()
    match amount:
        case 0:
            return
        case _:
            cursor.execute(f"SELECT balance FROM users WHERE login= '{lg}'")
            bal = cursor.fetchone()[0]
            match bal:
                case bal if bal < amount:
                    print("Недостаточно средств.")
                    saving(lg)
                case _:
                    cursor.execute(f"SELECT save FROM users WHERE login= '{lg}'")
                    save = cursor.fetchone()[0]
                    cursor.execute(f"SELECT balance FROM users WHERE login= '{lg}'")
                    bal = cursor.fetchone()[0]
                    db.execute(f"UPDATE users SET save = {save + amount} WHERE login= '{lg}'")
                    db.execute(f"UPDATE users SET balance = {bal - amount} WHERE login= '{lg}'")
                    db.commit()
                    printSaves(lg)
                    printBalance(lg)


def spendsaves(lg):
    amount = exiter()
    match amount:
        case 0:
            return
        case _:
            cursor.execute(f"SELECT save FROM users WHERE login= '{lg}'")
            save = cursor.fetchone()[0]
            match save:
                case save if save < amount:
                    print("Недостаточно средств.")
                    spendsaves(lg)
                case _:
                    cursor.execute(f"SELECT save FROM users WHERE login= '{lg}'")
                    save = cursor.fetchone()[0]
                    cursor.execute(f"SELECT balance FROM users WHERE login= '{lg}'")
                    bal = cursor.fetchone()[0]
                    db.execute(f"UPDATE users SET save = {save - amount} WHERE login= '{lg}'")
                    db.execute(f"UPDATE users SET balance = {bal + amount} WHERE login= '{lg}'")
                    db.commit()
                    printSaves(lg)
                    printBalance(lg)


def course():
    api = requests.get("https://www.cbr.ru/currency_base/daily/")
    tree = lxml.html.document_fromstring(api.text)
    crs = tree.xpath('//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr[12]/td[5]/text()')
    print("1 USD =", crs[0][:-2], "RUB")


def exiter():
    print("0 - Выход")
    amount = int(input("Введите сумму: "))
    return amount
