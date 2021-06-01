"""This functions appends a file"""


def append_write(filename="", text=""):
    """Append to a file"""
    with open(filename, 'a') as file:
        file.write(text)
    return len(text)
