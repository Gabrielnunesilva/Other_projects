class Category():
    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.current_balance = 0

    def __str__(self):
        title = f"{self.name:*^30}\n"
        extract = ""
        for transaction in self.ledger:
            amount = f"{transaction['amount']:.2f}"
            description = f"{transaction['description'][:23]}"
            extract += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + extract + total

    def deposit(self, amount, description=""):
        amount = float(amount)
        self.register_in_ledger(amount, description)
        self.set_balance(amount)

    def withdraw(self, amount, description=""):
        amount = float(amount)
        have_funds = self.check_funds(amount)
        if have_funds:
            amount = -amount
            self.register_in_ledger(amount, description)
            self.set_balance(amount)
            return True
        return False

    def transfer(self, amount, category):
        have_funds = self.check_funds(amount)
        if have_funds:
            description = f"Transfer to {category.name}"
            self.withdraw(amount, description)
            description = f"Transfer from {self.name}"
            category.deposit(amount, description)
            return True
        return False

    def check_funds(self, amount):
        amount = float(amount)
        current_balance = self.get_balance()
        if current_balance < amount:
            return False
        return True

    def register_in_ledger(self, amount, description="deposit"):
        transaction = {'amount': float(amount), 'description': description}
        self.ledger.append(transaction)

    def get_balance(self):
        return sum(transaction["amount"] for transaction in self.ledger)

    def set_balance(self, amount):
        self.current_balance += float(amount)


def create_spend_chart(categories):
    import math


    categorie_loots = []
    values_graphic = []
    for categorie in categories:
        loot = sum(transaction["amount"] for transaction in categorie.ledger if transaction["amount"] < 0)
        categorie_loots.append({'categorie': categorie.name, 'loot': float(loot)})

    total_loot_categories = sum(transaction["loot"] for transaction in categorie_loots)

    for categorie_loot in categorie_loots:
        value = (categorie_loot['loot'] / total_loot_categories) * 100
        percentage = math.floor(value / 10) * 10
        values_graphic.append(percentage)


    graphic_title = 'Percentage spent by category'
    bar_percent = "\n"
    for i in range(100, -1, -10):
        bar_percent += f"{i:>3}|"
        for value in values_graphic:
            bar_percent += " o " if value >= i else "   "
        bar_percent += " \n"


    separator_width = "-" * ((len(categories) * 3) + 1)
    separator_graphic = f"    {separator_width}\n"


    max_len_legend = max(len(categorie.name) for categorie in categories)
    legends_filled = [categorie.name.ljust(max_len_legend) for categorie in categories]
    categorie_legend = ""
    for i in range(max_len_legend):
        categorie_legend += "     "  
        for name in legends_filled:
            categorie_legend += name[i] + "  "  
        categorie_legend += "\n"

    graphic = graphic_title + bar_percent + separator_graphic + categorie_legend.rstrip("\n")
    return graphic


# TESTE
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(create_spend_chart([food, clothing]))

