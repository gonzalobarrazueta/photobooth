from moviepy.video.io.VideoFileClip import VideoFileClip
from photobooth_dsl.utils.video_utils import minutes_to_seconds, get_video_folder


def trim_video(video_name, start, end, output):

    start_seconds = minutes_to_seconds(start)
    end_seconds = minutes_to_seconds(end)

    try:
        with VideoFileClip(get_video_folder("original", video_name)) as video:
            trimmed_video = video.subclip(start_seconds, end_seconds)
            trimmed_video.write_videofile(
                get_video_folder("modified", output if output else "cropped_video.mov"),
                codec='libx264'
            )
    except Exception as e:
        print(f"An error occurred: {e}")
