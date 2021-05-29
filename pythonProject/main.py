import os

text = input("Введите какойто текст: ")

if len(text) == 1:

   print("В тексте", '"' + text + '"', len(text), "символ")

elif len(text) == 2 or len(text) == 3 or len(text) == 4:

   print("В тексте", '"' + text + '"', len(text), "символа")

else:

   print("В тексте", '"' + text + '"', len(text), "символов")
