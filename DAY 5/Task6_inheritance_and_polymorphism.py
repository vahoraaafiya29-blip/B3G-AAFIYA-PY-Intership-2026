class Notification:
     def send(self):
           print("Sending Notification")

class EmailNotification(Notification):
    def send(self):
        print("Email Sent Successfully")

class SMSNotification(Notification):
     def send(self):
          print("SMS sent Successfully")

notifications=[
    Notification(),
    EmailNotification(),
    SMSNotification()
]                     
for notification in notifications:
     notification.send()