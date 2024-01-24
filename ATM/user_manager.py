import json
import logging


class UserManager:
    def __init__(self, filename="users.json", logfile="atm.log"):
        """
        Initializing the UserManager object.

        :param filename: File name to store user data (default "users.json").
        """
        self.users = {}                                      # Dictionary of users.
        self.current_user_id = None                          # ID of the current user.
        self.filename = filename                             # File name to store data.
        self.logger = logging.getLogger("UserManager")
        self.configure_logging(logfile)
        self.load_users()                                    # Load data when creating an object.


    def configure_logging(self, logfile):
        """Method for setting up the logging system."""
        logging.basicConfig(filename=logfile, level=logging.INFO)

    def load_users(self):
        """
        Loading user data from a JSON file.

        If the file is not found, a new one is created. If an error occurs while decoding JSON,
        an error message is generated.
        """
        try:
            with open(self.filename, 'r') as file:
                self.users = json.load(file)
            self.logger.info("Данные пользователей загружены успешно.")
        except FileNotFoundError:
            self.logger.warning("Файл с данными пользователей не найден. Создан новый.")
        except json.JSONDecodeError:
            self.logger.error("Ошибка при декодировании JSON файла.")

    def save_users(self):
        """
        Saving user data to a JSON file.

        If an error occurs while encoding data into JSON, an error message is generated.
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.users, file, indent=4)
            self.logger.info("Данные пользователей сохранены успешно.")
        except json.JSONDecodeError:
            self.logger.error("Ошибка при кодировании данных в JSON формат.")

    def set_current_user(self, user_id):
        """
        Setting the current user by ID.

        :param user_id: User ID.
        """
        self.current_user_id = user_id

    def get_current_user_balance(self):
        """
        Getting the current balance of the current user.

        :return: User's current balance.
        """
        if self.current_user_id is not None:
            return self.users.get(self.current_user_id, {}).get("Balance", 0)
        return 0

    def register_user(self, num_card, name, surname, username, password):
        """
        New User Registration.

        :param num_card: Card number.
        :param name: Username.
        :param surname: User's last name.
        :param username: User login.
        :param password: User password.
        :return: New user ID.
        """
        START_BALANCE = 0
        user_id = len(self.users) + 1
        user_info = {
            "ID": user_id,
            "NumCard": num_card,
            "Name": name,
            "Surname": surname,
            "Username": username,
            "Password": password,
            "Balance": START_BALANCE
        }
        self.users[user_id] = user_info
        self.save_users()
        self.logger.info(f"Зарегистрирован новый пользователь: {user_info}")
        return user_id

    def login_user(self, username, password):
        """
        User login.

        :param username: User login.
        :param password: User password.
        :return: User ID if login is successful, None otherwise.
        """
        for user_id, user_info in self.users.items():
            if user_info["Username"] == username and user_info["Password"] == password:
                self.set_current_user(user_id)
                self.logger.info(f"Пользователь {user_info['Username']} вошел в свой аккаунт.")
                return user_id
        self.logger.warning("Попытка входа с неверными учетными данными.")
        return None

    def get_user_info(self, user_id):
        """
        Obtaining information about the user by his ID.

        :param user_id: User ID.
        :return: User information if found, None otherwise.
        """
        return self.users.get(user_id)
