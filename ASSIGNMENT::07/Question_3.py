class Bank:
    def __init__(self):
        self.accs = {}

    def create_acc(self, name, bal=0):
        if name not in self.accs:
            self.accs[name] = bal

    def deposit(self, name, amt):
        if name in self.accs and amt > 0:
            self.accs[name] += amt

    def withdraw(self, name, amt):
        if name in self.accs and 0 < amt <= self.accs[name]:
            self.accs[name] -= amt 

    def get_bal(self, name):
        return self.accs.get(name, None)

    def display_accs(self):
        print("Accs:", self.accs)

b = Bank()
b.create_acc("Alice", 100)
b.create_acc("Bob")
b.deposit("Alice", 50)
b.withdraw("Alice", 30)
b.deposit("Bob", 200)
b.display_accs()
print("Alice Bal:", b.get_bal("Alice"))
