#!/usr/bin/env python3.6
from account import Account
from user import User


def create_user_account(name,email,password):
	'''
	Function to create a new user
	'''
	new_user = User(name,email,password)

	return new_user

def save_user(user):
	'''
	Function to save User
	'''
	user.save_user()

def user_login(email):
	'''
	Function to login users
	'''
	return User.user_login(email)

def create_account(account_name,email,user_name,number,password):
	'''
	Function to create a new account
	'''
	new_account = Account(account_name,email,user_name,number,password)
	return new_account
def save_account(account):
	'''
	Function to create new account
	'''
	account.save_account()
def delete_account(account):
	'''
	Function to delete an acount
	'''
	account.delete_account()

def find_account(email):
	'''
	Function that finds an account using th ephone number and returns the account
	'''
	return Account.find_by_email(email)

def check_if_account_exists(email):
	'''
	Function that checks if an account exists
	'''
	return Account.account_exist(email)
def check_if_user_exists(email):
	'''
	Function that checks if a user exists
	'''
	return User.user_exist(email)
def display_accounts():
	'''
	Function that returns all saved contacts
	'''
	return Account.display_account()

def generate_password(pass_length):
	'''
	Function that generates a password
	'''
	return Account.generate_password(pass_length)

def main():
    print("Welcome to password locker")
    while True:
        print('''
              ca - create account
              lg - login
              esc - Escape''')
        short_code = input().lower()
        print("_" * 20)
        if short_code == "ca":
            print('''Create Acount
Enter your full name
                     ''')
            print("_" * 20)
            name = input()
            
            
            print("Enter Your Email")
            email = input()
            print("_" * 20)
            print("Enter Your Password")
            password = input()
            save_user(create_user_account(name, email,password))
            print("_" * 20)
            print("_" * 20)
            print(f"""Your user details - Username : {name} Email : {email} Password : {password}""")
            print("_" * 20)
            print("_" * 20)

            print("")
            print(f"Hi {name} What would you like to do?")
            print("")

            while True:
                print("Use these short codes: cac - create new account, dac - display account, fac - find an account, exit - exit accounts list")
                short_code = input().lower()

                if short_code == 'cac':
                        print("Creating a New Account")
                        print("-"*10)

                        print('')

                        print("Account name ...")
                        account_name = input()

                        print('')

                        print("User name ...")
                        user_name = input()

                        print('')

                        print("Email address ...")
                        email = input()

                        print('')

                        print("Phone Number ...")
                        number = input()

                        print('')

                        print("How long would you like your password to be")
                        pass_length = int(input())
                        password = generate_password(pass_length)

                        save_account(create_account(account_name,email, user_name,number,password))
                        print('')

                        print("Your New account details including your auto generated password are shown below")
                        print('')

                        print(f"New account details : Account: {account_name},Email:{email}, User name : {user_name},Phone Number: {number}, Password: {password}",)
                        print('')
                elif short_code == 'dac':
                        if display_accounts():
                            print("Below is a list of all your accounts")
                            print("-"*20)

                            print('')
                            for Accounts in display_accounts():
                                print(f"Account : {Accounts.account_name}, User name : {Accounts.user_name} E-mail address : {Accounts.email} Password : {Accounts.password}")

                                print('')
                        else:
                            print('')
                            print("You seem to not have any saved accounts yet. Save an account using the cc code")
                            print('')
                elif short_code == 'fac':
                        print("Enter the email of the account you want to find")
                        email = input()
                        if check_if_account_exists(email):
                                searched_account = find_account(email)
                                print("-"*20)
                                print("-"*20)

                                print('')
                                print(f"{searched_account.user_name} {searched_account.email}")
                                

                                print('')

                                print(f"Account ... {searched_account.account_name}")
                                print(f"Password ... {searched_account.password}")
                                print('')

                                print("-"*20)
                                print("-"*20)

                        else:
                                print('')
                                print("No account with that email exists")
                                print('')
                             
                elif short_code == "exit":
                        print('')
                        print("Goodbye ...")
                        break
                else:
                    print("Please input a valid short code")

        elif short_code == "lg":
            print("Log in")
            print("Enter your email")
            print("_" * 20)
            email = input()
            print("Enter Your Password")
            password = input()
            if check_if_user_exists(email):
            	authenticate_user = user_login(email)
            	if authenticate_user.email == email and authenticate_user.password == password:
		            print("")
		            print(f"Hi {authenticate_user.login_name} What would you like to do?")
		            print("")

		            while True:
		                print("Use these short codes: cac - create new account, dac - display account, fac - find an account, exit - exit accounts list")
		                short_code = input().lower()

		                if short_code == 'cac':
		                        print("Creating a New Account")
		                        print("-"*10)

		                        print('')

		                        print("Account name ...")
		                        account_name = input()

		                        print('')

		                        print("User name ...")
		                        user_name = input()

		                        print('')

		                        print("Email address ...")
		                        email = input()

		                        print('')

		                        print("Phone Number ...")
		                        number = input()

		                        print('')

		                        print("How long would you like your password to be")
		                        pass_length = int(input())
		                        password = generate_password(pass_length)

		                        save_account(create_account(account_name,email, user_name,number,password))
		                        print('')

		                        print("Your New account details including your auto generated password are shown below")
		                        print('')

		                        print(f"New account details : Account: {account_name},Email:{email}, User name : {user_name},Phone Number: {number}, Password: {password}",)
		                        print('')
		                elif short_code == 'dac':
		                        if display_accounts():
		                            print("Below is a list of all your accounts")
		                            print("-"*20)

		                            print('')
		                            for Accounts in display_accounts():
		                                print(f"Account : {Accounts.account_name}, User name : {Accounts.user_name} E-mail address : {Accounts.email} Password : {Accounts.password}")

		                                print('')
		                        else:
		                            print('')
		                            print("You seem to not have any saved accounts yet. Save an account using the cc code")
		                            print('')
		                elif short_code == 'fac':
		                        print("Enter the email of the account you want to find")
		                        email = input()
		                        if check_if_account_exists(email):
		                                searched_account = find_account(email)
		                                print("-"*20)
		                                print("-"*20)

		                                print('')
		                                print(f"{searched_account.user_name} {searched_account.email}")
		                                

		                                print('')

		                                print(f"Account ... {searched_account.account_name}")
		                                print(f"Password ... {searched_account.password}")
		                                print('')

		                                print("-"*20)
		                                print("-"*20)

		                        else:
		                                print('')
		                                print("No account with that email exists")
		                                print('')
		                             
		                elif short_code == "exit":
		                        print('')
		                        print("Goodbye ...")
		                        break
		                else:
		                    print("Please input a valid short code")

            	else:
            		print("The user and password combination does not work. Please try again")
            else:
            	print("A user with the email does not exist. Please register to start using the application")
                             

        elif short_code == "esc":
            print('')
            print("Exiting")
            break
        else:
            print("I'm sorry, the short code does not seem to exist")


if __name__ == '__main__':
    main()
