import re


def check_format(file_name):
    file_format_pattern = r'[a-zA-Z0-9-_.:\/]+\.([a-zA-Z0-9]+)'
    regex = re.compile(file_format_pattern)

    if regex.match(file_name):
        return True
    else:
        return False


# The value argument is an image path or a variable
def get_images_folder(value, folder):
    if folder == "original":
        return "photobooth_dsl/images/original/" + value
    elif folder == "modified":
        return "photobooth_dsl/images/modified_images/" + value
    else:
        raise ValueError("Invalid folder type specified. Choose 'original' or 'modified'.")
