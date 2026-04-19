import streamlit as st
from twilio.rest import Client
from datetime import datetime
import time
import os
# Twilio credentials (better: env variables use karo)
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH")
client = Client(account_sid, auth_token)
# Function to send message
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        return f"✅ Message Sent! SID: {message.sid}"
    except Exception as e:
        return f"❌ Error: {e}"

# UI
st.title("📲 WhatsApp Message Scheduler")

name = st.text_input("Enter Recipient Name")
recipient_number = st.text_input("Enter WhatsApp Number (with country code)")

message_body = st.text_area(f"Enter message for {name}")

date_input = st.date_input("Select Date")
time_input = st.time_input("Select Time")

# Button
if st.button("Schedule Message"):
    if not recipient_number or not message_body:
        st.error("⚠️ Please fill all fields")
    else:
        schedule_datetime = datetime.combine(date_input, time_input)
        current_datetime = datetime.now()

        delay_seconds = (schedule_datetime - current_datetime).total_seconds()

        if delay_seconds <= 0:
            st.error("❌ Time is in the past!")
        else:
            st.success(f"📅 Message scheduled for {schedule_datetime}")

            # Wait (not ideal but works for demo)
            time.sleep(delay_seconds)

            result = send_whatsapp_message(recipient_number, message_body)
            st.write(result)