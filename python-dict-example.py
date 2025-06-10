## This program translates a few English words into Persian using a simple dictionary.
dictionary = {
    "apple": "سیب",
    "book": "کتاب",
    "car": "ماشین"
}
word = input("یک کلمه انگلیسی وارد کن: ")

if word in dictionary:
    print("ترجمه:", dictionary[word])
else:
    print("این کلمه در دیکشنری نیست.")

