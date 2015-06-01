print type(3.14)

def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60 
    
print clock_helper(90)

val1 = [1, 2, 3]
val2 = val1[1:]
val1[2]  = 4

print val2[1]

def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    sum_of_last_three = 0
    
    # main loop
    for i in range(25):
        # sum the last three items in the list
        last_item_index = len(lst)-1
        sum_of_last_three = lst[last_item_index] + lst[last_item_index-1] + lst[last_item_index-2] 
        lst.append(sum_of_last_three)
    
    
sum_three = [0, 1, 2]

appendsums(sum_three)

print sum_three[20]


### ###

class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """

    __balance = 0
    __fees_paid = 0
    
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.__balance = initial_balance
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.__balance += amount
        
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.__balance -= amount
        
        if self.__balance < 0:
            self.__balance -= 5
            self.__fees_paid += 5
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.__balance
    
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.__fees_paid
        
## Testing ##
print "Testing class."

my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5) 
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50) 
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 

print my_account.get_balance(), my_account.get_fees()


    