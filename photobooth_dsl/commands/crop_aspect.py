import os
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
        return
