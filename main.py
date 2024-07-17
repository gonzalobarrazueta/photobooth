import argparse
from photobooth_dsl.interpreter import PhotoboothInterpreter


def main():
    command_line = argparse.ArgumentParser(description="Photobooth DSL")
    command_line.add_argument("command", type=str, help="DSL command to run")
    args = command_line.parse_args()

    interpreter = PhotoboothInterpreter()

    try:
        result = interpreter.execute(args.command)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
