
# Passgen

#### Create long and memorable passphrases.


## Example

```bash
    python passgen.py

    UnobstructedWhitehorseBarclayContaminants3696
```


## Background

As the outdated *NIST Special Publication 800-63* (2003) on passphrase recommendations (e.g. *P@55w0rd*) fades into obscurity, passphrase length helps to offer cracking resistance.


## Details

Create a long passphrase from Linux's dictionary file, or an alternative large word file.

Passgen offers a strength-memorability compromise through:

+ passphrase total character length
+ CSPRNG word-picker
+ lack of relationship between picked words
+ word combination memorability.

This is despite the use of dictionary words, which by themselves, are extremely weak as passwords.

Python's CSPRNG (Linux: */dev/urandom*, Windows: *CryptGenRandom*) is used to select words from the word file. A CSPRNG avoids word picking predictability.

Passphrase strength and resistance to Hashcat cracking patterns can be further increased by raising the number of words used and enabling some character substitution (mangling certain letters into numbers or other characters).


## Requirements

Python 2.6+ or Python 3 and an installed dictionary (Linux), or a large word file placed in the same directory as the script (Windows).

(A zipped Linux dictionary *words.txt* is included in the *resources/* directory for Windows usage.)


## Tests

Tested on CentOS, Debian, and Windows 7.


## Usage

**Linux**

```bash
    python passgen.py

    python3 passgen.py

    ./passgen.py
```

(Add to */usr/local/bin* or equivalent location for script availability.)


**Windows**

```batch
    passgen.py
```

... if *.py* is associated with Python interpreter, else:

```batch
    python passgen.py
```


## Passphrase Strengthening

Adjust the variables:

```python
    NUM_WORDS = 6

    MANGLE_LETTERS = True
```

and amend / add extra character substitution lines as required:

```python
    words = [word.replace('a', '@') for word in words]
```

## License

Passgen is released under the [GPL v.3](https://www.gnu.org/licenses/gpl-3.0.html).
