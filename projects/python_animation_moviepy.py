import pywhatkit
import datetime
from datetime import timedelta

def send_whatsapp_message(phone_number, message):
    now = datetime.datetime.now()
    send_time = now + timedelta(minutes=1)
    
    try:
        pywhatkit.sendwhatmsg(phone_number, 
                             message,
                             send_time.hour,
                             send_time.minute)
        print("Message sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    phone_number = "+1234567890"  
    message = "Hello! This is a test message from Python bot."

    send_whatsapp_message(phone_number, message)