"""Este script crea un diccionario que ordena las palabras según la letra por la que comienzan. En este caso hay que llamar a la función y darle como argumento nuestra lista de palabras"""
'''
def append_words_by_leter (list_of_words):
    by_letter = {}
    words = list_of_words
    for word in words:
        letter = word[0]
        if letter not in by_letter:
            by_letter[letter] = [word]
        else:
            by_letter[letter].append(word)

append_words_by_leter(list_of_words = list)
print(by_letter)
'''