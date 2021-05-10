from translate import Translator
# Configuring the translation
lang = Translator(from_lang="english", to_lang="pt-br")

# Translate any simple text given
text = "Hello, my name is Victor and I like programming!"
translated = lang.translate(text)
# Prints translation
print(translated)