import unittest
from account import Account

class TestAccount(unittest.TestCase):
    '''
    Test class  that defines test cases for our accounts class behaviours.
    Args:
        unittest.TestCase: Testcase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to before each test case.
        '''

        self.new_account = Account("facebook", "peter.m.polle@gmail.com", "ppolle", "0725603607","12345")

    def tearDown(self):
        '''
        Method that does clean up after each test case has run
        '''
        Account.account_list = []

    def test_account_init(self):
        '''
        test case to test if the object is initializzed properly
        '''
        self.assertEqual(self.new_account.account_name, "facebook")
        self.assertEqual(self.new_account.email, "peter.m.polle@gmail.com")
        self.assertEqual(self.new_account.user_name, "ppolle")
        self.assertEqual(self.new_account.number, "0725603607")
        self.assertEqual(self.new_account.password, "12345")

    def test_save_account(self):
    	'''
    	test_save_account test case to test if the account object is saved into
         the account list
    	'''
    	self.new_account.save_account() # saving the new account
    	self.assertEqual(len(Account.account_list),1)

    def test_save_multiple_accounts(self):
    	'''
    	test_save_multiple_accounts to check if we can save multiple accounts
            objects to our account_list
    	'''
    	
    	self.new_account.save_account()
    	Account("github","peter.m.polle@gmail.com","MrPolle","0725603607","45678").save_account()
    	self.assertEqual(len(Account.account_list),2)
    def test_delete_account(self):
    	'''
    	test_delete_account to test if an account can be deleted from the account_list
    	'''
    	self.new_account.save_account()
    	Account("twitter","peter.m.polle@gmail.com","MrPolle","0725603607","458675").save_account()
    	self.new_account.delete_account()
    	self.assertEqual(len(Account.account_list),1)
    def test_find_account_by_email(self):
    	'''
    	test_find_account_by_number to test if an account can be found by number and details displayed
    	'''
    	self.new_account.save_account()
    	test_account = Account("twitter","peter.m.polle@gmail.com","MrPolle","0725603607","344545")
    	test_account.save_account()
    	found_account = Account.find_by_email("peter.m.polle@gmail.com")
    	self.assertEqual(found_account.email,test_account.email)
    	  
    def test_display_all_accounts(self):
    	'''
    	method that returns all contacts saved
    	'''
    	self.assertEqual(Account.display_account(),Account.account_list)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_account.save_account()
        test_account = Account("Test","test@user.com","DonJohn","0711223344","233535") # new contact
        test_account.save_account()

        account_exists = Account.account_exist("test@user.com")

        self.assertTrue(account_exists)

if __name__ == '__main__':
    unittest.main()n