# Caesar Cipher - Encrypts/Decrypts words using uppercase and lowercase letters, numbers, and symbols.

import enchant

# The string to be encrypted/decrypted:
word = input('Enter word: ')

# Checking if the message is in the English dictionary.
d = enchant.Dict("en_US")
enDict = d.check(word)

# The encryption/decyption key:
key = 13

# Whether the program encrypts or decrypts:
if enDict:
	mode = 'encrypt'
else:
	mode = 'decrypt'

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`~!@#$%^&*_+-='

# Store the encrypted/decrypted form of the message:
translated = ''

translatedIndex = 0

for symbol in word:
	# Checking to see if the letter is in the given alphabet above (SYMBOLS).
	if symbol in SYMBOLS:
		symbolIndex = SYMBOLS.find(symbol)
		
		# Perform encryption/decryption:
		if mode == 'encrypt':
			translatedIndex = symbolIndex + key
		elif mode == 'decrypt':
			translatedIndex = symbolIndex - key
			
		# Handle wraparound, if needed:
		if translatedIndex >= len(SYMBOLS):
			translatedIndex = translatedIndex - len(SYMBOLS)
		elif translatedIndex < 0:
			translatedIndex = translatedIndex + len(SYMBOLS)
			
		translated = translated + SYMBOLS[translatedIndex]
	else:
		# Append the symbol without encrypting/decrypting:
		translated = translated + symbol
		
# Output the translated string:
print(mode.capitalize() + ': ' + translated)
