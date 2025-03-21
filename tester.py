import tokenizer, translator
tokenized = tokenizer.tokenize("exit 31;")
translated = translator.translate(tokenized)
built = translator.build(translated[0], translated[1])
print(built)