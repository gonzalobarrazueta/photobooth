import re


def minutes_to_seconds(time_segment):

    result = re.match(r'(\d+):(\d+)', time_segment)

    if result is None:
        raise ValueError("Invalid time format. Please use 'MM:SS' format.")
    else:
        minutes, seconds = result.groups()
        return int(minutes) * 60 + int(seconds)


def get_video_folder(folder, value):
    if folder == "original":
        return "photobooth_dsl/videos/original/" + value
    elif folder == "modified":
        return "photobooth_dsl/videos/modified/" + value
    else:
        raise ValueError("Invalid folder type specified. Choose 'original' or 'modified'.")
