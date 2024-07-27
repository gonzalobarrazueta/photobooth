import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageOps
from photobooth_dsl.utils.output_utils import get_image_folder
from photobooth_dsl.utils.display_images import compare_images


def apply_painting_filter(image):
    cv_image = np.array(image)
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)

    oil_painting = cv2.xphoto.oilPainting(cv_image, 7, 1)
    oil_painting = cv2.cvtColor(oil_painting, cv2.COLOR_BGR2RGB)

    return Image.fromarray(oil_painting)


def apply_comic_filter(image):
    cv_image = np.array(image)
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    color = cv2.bilateralFilter(cv_image, 9, 300, 300)

    comic = cv2.bitwise_and(color, color, mask=edges)

    comic = cv2.cvtColor(comic, cv2.COLOR_BGR2RGB)
    return Image.fromarray(comic)


def apply_filter(image_name, filter_name, output):

    original_image_path = get_image_folder("original", image_name)
    image = Image.open(original_image_path)

    if filter_name == "mono":
        filtered_image = ImageOps.grayscale(image)
    elif filter_name == "sepia":
        filtered_image = ImageOps.colorize(ImageOps.grayscale(image), "#704214", "#C0C0C0")
    elif filter_name == "blur":
        filtered_image = image.filter(ImageFilter.BLUR)
    elif filter_name == "sharpen":
        filtered_image = image.filter(ImageFilter.SHARPEN)
    elif filter_name == "painting":
        filtered_image = apply_painting_filter(image)
    elif filter_name == "comic":
        filtered_image = apply_comic_filter(image)
    else:
        raise ValueError(f"Filter '{filter_name}' not supported")

    filtered_image_path = get_image_folder("modified", f"filtered_image_{filter_name}.jpg" if output is None else output)
    filtered_image.save(filtered_image_path)

    compare_images("Original image", original_image_path, "Filtered image", filtered_image_path)

    # print each argument
    print(image_name, filter_name, output)