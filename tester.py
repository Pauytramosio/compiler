import tokenizer, tree
with open("test.sbs", "r") as file:
    text = file.read()
    tree.print_tree(tokenizer.tokenize(text))