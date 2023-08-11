def print_arguments(*args):
    num_args = len(args)
    print("Number of arguments:", num_args)
    
    if num_args > 0:
        print("List of arguments:")
        for index, arg in enumerate(args):
            print("Argument {}:".format(index + 1), arg)

if __name__ == "__main__":
    print_arguments(1, "hello", [1, 2, 3], {"name": "James"})
