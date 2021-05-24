# MultiEncoder
**MultiEncoder** is a multiple encoder. It encodes multiple in multiple formats so you can quickly deduce what encoding you're working wit.

## Install
Build the container:

`docker build -t multiencoder .`

Then run it: 

`docker run -it multiencoder /bin/bash`

For testing I find it easier to mount directory so I can use host's text editor instead of the container's text editor.

`docker run -v [host path to MultiEncoder]:/root/MultiEncoder/ -it multiencoder /bin/bash`


Within container run:
```
pip3 install virtualenv
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 ./multiencoder.py -h
```
Example:
```
python3 ./multiencoder.py -h
Usage: multiencoder.py [options]

Options:
  -h, --help            show this help message and exit
  -s STRING_DATA, --string=STRING_DATA
                        String to encode
  -a, --all             Use all encoding
  --base16              Encode Base16
  --base32              Encode Base32
  --base36              Encode Base36
  --base58              Encode Base58
  --base64              Encode Base64
  --base85              Encode Base85
  --bech32              Encode Bech32
  --decimal             Encode as Decimal
  --hex                 Encode Hex
  ```
  ```
python3 ./multiencoder.py -s "Hello World" --all
Original string_data:
Hello World

Base16:
48656C6C6F20576F726C64

Base32:
JBSWY3DPEBLW64TMMQ======

Base36:
Not an int

Base58:
JxF12TrwUP45BMd

Base64:
SGVsbG8gV29ybGQ=

Base85:
NM&qnZy;B1a%^M

Bech32:
Bech32 not yet implemented

Decimal:
Not an int

Hex:
48656c6c6f20576f726c64


python3 ./multiencoder.py -s "Hello World" --base64
Original string_data:
Hello World

Base64:
SGVsbG8gV29ybGQ=
```
## Contribute
If you wish to add a new encoding the form is in three parts
### Part 1
The function e.g,:
```
def hexData(string_data):
	string_bytes = string_data.encode(ENCODING)
	hex_bytes = binascii.hexlify(string_bytes)
	hex_string = hex_bytes.decode(ENCODING)
	return hex_string
```
### Part 2 the CLI switch e.g.,:
```
parser.add_option("--hex", dest="hex", action='store_true', help="Encode Hex")
```
### Part 3 the `if` statement for checking the switch e.g.,:
```
if options.hex or all_encodings:
	encoded = hexData(string_data)
	print("Hex:")
	print(f"{encoded}")
	print("")
```