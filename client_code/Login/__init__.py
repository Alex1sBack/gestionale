from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import m3.components as m3

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_button_click(self, **event_args):
    var = anvil.server.call('check_data', self.username_text.text, self.password_text.text)
    if(var):
      self.response_text.text = "Login effettuato con successo"   
      self.response_text.text_color = "Green"
    else:
      self.response_text.text = "Username o password non corretti"
      self.response_text.text_color = "Red"
