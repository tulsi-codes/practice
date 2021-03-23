import json 
#JSON was not the best way to do this but I needed practice in JSON which is why i choose it! 
#I know there are ways to shorten this code -- hoping to go over this in our next meeting

clients = "/Users/tulsipatel/Documents/DataEngineering/BankAccount/clients.json"
employees = "/Users/tulsipatel/Documents/DataEngineering/BankAccount/emp.json"
accounts = "/Users/tulsipatel/Documents/DataEngineering/BankAccount/account.json"
log_activity = "/Users/tulsipatel/Documents/DataEngineering/BankAccount/log_activity.json"

class BankAccount:
    #takes initial values (only for money use)
    def __init__(self, amount = 0, account_id = 0, account_name = ""):
        self.amount = amount
        self.account_id = account_id
        self.account_name = account_name

    
    

    def withdraw(self):
        #reads file
        with open(accounts) as f:
            data = json.load(f)
            f.close()
                        
        #looks for item and replaces value    
        for item in data["Account"]:
            if item["account_id"] == self.account_id:
                item[self.account_name] = item[self.account_name] - self.amount
                print(item)

        #writes account
        with open(accounts, "w") as outfile:
           json.dump(data, outfile, indent=2)

        #reads log
        with open (log_activity) as l:
            log_file = json.load(l)
            temp = log_file['log_file']

        #new log info
        yeter = {
            "account_id" : self.account_id, 
            "type_account" : self.account_name,
            "subtracted" : self.amount,
            "add" : 0
        }
        
        temp.append(yeter)

        #writes log
        with open(log_activity, "w") as outfile_l:
           json.dump(log_file, outfile_l, indent=2)  


    def deposit(self):
        #reads file
        with open (accounts) as f:
            data = json.load(f)
            f.close() 
                        
        #looks for item and replaces value    
        for item in data["Account"]:
            if item["account_id"] == self.account_id:
                item[self.account_name] = item[self.account_name] + self.amount
                print(item)

        #writes account
        with open(accounts, "w") as outfile:
           json.dump(data, outfile, indent=2)

        #reads log
        with open (log_activity) as l:
            log_file = json.load(l)
            temp = log_file['log_file']

        #log info
        yeter = {
            "account_id" : self.account_id, 
            "type_account" : self.account_name,
            "subtracted" : 0,
            "add" : self.amount
        }
        
        temp.append(yeter)

        #writes log
        with open(log_activity, "w") as outfile_l:
           json.dump(log_file, outfile_l, indent=2)  

    def new_client(self, account_id, f_name, l_name, address, phone_num,services, emp_id):

        self.account_id = account_id
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.phone_num = phone_num
        self.services = services
        self.emp_id = emp_id

        # read file
        with open (clients) as l:
            log_file = json.load(l)
            temp = log_file['Clients']
            l.close()
        
        #new info
        yeter = {
            "account_id" : self.account_id,
            "f_name" : self.f_name,
            "l_name" : self.l_name,
            "address" : self.address,
            "phone_num" : self.phone_num,
            "services" : self.services,
            "emp_id" : self.emp_id
        }
        
        temp.append(yeter)

        #writes to clients
        with open(clients, "w") as outfile_l:
           json.dump(log_file, outfile_l, indent=2)


    def new_emp(self, name, position, years_active, emp_id):

        
        self.name = name
        self.position = position
        self.years_active = years_active
        self.emp_id = emp_id

        
        with open (employees) as l:
            log_file = json.load(l)
            temp = log_file['Employee']
            l.close()
        
        #new info
        yeter = {
            "emp_id" : self.emp_id,
            "name" : self.name,
            "position" : self.position,
            "years_active" : self.years_active
        }
        
        temp.append(yeter)

        #writes to emp
        with open(employees, "w") as outfile_l:
           json.dump(log_file, outfile_l, indent=2) 



#there is test info a the bottom you can use 
#all new info! just run to test :)

#code below is for the user in the command line 

user_input = input("What would you like to do \n 1: Withdraw or \
Deposit money into an account \n 2: Open a new account \n 3: Add new empoloyee: ")


if user_input == 1:
    one = input("Do you want to withdraw (W) or deposit (D): ")
    if one == "D":
        while True:
            try:
                amount = int(input("Enter the Amount: "))
                break
            except ValueError:
                print("Opps! You need to enter a number!")
        while True:
            try:
                ID = int(input("Enter the ID: "))
                break 
            except ValueError:
                print("Opps! You need to enter a number!")
        while True:
            try:
                Account = input("Enter the account type: ")
                break 
            except KeyError:
                print("Enter a valid account type for the ID:")
        d = BankAccount(amount, ID, Account) 
        d.deposit()
    if one == "W":
        while True:
            try:
                amount = input("Enter the Amount: ")
                break
            except ValueError:
                print("Opps! You need to enter a number!")
        while True:
            try:
                ID = int(input("Enter the ID: "))
                break 
            except ValueError:
                print("Opps! You need to enter a number!")
        Account = input("Enter the account type: ")
        d = BankAccount(amount, ID, Account) 
        d.withdraw()

elif user_input == 2:
    while True:
        try:
            ID = int(input("Enter the ID: "))
            break 
        except ValueError:
            print("Opps! You need to enter a number!")
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    address = input("Enter address: ")
    phone_num = input("Enter phone number: ")
    while True:
        try:
            emp_id = int(input("Enter the emp_id of the employee that will help them: "))
            break 
        except ValueError:
            print("Opps! You need to enter a number!") 
    services_l = input("How many acccounts do you want to open: ")
    services = []
    for i in range(services_l):
        indicator = i 
        ask = input("what type of account will it ,{indicator}, be: ")
        services.append(ask)
    n = BankAccount() 
    n.new_client(ID, f_name, l_name, address, phone_num, services, emp_id)


elif user_input == 3:
    name = input("Enter name: ")
    position = input("Enter position: ")
    while True:
        try:
            years_active = int(input("Enter the years active: "))
            break
        except NameError:
            print("Opps! You need to enter a number!")
    while True:
        try:
            emp_id = int(input("Enter the ID: "))
            break 
        except ValueError:
            print("Opps! You need to enter a number!")
    t = BankAccount()
    t.new_emp(name, position, years_active, emp_id)



#t = BankAccount(50,1,"saving") 
#t.withdraw()
#d = BankAccount(100,1,"checking") 
#d.deposit()
#z = BankAccount()
#z.new_client(5, "Kim", "Kardashian", "509 table street", "555-342-2431", ["inventments"], 700)
#q = BankAccount() 
#q.new_emp("Rob", "client services", 10, 900)


