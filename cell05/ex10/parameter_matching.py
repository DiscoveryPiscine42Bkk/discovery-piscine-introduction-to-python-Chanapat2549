import sys

def main():
    num_args = len(sys.argv) - 1  # Subtract 1 for the script name itself

    if num_args == 1:
        parameter = sys.argv[1]
        user_input = input("What was the parameter? ")
        if user_input == parameter:
            print("Good job!")
        else:
            print("Nope, sorry...")
    else:
        print("none")

if __name__ == "__main__":
    main()