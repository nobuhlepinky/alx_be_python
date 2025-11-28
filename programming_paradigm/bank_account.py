class BankAccount:
    def __init__(self, initial_balance=0.0):
        if initial_balance < 0:
            initial_balance = 0.0
            print("Initial balance cannot be negative. Setting to $0.00.")

        self._account_balance = initial_balance

    def get_balance(self):
        return self._account_balance

    def deposit(self, amount):
            if amount > 0:
                self._account_balance += amount
            else:
                pass  # Ignore negative deposits
    def withdraw(self, amount):
         if amount <= 0:
            
            return False
        
         if self._account_balance >= amount:
            self._account_balance -= amount
            return True
         else:
            # Insufficient funds
            return False    

    def display_balance(self):
            print (f"Current Balance:${self._account_balance:.2f}") 
