import unittest 
from cred import Credential

class TestUser(unittest.TestCase):
  '''
  Test class that defines tes cases for the Credential class behaviours.
  Args:
      unittest.TestCase: TestCase class that helps in creating test cases 
  '''

  def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_cred = Credential("Willen","0700261031//...","willeng",)

  def tearDown(self):
     '''
     tearDown method that does clean up after each case has run.
     '''
     Credential.credential_list = []

  def test_init(self):
      '''
      test_init test case to test if the object is initialized properly 
      '''

      self.assertEqual(self.new_cred.username,"Willen")
      self.assertEqual(self.new_cred.phone_number,"0700261031")
      self.assertEqual(self.new_cred.password,"willeng")
      


  def test_save_credential(self):
        '''
        test_save_credentials test case to test if the credential
        object is saved into the credential list 
        '''
        self.new_cred.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
  
  def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we we can save 
        multiple contact
        objects to our credential_list
        '''
        self.new_cred.save_credential()
        test_credential= Credential("Willen","0700261031","willeng")

        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

  def delete_credential(self):
    '''
    delete_credential method deletes a saved contact from the contact_list 
    '''

    Credential.credential_list.remove(self)
  def test_find_credential_by_username(self):
    '''
    test to check if we can find a contact by username and 
    display information
    '''
    self.new_cred.save_credential()
    test_credential =Credential("Willen","0700261031","willeng")
    test_credential.save_credential()

    found_credential = Credential.find_by_username("Willen")

    self.assertEqual(found_credential.password,test_credential.password)
if __name__ == '__main__':
       unittest.main()
