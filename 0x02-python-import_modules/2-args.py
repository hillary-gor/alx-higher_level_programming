#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    # Count the number of arguments passed (excluding the script name itself)
    count = len(sys.argv) - 1

    # Check the count of arguments and print the appropriate message
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Iterate over the arguments and print them with their respective positions
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
