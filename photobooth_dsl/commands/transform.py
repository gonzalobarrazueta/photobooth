import numpy as np
from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET
from svgpath2mpl import parse_path
from photobooth_dsl.utils.output_utils import get_image_folder, get_shape


def transform_image(image_name, shape, custom_shape, triangle_type, output):

    image = Image.open(get_image_folder('original', image_name)).convert("RGBA") # Ensure the image has an alpha channel
    width, height = image.size

    # Load and parse the SVG path
    svg_shape = get_shape(shape)
    path = parse_svg(svg_shape)

    # Calculate scaling and translation to fit the SVG path to the image size
    vertices = np.array(path.vertices)
    min_x, min_y = vertices.min(axis=0)
    max_x, max_y = vertices.max(axis=0)

    svg_width = max_x - min_x
    svg_height = max_y - min_y

    scale_x = width / svg_width
    scale_y = height / svg_height
    scale = min(scale_x, scale_y)

    # Scale and translate the vertices
    vertices = (vertices - [min_x, min_y]) * scale
    vertices += [(width - svg_width * scale) / 2, (height - svg_height * scale) / 2]

    # Create a mask using the scaled vertices
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon([tuple(vertex) for vertex in vertices], outline=1, fill=1)

    # Apply the mask to the image
    image_np = np.array(image)
    mask_np = np.array(mask)

    # Create an alpha channel with the mask
    alpha_channel = np.where(mask_np == 1, 255, 0).astype(np.uint8)

    # Create a new image with RGBA channels
    result_np = np.dstack((image_np[:, :, :3], alpha_channel))

    # Convert the result back to an image
    result_image = Image.fromarray(result_np, "RGBA")

    # Save image
    result_image.save(get_image_folder("modified", output))
    result_image.show()


def parse_svg(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()

    namespaces = {"svg": "http://www.w3.org/2000/svg"}

    path = root.find(".//svg:path", namespaces)

    if path is None:
        raise ValueError("No path found in SVG file")
    else:
        return parse_path(path.get('d'))
