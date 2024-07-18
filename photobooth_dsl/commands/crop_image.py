import cv2
from photobooth_dsl.utils.output_utils import get_image_folder


def crop(image_name, w, h, output):

    image = cv2.imread(get_image_folder("original", image_name))
    x = 0
    y = 0
    cropped_image = image[x:x + h, y:y + w]

    cv2.imwrite(get_image_folder("modified", "cropped_image.jpg" if output is None else output), cropped_image)

    cv2.imshow('original', image)
    cv2.imshow('cropped', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
