from lark import Lark, Transformer
from photobooth_dsl.commands.crop_image import crop


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
        if not image_path.startswith('"') and not image_path.endswith('"'):
            image_path = self.variables[image_path]

        crop(image_path, int(width), int(height), output)
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
