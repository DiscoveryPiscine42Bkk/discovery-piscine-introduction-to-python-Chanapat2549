import sys

def main():
    parameters = sys.argv[1:]
    num_parameters = len(parameters)

    if num_parameters != 1:
        print("none$")
        return

    input_string = parameters[0]
    
    z_count = input_string.count('z')
    if z_count == 0:
        print("none$")
    else:
        print("z" * z_count + "$")

if __name__ == "__main__":
    main()