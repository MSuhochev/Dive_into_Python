import logging


class AtmModel:
    def __init__(self, user_manager):
        """
        Initializing the AtmModel object.

        :param user_manager: User manager.
        """
        self.user_manager = user_manager
        self.logger = logging.getLogger("AtmModel")
        self.operations_count = 0  # Counter for operations
        self.balance = self.user_manager.get_current_user_balance()  # Initialize balance

    def deposit(self, amount):
        """
        Replenishment of the user account.

        :param amount: Replenishment amount.
        :return: Transaction details.
        :raises ValueError: If the top-up amount is not a multiple of 50.
        """
        try:
            user_id = self.user_manager.current_user_id
            self.logger.info(f"Попытка пополнения счета для пользователя {user_id}")
            balance_before = self.user_manager.get_current_user_balance()

            if amount % 50 == 0:
                self.user_manager.users[user_id]["Balance"] += amount
                self.operations_count += 1
                self.user_manager.save_users()

                balance_after = self.user_manager.get_current_user_balance()

                transaction_details = f"Пополнение: +{amount:.2f} у.е., " \
                                      f"Баланс до: {balance_before:.2f} у.е., " \
                                      f"Баланс после: {balance_after:.2f} у.е."

                self.logger.info(f"Пользователь {user_id} пополнил счет на {amount} у.е. "
                                 f"Баланс: {balance_after:.2f} у.е.")

                return transaction_details
            else:
                raise ValueError("Сумма пополнения должна быть кратна 50 у.е.")
        except ValueError as e:
            self.logger.error(f"Ошибка при пополнении счета пользователя {user_id}: {e}")
            raise e

    def withdraw(self, amount):
        """
        Withdrawing funds from the user's account.

        :param amount: Withdrawal amount.
        :return: Transaction details.
        :raises ValueError: If the withdrawal amount is not a multiple of 50 or exceeds the balance.
        """
        try:
            user_id = self.user_manager.current_user_id
            balance_before = self.user_manager.get_current_user_balance()

            if amount % 50 == 0 and amount <= balance_before:
                withdrawal_fee = max(30, min(0.015 * amount, 600))
                total_amount = amount + withdrawal_fee
                self.user_manager.users[user_id]["Balance"] -= total_amount
                self.user_manager.save_users()

                balance_after = self.user_manager.get_current_user_balance()

                transaction_details = f"Снятие: -{total_amount:.2f} у.е., " \
                                      f"Комиссия: -{withdrawal_fee:.2f} у.е., " \
                                      f"Баланс до: {balance_before:.2f} у.е., " \
                                      f"Баланс после: {balance_after:.2f} у.е."

                self.logger.info(f"Пользователь {user_id} снял {amount} у.е. "
                                 f"Баланс: {balance_after:.2f} у.е.")

                return transaction_details
            elif amount > balance_before:
                raise ValueError("Нельзя снять больше, чем на счете.")
            else:
                raise ValueError("Сумма снятия должна быть кратна 50 у.е.")
        except ValueError as e:
            self.logger.error(f"Ошибка при снятии средств пользователя {user_id}: {e}")
            raise e

    def apply_interest(self):
        """
        Applying interest to the user's balance.
        Interest is calculated every third time the transaction is performed.
        """
        user_id = self.user_manager.current_user_id
        if self.operations_count % 3 == 0:
            interest = 0.003 * self.user_manager.users[user_id]["Balance"]
            # self.balance += interest
            self.user_manager.users[user_id]["Balance"] += interest
            self.user_manager.save_users()
            self.logger.info(f"Начислены проценты: {interest} у.е.")
        pass

    def get_balance(self):
        """
        Getting the user's current balance.

        :return: Current balance.
        """
        return self.user_manager.get_current_user_balance()
