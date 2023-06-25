import json

import requests
import openai

from model import arcticle_model


class GetSubtitles:
    openai.api_key = "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"

    def __init__(self, filename: list):
        self.filename = filename

    # получем субтитры из аудио файла
    def get_subtitles(self, subtitle_format='srt', **kwargs) -> list:
        result = []
        url = 'https://api.openai.com/v1/audio/transcriptions'
        headers = {
            'Authorization': f'Bearer {openai.api_key}',
        }
        data = {
            'model': 'whisper-1',
            'response_format': subtitle_format,
            'language': 'ru',
        }
        data.update(kwargs)
        for file in self.filename:
            files = {
                'file': (file, open(file, 'rb'))
            }
            response = requests.post(url, headers=headers, data=data, files=files)
            result.append(response.text.split('\n'))
        #print(result)
        return result

    # перебираем список и делим его на части  [[1, 'timestamp' ,'text'], [2, 'timestamp' ,'text']], ...
    def subtitle_division(self, lst: list, n: int = 4):
        result = []
        k = 0
        text = ''
        get_name_text_file = self.filename[0][:-5]
        for i in lst:
            for j in range(0, len(i) - 2, n):
                sub = i[j: n + j - 1]
                sub[1] = sub[1]
                text += sub[2]
                if len(sub) < n:
                    sub = sub + [None for y in range(n - len(sub) - 1)]
                result.append(sub)

        # сохраняет только текст субтитров для обработки на абзацы
        with open(f'{get_name_text_file}.txt', 'w') as f:
            f.write(text)
        #print(result)
        return result

    # из списка субтитров делаем словарь, где ключ - номер субтитра, значение - timestamp и text
    def convert_to_dict(self) -> dict:
        get_subtitles = self.get_subtitles()
        list_val = self.subtitle_division(get_subtitles)

        dct_json = {}
        j = 0
        for i, val in enumerate(list_val):
            dct_json[j] = val[1][:11], val[2]
            j += 1
        #print(dct_json)
        return dct_json
