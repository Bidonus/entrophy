import codecs


alphabets = "абвгдежзийклмнопрстуфхцчшщыьэюя"


def decode(ciphertext, _key):
	ciphertext = ciphertext.lower()
	_key = _key.lower()
	plaintext = ""
	length = len(_key)
	x = 0
	for i in ciphertext:
		if alphabets.find(i) != -1:
			if (alphabets.find(i) - ord(_key[x]) + 97) > 0:
				final_index = (alphabets.find(i) - ord(_key[x]) + 97)
			else:
				final_index = (alphabets.find(i) - ord(_key[x]) + 97 + 26) % 26
			plaintext += alphabets[final_index]
			if x == length - 1:
				x = 0
			else:
				x = x + 1
		else:
			plaintext += i
	return plaintext


file_path = './vigenere_text.txt'

with codecs.open(file_path, 'r', encoding='utf8') as file:
	data = file.read()

if __name__ == '__main__':
	key = input('Enter key:\t')
	print(decode(data, key))
