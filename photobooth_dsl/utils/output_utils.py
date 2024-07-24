import re


def check_format(file_name):
    file_format_pattern = r'[a-zA-Z0-9-_.:\/]+\.([a-zA-Z0-9]+)'
    regex = re.compile(file_format_pattern)

    if regex.match(file_name):
        return True
    else:
        return False


# The value argument is an image path or a variable
def get_image_folder(folder, value):
    if folder == "original":
        return "photobooth_dsl/images/original/" + value
    elif folder == "modified":
        return "photobooth_dsl/images/modified/" + value
    else:
        raise ValueError("Invalid folder type specified. Choose 'original' or 'modified'.")


def get_shape(shape):
    return "photobooth_dsl/images/svg_shapes/" + shape + ".svg"

def get_output(output):
    if output is None:
        return None
    else:
        return output.strip("'")
