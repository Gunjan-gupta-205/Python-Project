# Install required libraries
from twilio.rest import Client
from datetime import datetime,timedelta
import  time,os
#Twilio credentials
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH")
client=Client(account_sid,auth_token)
#DESIGN MESSAGE SEND FUNCTION
def send_whatsapp_message(recipient_number,messaage_body):
    try:
        message=client.messages.create(
            from_='whatsapp:+14155238886',
            body=messaage_body,
            to=f'whatsapp:+918209143407'
        )
        print(f'Message sent successfully! Message SID{message.sid}')

    except Exception as e:
        print('An error occurred')    

# user inputs
name=input('Enter the recepient name= ')
recepient_number=input('Enter th recepient Whatsapp number with country code :')
message_body=input(F'Enter the message you want to send to {name} :')
# scheduling logic

date_str=input('enter the date to dend the message (YYYY-MM-DD):')
time_str=input('Enter the time to send the message in 24 hour format): ')

schedule_datetime = datetime.strptime(
    f"{date_str.strip()} {time_str.strip()}",
    "%Y-%m-%d %H:%M"
)
current_datetime=datetime.now()

time_difference=schedule_datetime-current_datetime
delay_seconds=time_difference.total_seconds()

if delay_seconds <=0:
    print('The specified time is in past.Please enter a future date and time :')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    time.sleep(delay_seconds)    
# send message
    send_whatsapp_message(recepient_number,message_body)