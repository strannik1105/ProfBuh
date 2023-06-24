from moviepy.video.io.VideoFileClip import VideoFileClip


def video_slicer(vid, begin, end):
    slicer = VideoFileClip(vid.path)
    slicer = slicer.subclip(begin, end)
    file_name = str(vid.video_id) + "-sliced.mp4"
    slicer.write_videofile(file_name)
