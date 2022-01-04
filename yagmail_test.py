import yagmail
import csv

# yagmail.register('strooizout.python@gmail.com', 'PythonBot2021')

yag = yagmail.SMTP("strooizout.python@gmail.com")

title = 'Test'
body = '''
Lieve lieve lieve {name},

Ik ben de robot assistent van Martijn. Ik heb je email op de mailing lijst gezet. Veel plezier met alle spam! :)

<3 PythonBot
'''


with open("contacts.csv") as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for name, receiver_email in reader:
        yag.send(to=receiver_email, 
                subject=title, 
                contents=body.format(name=name),
                 attachments=['strooizout.csv', 'screenshot.png']
        )