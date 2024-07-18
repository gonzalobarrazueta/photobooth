def aspect_ratio_mapping(aspect_ratio):
    aspect_ratio_map = {
        "3:4": 0.75,
        "1:1": 1.00,
        "3:2": 1.50,
        "16:9": 1.78,
        "4:3": 1.33
    }

    if aspect_ratio in aspect_ratio_map:
        return aspect_ratio_map[aspect_ratio]
    else:
        raise ValueError(f"Unsupported aspect ratio: {aspect_ratio}")
