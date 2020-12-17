# Caesar Cipher - Encrypts/Decrypts phrases using English dictionary. Numbers and symbols will result in a decryption since it's not a english word.

import enchant

# The string to be encrypted/decrypted:
message = input('Enter message: ').upper()

# Checking if the message is in the English Dictionary to encrypt/decrypt.
for word in message.split():
	d = enchant.Dict("en_US")
	enDict = d.check(word)
	# Whether the program encrypts or decrypts:
	if enDict:
		mode = 'encrypt'
	else:
		mode = 'decrypt'

# The encryption/decyption key:
key = 2

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Store the encrypted/decrypted form of the message:
translated = ''

translatedIndex = 0

for symbol in message:
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
