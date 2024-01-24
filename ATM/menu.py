import logging


def print_initial_menu():
    """Function menu before user login or registration in the system."""
    print("\nВыберите действие:")
    print("1. Зарегистрироваться")
    print("2. Войти")
    print("3. Завершить работу")


def print_main_menu():
    """Function menu after user login."""
    print("\nВыберите действие:")
    print("1. Пополнить")
    print("2. Снять")
    print("3. Информация о пользователе")
    print("4. Информация о счете")
    print("5. Выйти")


def get_user_choice():
    """Function to get user selection."""
    choice = input("Введите номер действия: ")
    return choice


def configure_logging(logfile="atm.log"):
    """Function for setting up the logging system."""
    logging.basicConfig(filename=logfile, level=logging.INFO)
