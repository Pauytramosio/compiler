def print_tree(data, indent=0):
    INDENT = 4
    for item in data:
        if isinstance(item, list):
            print_tree(item, indent + INDENT)
        else:
            print(' ' * indent + str(item))