#!/usr/bin/python3
import time
import os
from models.Schedule import Create_Schedule
from datetime import datetime
from twilio.rest import Client
import schedule

current_date_time = datetime.now()
now = current_date_time.strftime("%Y-%m-%d")
class Reminder:
    def __init__(self):
        self.acct_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.auto_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.from_no = os.environ["TWILIO_WHATSAPP_NO"]
        self.to_no = os.environ["MY_NUMBER"]
        self.schedule = Create_Schedule()
        self.data = self.schedule.View("daily")
        self.reminder = None
        for k,v in self.data.items():
            if v['Date'] == now:
                self.date = datetime.strptime(self.data[k]["Date"], "%Y-%m-%d")
                self.reminder = datetime.strptime(self.data[k]["Reminder"],
                                                  "%H:%M:%S").time()
                self.message = f"the following tasks are due {k} {v}"
                self.my_time = datetime.combine(self.date, self.reminder)
                self.time_delta = self.my_time - datetime.now()	



    def Get_daily(self):
        """
            returns messsage displaying current daily task 
        """
        return self.messagels
        

    def Twilio(self):
        """
            establish a connection to the Twilio API 
        """
        try:
                    client = Client(self.acct_sid, self.auto_token)
                    text = self.message
                    session = client.messages.create(
                            body=text,
                            from_=self.from_no,
                            to=self.to_no,
                            )
                    return session
        except Exception as e:
            print('Failed', e)
            return e
    def send_Reminder(self):
        """
            having established a connection funtion sends a reminder using the
            twilio api to designated number.
        """
        try:
            if self.reminder:
                    clock = str(self.reminder)
                    schedule.every().day.at(clock).do(self.Twilio)
                    while True:
                        """ 
                            loops every 10 seconds to check if there are any
                            active reminder
                        """
                        schedule.run_pending()
                        time.sleep(10)
            else:
                    print(">>> no reminder set")
            print("**** Done! ****")
        except Exception as e:
            print("Failed to establish connection", e)
