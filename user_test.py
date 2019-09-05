import unittest
from user import User

class TestUser(unittest.TestCase):
	'''
    Test class  that defines test cases for our accounts class behaviours.
	Args:
        unittest.TestCase: Testcase class that helps in creating test cases
    '''
	def setUp(self):
		'''
		set up method to clear before each test case.
		'''

		self.new_user = User("Peter Polle","peter.m.polle@gmail.com", "12345")

	def tearDown(self):
		'''
		Method that does clean up after each test case has run
		'''
		User.user_list = []

	def test_account_init(self):
		'''
		Test case to test if the object is initializzed properly
		'''
		self.assertEqual(self.new_user.login_name, "Peter Polle")
		self.assertEqual(self.new_user.email,"peter.m.polle@gmail.com")
		self.assertEqual(self.new_user.password, "12345")
	def test_save_user(self):
		'''
		Test case to test that the user object is saved into the user_list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.user_list),1)

	def test_save_multiple_users(self):
		'''
		test case to see if multiple users can be saved into user_list
		'''
		self.new_user.save_user()
		User("Gerald Mzungu","gmzungu@gmail.com","12345").save_user()
		self.assertEqual(len(User.user_list),2)
	def test_user_login(self):
		'''
		Test case to test user login
		'''
		self.new_user.save_user()
		test_user = User("Thor Odinson","thor@asgard.com","12345")
		test_user.save_user()

		find_user = User.user_login("thor@asgard.com")
		self.assertEqual(find_user.email,test_user.email)
	def test_user_exists(self):
		'''
		Test case to acertain that a user exists
		'''
		self.new_user.save_user()
		test_user = User("martin Luther King","martin@luther.king","12345").save_user()
		user_exists = User.user_exist("martin@luther.king")
		self.assertTrue(user_exists)

if __name__ == '__main__':
    unittest.main()