import sys

def downcase_it(s):
    """
    Converts a given string to lowercase.
    """
    return s.lower()

if __name__ == "__main__":

    parameters = sys.argv[1:]

    if not parameters:
        print("none")
    else:
        for param in parameters:
            print(downcase_it(param))