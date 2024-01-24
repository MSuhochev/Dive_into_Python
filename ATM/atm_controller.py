import logging


class AtmController:
    def __init__(self, model, view, user_manager):
        """
        Initializing the AtmController object.

        :param model: ATM model.
        :param view: ATM view.
        :param user_manager: User manager.
        """
        self.model = model
        self.view = view
        self.user_manager = user_manager
        self.logger = logging.getLogger("AtmController")
        self.current_user_id = None

    def register_user(self, num_card, name, surname, username, password):
        """
        New User Registration.

        :param num_card: User card number.
        :param name: Username.
        :param surname: User's last name.
        :param username: User login.
        :param password: User password.
        """
        self.current_user_id = self.user_manager.register_user(num_card, name, surname, username, password)

    def login_user(self, username, password):
        """
        User login.

        :param username: User login.
        :param password: User password.
        :return: True if the login was successful, otherwise False.
        """
        user_id = self.user_manager.login_user(username, password)
        if user_id:
            self.current_user_id = user_id
            return True
        else:
            return False

    def deposit(self, amount):
        """
        Processing the account replenishment operation.

        :param amount: Amount to top up.
        """
        try:
            transaction_details = self.model.deposit(amount)
            self.view.display_transaction_details(transaction_details)
            self.view.display_balance(self.model.get_balance())        # Покажем итоговый баланс
            self.model.apply_interest()                                # Вызываем метод для начисления процентов
        except ValueError as e:
            self.view.display_error(str(e))
            self.logger.error(f"Ошибка при обработке пополнения: {e}")

    def withdraw(self, amount):
        """
        Processing the withdrawal transaction.

        :param amount: Amount to withdraw.
        """
        try:
            transaction_details = self.model.withdraw(amount)
            self.view.display_transaction_details(transaction_details)
            self.view.display_balance(self.model.get_balance())
        except ValueError as e:
            self.view.display_error(str(e))
            self.logger.error(f"Ошибка при обработке снятия: {e}")

    def display_user_info(self):
        """Display information about the current user."""
        self.view.display_user_info(self.user_manager, self.current_user_id)

    def display_balance(self, transaction_details=None):
        """
        Displaying balance information.

        :param transaction_details: Details of the last transaction.
        """
        balance = self.model.get_balance()
        self.view.display_account_info(balance, transaction_details)
