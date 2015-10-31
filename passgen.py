#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Passgen
    Create long and memorable passphrases from Linux's dictionary file or a large word file.

    Passgen offers a strength-memorability compromise through: passphrase character length, CSPRNG word-picker, lack of relationship between picked words, and word combination memorability.
    Uses Python's CSPRNG (Linux: /dev/urandom, Windows: CryptGenRandom) to select words.
    Python 2 and 3 compatible, tested on Debian and CentOS Linux distros, and Windows.  (For Python3, replace existing shebang with: #!/usr/bin/python3)

    Author         Martin Latter <copysense.co.uk>
    Copyright      Martin Latter 23/10/2015
    Version        0.2
    License        GNU GPL version 3.0 (GPL v3); http://www.gnu.org/licenses/gpl.html
    Link           https://github.com/Tinram/Passgen.git
"""


import os, sys
from random import SystemRandom


# configuration
numwords = 4
numerifywords = False # character substitutions
numberlimit = 10000

benchmark = False


if benchmark:
    import time


def main():

    if os.access('/usr/share/dict/words', os.R_OK): # Debian
        file = '/usr/share/dict/words'
    elif os.access('/usr/share/dict/linux.words', os.R_OK): # CentOS
        file = '/usr/share/dict/linux.words'
    elif os.access('words.txt', os.R_OK): # cwd, Windows, user-placed file
        file = 'words.txt'
    else:
        sys.exit("Could not locate the system dictionary file - please manually edit the file location.")


    if benchmark:
        start = time.time()


    file = open(file, 'r')
    wordlist = file.readlines()
    file.close()


    cryptogen = SystemRandom()

    wordindexes = [cryptogen.randrange(len(wordlist)) for i in range(numwords)]

    words = [wordlist[index] for index in wordindexes]

    if numerifywords: # enact before capitalization
        words = [word.replace('o', '0') for word in words] # 'o' to zero: just one way of mangling letters
            # words = [word.replace('a', '@') for word in words]
            # words = [word.replace('s', '5') for word in words]

    words = [word.capitalize() for word in words]
    words = [word.rstrip() for word in words] # remove line breaks
    words = [word.replace("'s", '') for word in words] # remove apostrophe s

    rndnumber = cryptogen.randrange(numberlimit)

    print('' . join(words) + str(rndnumber))


    if benchmark:
        print('\ntime taken ' + str(time.time() - start) + ' sec')

    # end main()


if __name__ == '__main__':
    main()
