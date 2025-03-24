import tokenizer, tree
with open("test.xom", "r") as file:
    text = file.read()

for textt in tokenizer.tokenize(text):
    print(textt)
    print(" KREO ")