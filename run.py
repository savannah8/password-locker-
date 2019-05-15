from cred import Credential

def create_acc(self,username,number,password):
    '''
    Function to create a new user
    '''
    new_user = Credential(username,number,password)
    return new_user
def save_creds(cred):
  '''
  Function to save credentials
  '''  
  cred.save_credential()

def del_cred(cred):
  '''
  function to delete credentials
  '''
  cred.delete_credential()
def find_user(username): 
  '''
  Function that finds user's credentials
  '''
  return Credential.credential_list

def main():
  print("Hello!Welcome to The password locker!")


    

  print("What is your name")

  user_name = input()

  print(f"Hello {user_name}.What would you like to do?")
  print('\n')

  while True:
    list =('''
    cc-create account
    dc - delete account 
    fc - find account 
    '''
    )
    print ("use these short codes to decide what to do:") 
    print (list)
    

    short_code = input().lower()
    
    if short_code == 'cc':
      print("New User:")

      print("Enter your name:")
      user =input()

      print("Enter your phone number:")
      num = input()

      print("create password:")
      pas = input()

      print ("confirm password:")
      password2 = input ()

      save_creds(create_acc(user,num,pas,password2)) 
      
      print("Thank you!you have successfully created an acc.")

    elif short_code == 'dc':
        
      del_cred(save_creds)

    elif short_code == 'fc':

      find_user(save_creds)   
main()   
