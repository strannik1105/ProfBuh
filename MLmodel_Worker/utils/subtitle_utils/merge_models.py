import json
import os

import yt_dlp
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from model import arcticle_model
from subtitle_model import GetSubtitles


def download_video(video_url: str):
    # Создаем объект yt_dlp
    filename = video_url[video_url.rfind('=') + 1:]
    yt_opts = {

        'outtmpl': f'{filename}.mp4',

    }
    # Скачиваем видео
    try:
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.download([video_url])
        file = check_size_video(filename)
        return file

    except:
        return 'PIZDA'


def check_size_video(filename: str) -> list:
    list_video = []
    clip = VideoFileClip(filename + '.mp4')
    duration = clip.duration
    total = clip.duration
    if duration > 420:
        t1 = 0
        i = 420
        j = 1

        while duration > 0:
            if total < 420:
                print('yes')
                ffmpeg_extract_subclip(filename + '.mp4', t1, total, targetname=f"{filename}{j}.mp4")

            else:
                ffmpeg_extract_subclip(filename + '.mp4', t1, i, targetname=f"{filename}{j}.mp4")

            list_video.append(f"{filename}{j}.mp4")
            clip = VideoFileClip(f"{filename}{j}.mp4")
            duration1 = clip.duration
            duration -= duration1
            t1 = i
            i += 420
            j += 1
    else:
        list_video.append(f"{filename}.mp4")
    return list_video


# собирает json из субтитров с тайм кодами и текста с абзацами из гпт
def get_two_text(url: str):
    # скачивает видео по ссылке и передает название файла
    output_file = url[url.rfind('=') + 1:]
    downloader = download_video(url)

    # субтитры с тайм кодами
    dict_from_audio = GetSubtitles(downloader).convert_to_dict()
    while os.path.exists(f'{output_file}.txt') is False:
        f = False
    dict_from_model = arcticle_model(output_file)

    return add_timestamp_for_subscript(dict_from_model, dict_from_audio, output_file)


# собирает json из субтитров с тайм кодами и текста с абзацами из гпт
def add_timestamp_for_subscript(text1: dict[int: list],
                                text2: dict[int: list],
                                output_filename='endfile.json'
                                ) -> dict[int: list]:
    for k1 in text1:
        if text1[k1] == '':
            del text1[k1]

        for k2 in text2:
            if str(text2[k2][1]) in ''.join(text1[k1]):
                text1[k1].append(text2[k2][0])
                k2 += 1
                break

    # удаляем файл после обработок
    # os.remove(output_filename + '.mp4')

    return output_json(text1, output_filename)


# конечный json с абзацами
def output_json(text1: dict, filename: str) -> None:
    path = ''
    with open(f'{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(text1, f, ensure_ascii=False, indent=4)


get_two_text('https://www.youtube.com/watch?v=0K_eZGS5NsU')
