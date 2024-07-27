from moviepy.video.io.VideoFileClip import VideoFileClip
from photobooth_dsl.utils.video_utils import get_video_folder, minutes_to_seconds


def video_to_gif(video_name, output, start=None, end=None):
    try:
        with VideoFileClip(get_video_folder("original", video_name)) as video:
            if start and end:
                video = video.subclip(minutes_to_seconds(start), minutes_to_seconds(end))
            video.write_gif(get_video_folder("modified", output if output else "video.gif"), fps=15)
    except Exception as e:
        print(f"An error occurred: {e}")
