from moviepy.editor import *
from photobooth_dsl.utils.video_utils import get_video_folder, minutes_to_seconds


def adjust_speed(video_name, speed, output):

    video = VideoFileClip(get_video_folder("original", video_name))
    video_sped_up = video.fx(vfx.speedx, float(speed))

    video_sped_up.write_videofile(
        get_video_folder("modified", output if output else "video_sped_up.mp4"),
        codec="libx264"
    )
