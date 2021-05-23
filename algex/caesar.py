alphabet = 'abcdefghijklmnopqrstuvwxyz'
def caesarCipherEncryptor(string, key):
	d = {c: i for i, c in enumerate(alphabet)}
	result = [''] * len(string)
	for i, c in enumerate(string):
		result[i] = alphabet[(d[c] + key) % len(alphabet)]
	return ''.join(result)