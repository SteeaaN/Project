from AuthWork import ath_cheking, goto_exit
from UserWork import printBalance, printSaves, spendsaves, add, saving, subtract, course


class auth:
    def __init__(self):
        self.ansv()

    def ansv(self):
        print(f"1 - Вход\n2 - Регистрация\n0 - Выход")
        ansver = input("Выберите действие: ")
        match ansver:
            case "1":
                result = ath_cheking('login')
                match result[1]:
                    case True:
                        userr = User(result[0])
                    case _:
                        pass
            case "2": ath_cheking("registration")
            case "0": goto_exit()
            case _: print("Ошибка ввода!")
        self.ansv()


class User:
    def __init__(self, login):
        self.lg = login
        self.ansv()

    def ansv(self):
        print(f"1 - Вывести баланс на экран\n2 - Вывести сбережения на экран\n3 - Добавить\n4 - Вычесть\n5 - Отложить\n"
              f"6 - Перевести сбережения на баланс\n7 - Курс рубля к доллару\n0 - Выход из аккаунта")
        res = input("Выберите действие: ")
        match res:
            case "1": printBalance(self.lg)
            case "2": printSaves(self.lg)
            case "3": add(self.lg)
            case "4": subtract(self.lg)
            case "5": saving(self.lg)
            case "6": spendsaves(self.lg)
            case "7": course()
            case "0": use = auth()
            case _: print("Ошибка ввода")
        self.ansv()


def main():
    use = auth()


if __name__ == "__main__":
    main()
