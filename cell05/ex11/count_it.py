import sys

def main():
    # sys.argv is a list of command line arguments.
    # sys.argv[0] is the script name itself.
    # So, the actual parameters start from sys.argv[1].
    parameters = sys.argv[1:]
    num_parameters = len(parameters)

    if num_parameters == 0:
        print("none$")
    else:
        print(f"parameters: {num_parameters}$")
        for param in parameters:
            print(f"{param}: {len(param)}$")

if __name__ == "__main__":
    main()