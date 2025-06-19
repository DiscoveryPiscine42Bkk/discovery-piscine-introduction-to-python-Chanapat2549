import sys

def shrink(s):
  
    print(s[:8])

def enlarge(s):
 
    if len(s) < 8:
        s += 'Z' * (8 - len(s))
    print(s)

def main():
    if len(sys.argv) < 2:
        print('none')
        return

    for i, arg in enumerate(sys.argv[1:]):
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else: # Exactly eight characters
            print(arg)
            if i < len(sys.argv) - 2:
                print()

if __name__ == "__main__":
    main()