import requests
import openai


class GetSubtitles:
    openai.api_key = "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"

    def __init__(self, filename: str):
        self.file = filename

    # получем субтитры из аудио файла
    def get_subtitles(self, subtitle_format='srt', **kwargs) -> list:
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
        files = {
            'file': (self.file, open(self.file, 'rb'))
        }

        response = requests.post(url, headers=headers, data=data, files=files)
        return response.text.split('\n')

    # перебираем список и делим его на части  [[1, 'timestamp' ,'text'], [2, 'timestamp' ,'text']], ...
    def subtitle_division(self, lst: list, n: int = 4) -> list:
        result = []
        for x in range(0, len(lst) - 2,
                       n):  # делаем len(lst)-2, т.к. в файле с субтитрами вконце имеется две пустые строки
            sub = lst[x: n + x - 1]
            # timestamp сохраняет только значение start
            sub[1] = sub[1][:11]
            # text по timestamp, переводим список в строку

            if len(sub) < n:
                sub = sub + [None for y in range(n - len(sub) - 1)]
            result.append(sub)
        return result

    # из списка субтитров делаем словарь, где ключ - номер субтитра, значение - timestamp и text
    def convert_to_dict(self) -> dict:
        get_subtitles = self.get_subtitles()
        list_val = self.subtitle_division(get_subtitles)

        dct_json = {}
        for i, val in enumerate(list_val):
            dct_json[i] = val[1], val[2]
        print(dct_json)
        return dct_json


