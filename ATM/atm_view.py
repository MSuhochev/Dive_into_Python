import logging


class AtmView:
    def __init__(self, logfile="atm.log"):
        """
        Initializing the AtmView object.

        Installs a logger to track errors.
        """
        self.logger = logging.getLogger("AtmView")
        self.configure_logging(logfile)  # Вызываем метод для настройки логирования

    def configure_logging(self, logfile):
        """Method for setting up the logging system."""
        logging.basicConfig(filename=logfile, level=logging.INFO)

    @staticmethod
    def display_balance(balance):
        """
        Display balance information.

        :param balance: Current balance.
        """
        print(f"Баланс: {balance:.2f} у.е.")

    @staticmethod
    def display_transaction_details(transaction_details):
        """
        Displays details of the latest transaction.

        :param transaction_details: Transaction details.
        """
        print("Подробная информация о последней операции:")
        print(transaction_details)

    @staticmethod
    def display_error(message):
        """Displays an error message."""
        print(f"Ошибка: {message}")
        logging.error(f"Ошибка: {message}")

    @staticmethod
    def display_user_info(user_manager, current_user_id):
        """
        Display information about the current user.

        :param user_manager: User manager.
        :param current_user_id: Current user ID.
        """
        user_info = user_manager.get_user_info(current_user_id)
        if user_info:
            print("Информация о пользователе:")
            for key, value in user_info.items():
                print(f"{key}: {value}")
        else:
            print("Пользователь не найден.")

    @staticmethod
    def display_account_info(balance, transaction_details):
        """
        Display account information.

        :param balance: Current balance.
        :param transaction_details: Details of the last transaction.
        """
        print(f"Информация о счете:")
        print(f"Баланс: {balance:.2f} у.е.")
        if transaction_details:
            print("Подробная информация о последней операции:")
            print(transaction_details)
