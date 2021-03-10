from telethon.sync import TelegramClient 
from telethon import TelegramClient
import constants
   
# creating a telegram session and assigning it to a variable client 
client = TelegramClient('session', constants.API_ID, constants.API_HASH) 
# connecting and building the session 
client.connect() 
  
# in case of script ran first time it will 
# ask either to input token or otp sent to 
# number or sent or your telegram id  
if not client.is_user_authorized():
    client.send_code_request(constants.PHONE) 
    # signing in the client 
    client.sign_in(constants.PHONE, input('Enter the code: '))    
try: 
    user = constants.PHONE
    receiver = client.get_input_entity(user)
  
    message = "latest_close sdf" # sending message using telegram client 
    client.send_message(receiver, message) 
except Exception as e: 
    print(e); 
  
client.disconnect() 