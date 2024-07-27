from lark import Lark, Transformer
from photobooth_dsl.commands.crop_image import crop
from photobooth_dsl.commands.add_filter import apply_filter
from photobooth_dsl.commands.crop_aspect import crop_aspect
from photobooth_dsl.commands.transform import transform_image
from photobooth_dsl.commands.trim_video import trim_video
from photobooth_dsl.commands.video_to_gif import video_to_gif
from photobooth_dsl.commands.adjust_speed import adjust_speed
from photobooth_dsl.utils.variables_util import is_variable
from photobooth_dsl.utils.output_utils import get_output


class PhotoboothTransformer(Transformer):

    def __init__(self):
        self.variables = {}

    def set_var(self, args):
        variable, value = args
        self.variables[variable] = value
        return self.variables

    def crop_image(self, args):
        image_path, width, height, output = args

        # Handle case where the image path is a variable
        if is_variable(image_path):
            image_path = self.variables[image_path]

        crop(image_path.strip("'"), int(width), int(height), get_output(output))
        return args

    def crop_aspect(self, args):
        image_path, smart, aspect_ratio, output = args

        # Handle case where the image path is a variable
        if is_variable(image_path):
            image_path = self.variables[image_path]

        crop_aspect(image_path.strip("'"), True if smart else False, aspect_ratio, get_output(output))

        return args

    def transform_image(self, args):
        image_path, shape, custom_shape, triangle_type, output = args

        # Handle case where the image path is a variable
        if is_variable(image_path):
            image_path = self.variables[image_path]

        transform_image(image_path.strip("'"), shape, custom_shape, triangle_type, get_output(output))

    def add_filter(self, args):
        filter_name, image_path, output = args

        # Handle case where the image path is a variable
        if is_variable(image_path):
            image_path = self.variables[image_path]

        apply_filter(image_path.strip("'"), filter_name, get_output(output))

    def trim_video(self, args):
        video_path, start, end, output = args

        # Handle case where the video path is a variable
        if is_variable(video_path):
            video_path = self.variables[video_path]

        trim_video(video_path.strip("'"), start, end, get_output(output))

    def video_to_gif(self, args):
        video_path, start, end, output = args

        # Handle case where the video path is a variable
        if is_variable(video_path):
            video_path = self.variables[video_path]

        video_to_gif(video_path.strip("'"), get_output(output), start, end)

    def adjust_speed(self, args):
        video_path, speed, output = args
        print(video_path, speed, output)

        # Handle case where the video path is a variable
        if is_variable(video_path):
            video_path = self.variables[video_path]

        adjust_speed(video_path.strip("'"), speed, get_output(output))


class PhotoboothInterpreter:
    def __init__(self):
        # Read grammar definition from parser.lark
        with open("photobooth_dsl/parser.lark", "r") as grammar_file:
            grammar = grammar_file.read()

        self.parser = Lark(grammar, start="start", parser="lalr", transformer=PhotoboothTransformer())
        self.transformer = PhotoboothTransformer()

    def execute(self, command):
        tree = self.parser.parse(command)
        return self.transformer.transform(tree)
