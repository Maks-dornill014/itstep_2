class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Ініціалізує банківський рахунок.
        :param account_number: Номер рахунку
        :param balance: Початковий баланс (за замовчуванням 0)
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Поповнює баланс рахунку.
        :param amount: Сума для поповнення
        """
        if amount > 0:
            self.balance += amount
            print(f"Депозит успішний: {amount} грн. Поточний баланс: {self.balance} грн.")
        else:
            print("Помилка: сума для поповнення повинна бути більше нуля.")

    def withdraw(self, amount):
        """
        Знімає кошти з рахунку, якщо достатньо балансу.
        :param amount: Сума для зняття
        """
        if amount <= 0:
            print("Помилка: сума для зняття повинна бути більше нуля.")
        elif amount > self.balance:
            print(f"Недостатньо коштів для зняття {amount} грн. Поточний баланс: {self.balance} грн.")
        else:
            self.balance -= amount
            print(f"Зняття успішне: {amount} грн. Поточний баланс: {self.balance} грн.")

    def __str__(self):
        """
        Інформація про рахунок у вигляді рядка.
        """
        return f"Номер рахунку: {self.account_number}, Баланс: {self.balance} грн."


# Приклад використання
if __name__ == "__main__":
    # Створення рахунку
    account = BankAccount("UA9876543210", 1000)  # Номер рахунку, баланс 1000 грн

    # Виведення інформації про рахунок
    print(account)

    # Поповнення балансу
    account.deposit(500)
    account.deposit(-200)  # Спроба некоректного поповнення

    # Зняття коштів
    account.withdraw(200)
    account.withdraw(2000)  # Спроба зняти більше, ніж є
    account.withdraw(-50)   # Спроба некоректного зняття

    # Підсумкова інформація про рахунок
    print(account)
