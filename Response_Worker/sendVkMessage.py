import vk_api
from config import VK_TOKEN
from urllib.parse import urlparse


class VkSender:
    def __init__(self):
        self.vk_bot = vk_api.VkApi(token=VK_TOKEN)
        self.bot = self.vk_bot.get_api()

    def send_message(self, user_id):
        user_id = self.check_url(user_id)
        user_full_id = self.bot.users.get(user_ids=user_id)[0]['id']
        self.bot.messages.send(peer_id=user_full_id, random_id=0, message="Спасибо, что используете наш сервис!\n"
                               "Как будет готова статья, мы отправим вам ссылку!")


    def send_article(self, user_id, URL):
        user_id = self.check_url(user_id)
        user_full_id = self.bot.users.get(user_ids=user_id)[0]['id']
        self.bot.messages.send(peer_id=user_full_id, random_id=0, message="Статья готова!\n"
                                                                          f"Ссылка на статью: {URL}")

    def check_url(self, id):
        user_path = urlparse(id)
        if user_path.scheme == '':
            return user_path.path
        else:
            return user_path.path.split("/")[1]

