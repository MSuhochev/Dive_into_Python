from menu import print_initial_menu, print_main_menu, get_user_choice, configure_logging
from user_manager import UserManager
from atm_model import AtmModel
from atm_view import AtmView
from atm_controller import AtmController


def run_atm(logfile="atm.log", users_file="users.json"):
    """Function for starting the ATM."""
    configure_logging(logfile)                               # Setting up the logging system

    user_manager = UserManager(users_file)                   # Initialize user manager,
    model = AtmModel(user_manager)                           # model,
    view = AtmView()                                         # view,
    controller = AtmController(model, view, user_manager)    # and controller.

    while True:
        # Display the initial menu and get the user's choice.
        print_initial_menu()
        choice = get_user_choice()

        if choice == '1':
            # New User Registration.
            num_card = input("Введите номер карты: ")
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            controller.register_user(num_card, name, surname, username, password)
        elif choice == '2':
            # User login.
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            if controller.login_user(username, password):
                print("Вход выполнен успешно.")
                while True:
                    # Display the main menu and process user selection.
                    print_main_menu()
                    choice = get_user_choice()
                    if choice == '1':
                        # Payment to Bank account.
                        amount = int(input("Введите сумму для пополнения: "))
                        controller.deposit(amount)
                    elif choice == '2':
                        # Withdrawal from account.
                        amount = int(input("Введите сумму для снятия: "))
                        controller.withdraw(amount)
                    elif choice == '3':
                        # Display information about the user.
                        controller.display_user_info()
                    elif choice == '4':
                        # Display information about the account.
                        controller.display_balance()
                    elif choice == '5':
                        # Exit to the main menu.
                        break
                    else:
                        print("Неверный выбор. Пожалуйста, выберите от 1 до 5.")
            else:
                print("Ошибка входа. Проверьте логин и пароль.")
        elif choice == '3':
            # Terminate the program.
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 3.")
