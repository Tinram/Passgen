
# Passgen


## Purpose

#### Create long and memorable passphrases.

For command-line and headless-server usage.


## Details

Create a long passphrase from Linux's dictionary file (or an alternative large word file).

Offers a strength-memorability compromise through:

- passphrase total character length
- CSPRNG word-picker
- lack of relationship between picked words
- word combination memorability.

This is despite the use of dictionary words, which by themselves, are extremely weak as passwords.

Uses Python's CSPRNG (Linux: */dev/urandom*, Windows: *CryptGenRandom*) to select words from the dictionary file. A CSPRNG is used to avoid word pick predictability.

Passphrase strength and resistance to Hashcat cracking patterns can be further increased by raising the number of words used and enabling character substitution (mangling certain letters into numbers).


## Requirements

Python 2.6+ or Python 3 and an installed dictionary (Linux) or a large word file in the same directory as the script (Windows).

(A zipped Linux dictionary (words.txt) is included in the /resources/ directory for Windows usage.)


## Tests

Tested on CentOS, Debian, and Windows 7.


## Usage

**Linux:**

`python passgen.py`

`python3 passgen.py`

`./passgen.py` (with file executable bit set)

(add to */usr/local/bin* or equivalent location for script availability)


**Windows:**

`passgen.py` (if .py is associated with Python interpreter)

`python passgen.py`


## Passphrase Strengthening

Adjust the variables:

`numwords = 6`

`numerifywords = True`

and uncomment / amend the extra character substitution lines:

`# words = [word.replace('a', '@') for word in words]`


## License

Passgen is released under the [GPL v.3](https://www.gnu.org/licenses/gpl-3.0.html).
