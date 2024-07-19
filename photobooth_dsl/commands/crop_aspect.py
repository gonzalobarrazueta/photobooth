import os
import cv2
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from photobooth_dsl.utils.aspect_ratio_map import aspect_ratio_mapping
from photobooth_dsl.utils.output_utils import get_image_folder
from photobooth_dsl.commands.crop_image import crop

load_dotenv()


def crop_aspect(image_name, smart, aspect_ratio, output):

    try:
        endpoint = os.environ["VISION_ENDPOINT"]
        key = os.environ["VISION_KEY"]

    except KeyError:
        print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
        exit()

    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    # if the smart option is used in the command, then use Azure Vision API
    if smart is True:
        with open(get_image_folder("original", image_name), "rb") as f:
            image_data = f.read()

        modified_image = client.analyze(
            image_data=image_data,
            visual_features=[VisualFeatures.SMART_CROPS],
            smart_crops_aspect_ratios=[aspect_ratio_mapping(aspect_ratio)]
        )

        if modified_image is not None:
            smart_crop_values = modified_image.smart_crops.list[0]["boundingBox"]
            print(smart_crop_values)

        crop(image_name, smart_crop_values['w'], smart_crop_values['h'], output,
             smart_crop_values['x'], smart_crop_values['y'])
    else:
        auto_aspect_ratio(image_name, aspect_ratio, output)


def auto_aspect_ratio(image_name, aspect_ratio, output):

    image = cv2.imread(get_image_folder("original", image_name))
    h, w, _ = image.shape

    aspect_ratio = aspect_ratio_mapping(aspect_ratio)

    if w / h > aspect_ratio:
        new_h = h
        new_w = int(h * aspect_ratio)
    else:
        new_w = w
        new_h = int(w * pow(aspect_ratio, -1))

    # Calculate crop coordinates
    x_center, y_center = w // 2, h // 2
    x1 = max(0, x_center - new_w // 2)
    y1 = max(0, y_center - new_h // 2)
    x2 = x1 + new_w
    y2 = y1 + new_h

    # Crop the image
    cropped_image = image[y1:y2, x1:x2]

    # Save the cropped image
    cv2.imwrite(get_image_folder("modified", "ar_image.jpg" if output is None else output), cropped_image)

    cv2.imshow('original', image)
    cv2.imshow('cropped', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
