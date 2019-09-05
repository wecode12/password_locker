class User:
	'''
	Class that generates new instance of a user
	'''
	user_list = []

	def __init__(self, login_name,email,password):
		'''
		this method ddefines properties for our user object
		'''
		self.login_name = login_name
		self.email = email
		self.password = password
	
	def save_user(self):
		'''
		saves user objects into user_list
		'''
		User.user_list.append(self)
	
	@classmethod
	def user_login(cls,email):
		'''
		Method that finds a user and logs them in
		'''
		for user in cls.user_list:
			if user.email == email:
				return user

	@classmethod
	def user_exist(cls,email):
		'''
		Method that checks if a user exists from the user list
		'''
		for user in cls.user_list:
			if user.email == email:
				return True

		return False

		