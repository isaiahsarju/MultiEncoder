import sys
from optparse import OptionParser
import string
import base58
import base64
import bech32
import binascii

ENCODING = "ascii"

# This is where we add new encoding functions

def base16Data(string_data):
	string_data_bytes = string_data.encode(ENCODING)
	base16_bytes = base64.b16encode(string_data_bytes)
	base16_string_data = base16_bytes.decode(ENCODING)
	return base16_string_data

def base32Data(string_data):
	string_data_bytes = string_data.encode(ENCODING)
	base32_bytes = base64.b32encode(string_data_bytes)
	base32_string_data = base32_bytes.decode(ENCODING)
	return base32_string_data

def base36Data(string_data):
#	https://tomm.yt/posts/encode-base36-in-python/
	try:
		str_int = int(string_data)
	except ValueError as v:
		return "Not an int"
	alphabet = string.digits + string.ascii_lowercase
	out = []
	while str_int > 0:
	    str_int, r = divmod(str_int, 36)
	    out.append(alphabet[r])
	return(''.join(reversed(out)))

def base58Data(string_data):
	string_bytes = string_data.encode(ENCODING)
	base58_bytes = base58.b58encode(string_bytes)
	base58_string = base58_bytes.decode(ENCODING)
	return base58_string

def base64Data(string_data):
	string_data_bytes = string_data.encode(ENCODING)
	base64_bytes = base64.b64encode(string_data_bytes)
	base64_string_data = base64_bytes.decode(ENCODING)
	return base64_string_data

def base85Data(string_data):
	string_data_bytes = string_data.encode(ENCODING)
	base85_bytes = base64.b85encode(string_data_bytes)
	base85_string_data = base85_bytes.decode(ENCODING)
	return base85_string_data

def bech32Data(string_data):
	#hrp = "bc"
	#witver = 0
	#string_bytes = string_data.encode(ENCODING)
	#bech32_bytes = bech32.encode(string_bytes,0,hrp)
	#bech32_string = bech32_bytes.decode(ENCODING)
	return "Bech32 not yet implemented"

def decimalData(string_data):
	try:
		decimal_string_data = int(string_data)
	except ValueError as v:
		decimal_string_data = "Not an int" 
	return decimal_string_data

def hexData(string_data):
	string_bytes = string_data.encode(ENCODING)
	hex_bytes = binascii.hexlify(string_bytes)
	hex_string = hex_bytes.decode(ENCODING)
	return hex_string

def main():
	parser = OptionParser()
	parser.add_option("-s", "--string", dest="string_data", default="", help="String to encode")
	parser.add_option("-a", "--all", dest="all", action="store_true", default=False, help="Use all encoding")

	# This is where we add flags for new encodings

	parser.add_option("--base16", dest="base16", action="store_true", default=False, help="Encode Base16")
	parser.add_option("--base32", dest="base32", action="store_true", default=False, help="Encode Base32")
	parser.add_option("--base36", dest="base36", action="store_true", default=False, help="Encode Base36")
	parser.add_option("--base58", dest="base58", action='store_true', help="Encode Base58")
	parser.add_option("--base64", dest="base64", action="store_true", default=False, help="Encode Base64")
	parser.add_option("--base85", dest="base85", action="store_true", default=False, help="Encode Base85")
	parser.add_option("--bech32", dest="bech32", action='store_true', help="Encode Bech32")
	parser.add_option("--decimal", dest="decimal", action='store_true', help="Encode as Decimal")
	parser.add_option("--hex", dest="hex", action='store_true', help="Encode Hex")


	(options, args) = parser.parse_args()

	string_data = options.string_data
	all_encodings = options.all
	print("Original string_data:")
	print(f"{string_data}")
	print("")

	# This is where we do encoding if flag is set to true

	if options.base16 or all_encodings:
		encoded = base16Data(string_data)
		print("Base16:")
		print(f"{encoded}")
		print("")

	if options.base32 or all_encodings:
		encoded = base32Data(string_data)
		print("Base32:")
		print(f"{encoded}")
		print("")

	if options.base36 or all_encodings:
		encoded = base36Data(string_data)
		print("Base36:")
		print(f"{encoded}")
		print("")

	if options.base58 or all_encodings:
		encoded = base58Data(string_data)
		print("Base58:")
		print(f"{encoded}")
		print("")

	if options.base64 or all_encodings:
		encoded = base64Data(string_data)
		print("Base64:")
		print(f"{encoded}")
		print("")

	if options.base85 or all_encodings:
		encoded = base85Data(string_data)
		print("Base85:")
		print(f"{encoded}")
		print("")

	if options.bech32 or all_encodings:
		encoded = bech32Data(string_data)
		print("Bech32:")
		print(f"{encoded}")
		print("")

	if options.decimal or all_encodings:
		encoded = decimalData(string_data)
		print("Decimal:")
		print(f"{encoded}")
		print("")

	if options.hex or all_encodings:
		encoded = hexData(string_data)
		print("Hex:")
		print(f"{encoded}")
		print("")

if __name__ =="__main__":
	main()