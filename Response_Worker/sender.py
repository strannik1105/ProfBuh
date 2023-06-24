from sendMail import MailSender
from sendVkMessage import VkSender


class Sender:
    def send_message(self, params):
        if params[0] == 'vk':
            sender = VkSender()
            sender.send_article(params[1],params[2])
        else:
            sender = MailSender()
            sender.send_message(params[1],params[2])

        print("Message sent to user")