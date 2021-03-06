import smtplib
import getpass

from email.message import EmailMessage

print('''
Program Kirim Email menggunakan Python
''')

dari   = input("From   : ")
tujuan = input("To     : ")
subjek = input("Subject: ")
pesan  = input("Pesan  : ")
pwd    = getpass.getpass('\nPassword anda: ')


msg = EmailMessage()
msg['Subject'] = subjek
msg.set_content(pesan)
msg['From'] = dari
msg['To'] = tujuan

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(dari, pwd)
    server.send_message(msg)
except Exception as e:
    print("\nError : Tidak bisa mengirim pesan\n\n",e)
finally:
    server.quit()