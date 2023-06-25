from moviepy.video.io.VideoFileClip import VideoFileClip

from ProfBuh.MLmodel_Worker.utils.video_utils.video_model import Video


def video_slicer(vid: Video, begin: int, end: int):
    slicer = VideoFileClip(vid.path)
    slicer = slicer.subclip(begin, end)
    file_name = str(vid.video_id) + "-sliced.mp4"
    slicer.write_videofile(file_name)
