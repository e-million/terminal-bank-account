# -----------------------------------------------------------------
# Assignment Name:  Final
# Name:             Million Eyassu
# -----------------------------------------------------------------

# Customer Class
class Customer:

    _allCustomers = []  # list to store all customers
    _customerCount = 0  # Grand total of all customers created

    # Constructor
    def __init__(self, firstName, lastName, SSN):
        # adds every instance of Customer into the list
        self._allCustomers.append(self)
        self._customerCount += 1  # Adds 1 to total accounts created
        self.firstName = firstName.lower()  # first name
        self.lastName = lastName.lower()  # last name
        self.SSN = int(SSN)  # social

    # gets customer's name
    def getName(self):
        print(self.firstName + " " + self.lastName)


# Account Class

class Account(Customer):
    _totalAccounts = []  # array total of all customers created
    # Constructor

    def __init__(self, firstName, lastName, SSN, accountType, balance):
        # Inherits the props from the Customer Class
        Customer.__init__(self, firstName, lastName, SSN)
        # adds all instances of account class into an array
        self._totalAccounts.append(self)
        self.accountType = accountType  # checking or savings
        self.balance = balance  # balance

    # gets account type
    def getType(self):
        print(self.accountType)

    # gets balance
    def getBalance(self):
        print("Account balance is: {}".format(self.balance))

    # Makes sure the deposit is greater or equal to the minmum allowed
    def minimumDeposit(self, deposit):
        if deposit < 500:
            print('Deposit needs to be greater than 500 for SAVINGS account')
            return False
        else:
            return True

    # if savings goes below minimum deposit (500) Then return true
    def overdraftSavings(self, amount):
        if self.balance - amount < 500:  # minimum deposit
            print('Savings has gone below the minimum deposit amount (500)')
            return True
        else:
            return False

    # if savings goes below minimum deposit (500) Then return true
    def overdraftChecking(self, withdrawAmount):
        if self.balance - withdrawAmount < 0:  # if balance after transaction is 0 then, overdraft fee is applied
            print('Checking balance has been overdrafted. A $20.00 fee has been applied')
            self.balance -= 20  # add overdraft fee if account balance is below 0
            return True
        else:
            return False

    # Deposit to account
    def deposit(self, amount):
        # if number is valid
        if self.validateNumbers(amount) == True:
            # if account is savings
            if self.accountType == 's':
                # if the minimum deposit amount is acceptable
                if self.minimumDeposit(amount) == True:
                    # complete the deposit
                    self.balance += amount
                    print('You deposited: {}'.format(amount))
            else:
                # Else, if it is a checking account, go ahead with the transaction since there is no restriction on the deposit amount
                self.balance += amount  # Checking
                print('You deposited: {}'.format(amount))

    # Withdraw from account
    def withdraw(self, amount):
        # validate amount
        if self.validateNumbers(amount) == True:
            if self.accountType == 's':  # If its a savings account
                # if account has not been overdrafted
                if self.overdraftSavings(amount) == False:
                    self.balance -= amount  # complete withdrawal
                    print('You withdrew: {}'.format(amount))
            else:
                # Else, if it is a checking account, go ahead with the transaction since there is no restriction on the withdrawal amount
                self.overdraftChecking(amount)
                self.balance -= amount  # Checking account
                print('You withdrew: {}'.format(amount))

    def validateNumbers(self, intNumber):
        try:
            # convert intNumber into int
            int_Input = int(intNumber)
            # if intNumber is > 0, return true
            if(int_Input > 0):
                return True
            else:
                # else, give error message
                print("Your Number Must Be Positive")
        except ValueError:  # error message for non numeric values
            int_Input = int(0)
            print("Your Number Must be Numeric")
        return int_Input

    # returns the details of the customer accounts
    def __repr__(self):
        return "Name: {} {}, Balance: {}, Account Type: {}".format(self.firstName, self.lastName, self.balance, self.accountType)

    def transfer(self, obj, amount):

        # validate amount
        if self.validateNumbers(amount) == True:
            # if balance is < = 0, give error message
            if self.balance <= 0:
                print("Account balance insufficient")
            else:
                # else, continue with transfer
                self.withdraw(amount)
                obj.deposit(amount)

            # print balances for both accounts
            print("Balance after Transfer: " + str(self.balance))
            print("Balance after Transfer: " + str(obj.balance))

    def getTotalBalance(self):
        total = 0  # define variable
        ssn = self.SSN  # SSN of the instance that called the method
        listLen = len(self._allCustomers)  # length of customer array
        i = 0  # iterator

        # iterate through the _allCustomers list to get the total balance of all accounts
        while(i < listLen):
            if int(self._allCustomers[i].SSN) == ssn:  # See if SSN matches
                # Adds to the total balance
                total += int(self._allCustomers[i].balance)
                i += 1  # adds to the iterator

        # returns balance
        print("Total Balance of all " +
              str(self.lastName) + "'s accounts: " + str(total))

    def getTotalCheckingAmount(self):
        total = 0  # define variable
        ssn = self.SSN  # SSN of the instance that called the method
        listLen = len(self._allCustomers)  # length of array
        i = 0  # iterator

        # iterate through the _allCustomers list to get the total balance of all accounts
        while(i < listLen):
            if int(self._allCustomers[i].SSN) == ssn:  # See if SSN matches
                # Checks what type the account is
                if str(self._allCustomers[i].accountType) == 'c':
                    # Adds to the total balance
                    total += int(self._allCustomers[i].balance)
                i += 1  # adds to the iterator
        # returns balance
        print("Total Balance of all " +
              str(self.lastName) + "'s Checking accounts: " + str(total))

    def getTotalSavingsAmount(self):
        total = 0  # define variable
        ssn = self.SSN  # SSN of the instance that called the method
        listLen = len(self._allCustomers)  # length of array
        i = 0  # iterator

        # iterate through the _allCustomers list to get the total balance of all accounts
        while(i < listLen):
            if int(self._allCustomers[i].SSN) == ssn:  # See if SSN matches
                # Checks what type the account is
                if str(self._allCustomers[i].accountType) == 's':
                    # Adds to the total balance
                    total += int(self._allCustomers[i].balance)
                i += 1  # adds to the iterator

        # returns balance
        print("Total Balance of all " +
              str(self.lastName) + "'s Savings accounts: " + str(total))


#
#
#
#
#
#
#
# Tests #
# Multiple customer accounts can be created
# The accounts can be either savings or checking
# The accounts are set up by customer first name, last name, and SSN
jeffrey_S = Account('jeffrey', 'smith', 257487357, 's', 300)
jeffrey_C = Account('jeffrey', 'smith', 257487357, 'c', 500)
jeffrey_S2 = Account('jeffrey', 'smith', 257487357, 's', 3000)
jeffrey_C2 = Account('jeffrey', 'smith', 257487357, 'c', 5000)
#
# The savings account has a minimum deposit of $500.00.
jeffrey_S.deposit(300)
#
# The accounts can be added to or deducted from for any customer.
jeffrey_S.deposit(600)
jeffrey_C.deposit(500)
jeffrey_S.withdraw(150)
jeffrey_C.withdraw(200)
#
# The savings account cannot go below the minimum deposit.
jeffrey_S.withdraw(1000)
#
# If checking goes below the balance of 0, a fee of $20.00 is applied per transaction.
jeffrey_C.withdraw(1000)
jeffrey_C.getBalance()
#
# All deposits to any account must be numeric and above 0.
jeffrey_C.deposit('f')
jeffrey_S.deposit('w')
jeffrey_C.deposit(-2)
jeffrey_S.deposit(-5)
#
# All deductions from any account must be numeric and above 0
jeffrey_C.withdraw('f')
jeffrey_S.withdraw('w')
jeffrey_C.withdraw(-2)
jeffrey_S.withdraw(-5)
#
# At any time, the balance for checking and savings can be displayed per customer.
jeffrey_C.getBalance()
jeffrey_S.getBalance()
#
# At any time, the total balance for all accounts per customer can be viewed.
jeffrey_C.getTotalBalance()
jeffrey_C.getTotalSavingsAmount()
jeffrey_S.getTotalCheckingAmount()
#
# Transfer between accounts
jeffrey_S2.transfer(jeffrey_C, 200)
jeffrey_C2.transfer(jeffrey_S, 200)
