class Category:
    def __init__(self, category):
        self.balance = 0.00
        self.ledger = []
        self.category = category

    def deposit(self, amount, description=""):
        self.balance = self.balance + amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance = self.balance - amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, transfer_amount, transfer_to):
        if self.check_funds(transfer_amount):
            transfer_to.deposit(transfer_amount, f"Transfer from {self.category}")
            self.withdraw(transfer_amount, f"Transfer to {transfer_to.category}")
            return True
        return False

    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        return False

    def __str__(self):
        sum = 0
        result = self.category.center(30, '*') + '\n'
        for i in range(len(self.ledger)):
            result += \
                f'{self.ledger[i]["description"][:23]}' \
                f'{str("%.2f" % (float(self.ledger[i]["amount"]))):>{30 - len(self.ledger[i]["description"][:23])}}' \
                + '\n'
            sum += self.ledger[i]['amount']
        result += f'Total: {sum}'
        return result


def create_spend_chart(categories):
    withdraws = []
    percent = []
    lens = []
    result = 'Percentage spent by category\n'

    for withdraw in categories:
        withdraws.append(-withdraw.ledger[1]['amount'])
        lens.append(withdraw.category)

    for withdraw in withdraws:
        perc = round(int((withdraw / sum(withdraws)) * 100) / 10) * 10
        if perc > 10:
            percent.append(perc)
        else:
            percent.append(0.00)

    for i in range(100, -10, -10):
        result += f'{i:>3}| '
        for perc in percent:
            result += 'o  ' if perc >= i else '   '
            perc -= 10
        result += '\n'

    result += f'    {"-" * 10}\n'

    for i in range(len(max(lens, key=len))):
        result += '     '
        for letter in categories:
            try:
                result += letter.category[i] + '  '
            except:
                result += '   '
        result += '\n'
    result = result[:-1]
    return result
