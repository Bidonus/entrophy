import codecs


alphabets = "абвгдежзийклмнопрстуфхцчшщыьэюя"


def vigenere(text, _key):

    text = text.lower()
    _key = key.lower()

    ciphertext = ""
    length = len(key)
    x = 0

    for char in text:
        if alphabets.find(char) != -1:
            final_index = (alphabets.find(char) + ord(key[x]) - 97) % 26
            ciphertext += alphabets[final_index]
            if x == length - 1:
                x = 0
            else:
                x = x + 1
        else:
            ciphertext += char

    return ciphertext


file_path = './vigenere_text.txt'
with codecs.open(file_path, 'r', encoding='utf8') as file:
    data = file.read()


if __name__ == '__main__':
    key = input('Enter key:\t')
    print(vigenere(data, key))
