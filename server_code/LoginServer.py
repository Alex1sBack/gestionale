import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
@anvil.server.portable_class
def check_data(username, password):
  if(not app_tables.user_data.has_row(username)):
    return False
    
  givenPassword = app_tables.user_data.get(username)
  if(givenPassword != None & givenPassword == password):
    return True

  return False
  
