
import string
import random
class Account:
	'''
	Class that generates new instances of accounts/credentials
	'''

	account_list = []

	def __init__(self,account_name,email,user_name,number,password):
		'''
		__init__ method that helps us define properties for our objects.
		'''

		self.account_name = account_name
		self.email = email
		self.user_name = user_name
		self.number = number
		self.password =password

	def save_account(self):
		'''
		save-account method saves account objects into account_list
		'''
		Account.account_list.append(self)
	def delete_account(self):
		'''
		delete_account method deletes account
		'''
		Account.account_list.remove(self)


	@classmethod
	def find_by_email(cls, email):
		'''
    	Method that takes in an account number and returns credentials that match that number
    	'''
		for account in cls.account_list:
			if account.email == email:
				return account

	@classmethod
	def display_account(cls):
		'''
		method that returns the account list
		'''
		return cls.account_list

	@classmethod
	def account_exist(cls,email):
		'''
		Method that checks if an account exists from the account list.
		
		'''
		for account in cls.account_list:
			if account.email == email:
				return True

		return False

	@classmethod
	def generate_password(cls,pass_length):
		'''
		class to generate passowrds
		'''
		allchar = string.ascii_letters + string.punctuation + string.digits
		password = ''.join(random.sample(allchar, int(pass_length)))
		return password