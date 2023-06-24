import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import VK_TOKEN

vk_bot = vk_api.VkApi(token=VK_TOKEN)
session_bot = vk_bot.get_api()
longpoll = VkBotLongPoll(vk_bot, 214053144)


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        peer = event.object.from_id
        user_id = event.object.message["from_id"]