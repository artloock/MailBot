#!/usr/bin/env python
# coding: utf-8

# In[2]:


import smtplib
import getpass

def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        # Connect to the SMTP server of your email provider
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Log in to your email account
        server.login(sender_email, sender_password)

        # Create the email message
        email_message = f"Subject: {subject}\n\n{message}"

        # Send the email
        server.sendmail(sender_email, receiver_email, email_message)
        print("Email sent successfully!")

    except Exception as e:
        print("An error occurred while sending the email.")
        print(e)

    finally:
        # Disconnect from the SMTP server
        server.quit()

# Get sender email and password securely
sender_email = input("Enter your email: ")
sender_password = getpass.getpass("Enter your password: ")

# Get receiver email
receiver_email = input("Enter the supplier's email: ")

# Set the email subject and message
subject = "Email test"
message = "Hello Word"

# Send the email
send_email(sender_email, sender_password, receiver_email, subject, message)


# In[ ]:




