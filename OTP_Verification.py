#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# In[4]:


from twilio.rest import Client

def send_otp(phone_number):
    otp = random.randint(100000, 999999)
    message = 'Your one-time password is: {}'.format(otp)
    account_sid = 'ACbad72ea0aae6a89eab79a6b9aa2f9032'
    auth_token = 'e6595d51756e5c99776a4189c9dad98f'
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body=message,
            from_='your-twilio-phone-number',
            to=phone_number
        )
        print(message.sid)
    except Exception as e:
        print(str(e))
    return otp


# In[5]:


def verify_otp(user_otp, correct_otp):
    if user_otp == correct_otp:
        return True
    else:
        return False


# In[ ]:


if __name__ == "__main__":
    user_email = input("Enter your email: ")
    correct_otp = send_otp(user_email)
    user_otp = int(input("Enter the OTP you received: "))
    if verify_otp(user_otp, correct_otp):
        print("OTP verification successful!")
    else:
        print("OTP verification failed. Please try again.")

