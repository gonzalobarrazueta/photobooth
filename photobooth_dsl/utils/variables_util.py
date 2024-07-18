# Handles cases where the value passed is a variable
def is_variable(value):

    # If the value is enclosed in quotes, it is a string and not a variable
    if value.startswith("'") and value.endswith("'"):
        return False
    else:
        return True
