from moviepy.editor import VideoFileClip
import numpy as np
import os


def video_storyboard(video):
    video_clip = VideoFileClip(video.path)

    filename, _ = os.path.splitext(video.path)
    filename += "-moviepy"
    if not os.path.isdir(filename):
        os.mkdir(filename)

    saving_frames_per_second = min(video_clip.fps, 0.34)
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
    counter = 1
    for current_duration in np.arange(0, video_clip.duration, step):
        frame_filename = os.path.join(filename, f"{video.video_id}-frame{counter}.jpg")
        video_clip.save_frame(frame_filename, current_duration)
        counter += 1
    # скрины сохраняются в папку, где находится видео
    # название каждого новго скрина: {id видео}-frame{номер скрина, начиная с 1}.jpg
