import openai


class GetArticleWithGPT:

    def __init__(self, filename):
        self.file = filename

    # получает текст с аудио файла для обработки в ГПТ
    def generate_text_for_gpt(self) -> str:
        result = openai.Audio.transcribe(
            model='whisper-1',
            file=open(self.file, 'rb')
        )
        str = result['text'].replace('.', '')
        print(str)
        with open('file.txt', 'w') as f:
            f.write(str)
        return str

    def generate_gpt3_response(self, print_output=False):
        """
        Query OpenAI GPT-3 for the specific key and get back a response
        :type user_text: str the user's text to query for
        :type print_output: boolean whether or not to print the raw output JSON
        """
        user_text = self.generate_text_for_gpt()

        completions = openai.Completion.create(
            engine='text-davinci-003',  # Determines the quality, speed, and cost.
            temperature=0.5,  # Level of creativity in the response
            prompt=user_text,  # What the user typed in
            max_tokens=100,  # Maximum tokens in the prompt AND response
            n=1,  # The number of completions to generate
            stop=None,  # An optional setting to control response generation
        )

        # Displaying the output can be helpful if things go wrong
        if print_output:
            print(completions)

        # Return the first choice's text
        text = completions.choices[0].text.split('\n')[2:]
        # вызываем функцию, которая пронумеровывает полученный текст с абзацем
        # print(text)
        return text

    # собирает словарь {id: [text], ...}, выводит итоговый словарь с абзацами
    def enumerate(self, start: int = 0) -> dict[int:[list, int]]:
        sequence = self.generate_gpt3_response()
        dict_abzaz = {}
        n = start
        for elem in sequence:
            dict_abzaz[n] = [elem]
            n += 1

        return dict_abzaz
