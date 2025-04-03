import tokenizer
with open("test.sbs", "r") as file:
    text = file.read()

for textt in tokenizer.tokenize(text):
    print(textt)