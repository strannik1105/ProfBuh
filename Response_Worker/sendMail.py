from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from config import TOKEN, MAIL


class MailSender:
    def __create_connection(self):
        connection = smtplib.SMTP_SSL('smtp.mail.ru: 465')
        connection.login(MAIL, TOKEN)
        return connection

    def send_message(self, mailTo, link):
        server = self.__create_connection()
        msg = MIMEMultipart()
        msg['From'] = MAIL
        msg['To'] = mailTo
        msg['Subject'] = "Твоя статья готова!"
        message = f"Статья сформированна!\nСкачать ее можно по ссылке: {link}"
        msg.attach(MIMEText(message, 'plain'))
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        return True
