from lark import Lark, Transformer
from photobooth_dsl.commands.crop_image import crop
from photobooth_dsl.commands.crop_aspect import crop_aspect
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

        crop(image_path.strip("'"), int(width), int(height), None if output is None else output.strip("'"))
        return args

    def crop_aspect(self, args):
        image_path, smart, aspect_ratio, output = args

        # Handle case where the image path is a variable
        if is_variable(image_path):
            image_path = self.variables[image_path]

        crop_aspect(image_path.strip("'"), True if smart else False, aspect_ratio, get_output(output))

        return args


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
