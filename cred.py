class Credential :
  '''
  Class that has the user's credentials
  '''
  credential_list =[]

  def __init__(self,username,number,password):
    
    self.username =username
    self.phone_number = number
    self.password = password
    
  def save_credential(self):
      '''
      save_credential method saves contact objects into credential_list
      '''
      Credential.credential_list.append(self)


  def delete_credential(self):
    '''
    delete_credential method deletes a saved contact from the contact_list 
    '''

    Credential.credential_list.remove(self)

  
  @classmethod
  def find_by_username(cls,username):
    '''
    method that takes in number and returns a contact 
    that matches that number 
    Args:
      username:username to search for
    Returns :
      Credentials of that matches the username.
    '''
    for credential in cls.credential_list:
      if credential.username == username:
        return credential
