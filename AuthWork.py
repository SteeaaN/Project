from parms import *


def ath_cheking(tp):
    ath_result = ath(tp)
    match ath_result:
        case 0:
            return[0, False]
        case _:
            validly = check(ath_result[0])
            match tp:
                case tp if tp == "login":
                    fnc_result = Lg_Checking(ath_result[0], ath_result[1], validly)
                    return [ath_result[0], fnc_result]
                case _:
                    Reg_Checking(ath_result[0], ath_result[1], validly)


def ath(tp):
    print("0 - Назад")
    lg = input("Введите логин: ")
    match lg:
        case "0":
            return 0
        case lg if len(lg) > 2:
            pw = input("Введите пароль: ")
            match pw:
                case pw if pw == "0":
                    return 0
                case pw if len(pw) > 2:
                    return [lg, pw]
                case _:
                    print("Пароль должен содержать минимум 3 символа!")
                    ath_cheking(tp)
        case _:
            print("Логин должен содержать минимум 3 символа!")
            ath_cheking(tp)


def check(lg):
    cursor.execute(f"SELECT login FROM users WHERE login = '{lg}'")
    match cursor.fetchone():
        case None:
            x = False
        case _:
            x = True
    return x


def Lg_Checking(lg, pw, x):
    match x:
        case False:
            print("Неверно введен логин или пароль.")
            ath_cheking("login")
        case True:
            cursor.execute(f"SELECT password FROM users WHERE login = '{lg}'")
            match cursor.fetchone():
                case cursor.fetchone() if pw in cursor.fetchone():
                    print("Успешно!")
                    y = True
                    return y
                case _:
                    print("Неверно введен логин или пароль.")
                    ath_cheking("login")


def Reg_Checking(lg, pw, x):
    match x:
        case False:
            cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (lg, pw, 0, 0))
            db.commit()
            print("Успешно!")
        case True:
            print("Пользователь с таким логином уже существует!")
            ath_cheking("registration")


def goto_exit():
    print("Завершение работы...")
    exit()
