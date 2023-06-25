from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from config import MAIL_TOKEN, MAIL


class MailSender:
    def __create_connection(self):
        connection = smtplib.SMTP_SSL('smtp.mail.ru: 465')
        connection.login(MAIL, MAIL_TOKEN)
        return connection

    def send_message(self, user_mail, URL):
        server = self.__create_connection()
        msg = MIMEMultipart()
        msg['From'] = MAIL
        msg['To'] = user_mail
        msg['Subject'] = "Твоя статья готова!"
        message = f"Статья сформированна!\nСкачать ее можно по ссылке: {URL}"
        msg.attach(MIMEText(message, 'plain'))
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

