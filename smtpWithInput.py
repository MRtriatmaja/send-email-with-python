import smtplib
import getpass

from email.message import EmailMessage

print('''
Program Kirim Email menggunakan Python
Muhammad Rasyid Triatmaja (190010157)
''')

dari   = input("dari   : ")
tujuan = input("Kepada : ")
subjek = input("Subjek : ")
pesan  = input("Pesan  : ")
pwd    = getpass.getpass('Password anda: ')

#print(type(dari), tujuan, subjek, pesan, pwd)

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
    print(e)
finally:
    print("\nemail anda berhasil dikirim!")
    server.quit()
