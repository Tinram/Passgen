#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Passgen
    Create long and memorable passphrases from Linux's dictionary file or a large word file.

    Passgen offers a strength-memorability compromise through: passphrase character length, CSPRNG word-picker, lack of relationship between picked words, and word combination memorability.
    Uses Python's CSPRNG (Linux: /dev/urandom, Windows: CryptGenRandom) to select words.
    Python 2 and 3 compatible, tested on Debian and CentOS Linux distros, and Windows.  (For Python3, replace existing shebang with: #!/usr/bin/env python3)

    Author         Martin Latter <copysense.co.uk>
    Copyright      Martin Latter 23/10/2015
    Version        0.21
    License        GNU GPL version 3.0 (GPL v3); http://www.gnu.org/licenses/gpl.html
    Link           https://github.com/Tinram/Passgen.git
"""


import os
import sys
import time
from random import SystemRandom


# configuration
NUM_WORDS = 4
NUMBER_LIMIT = 10000
MANGLE_LETTERS = False # character substitutions
BENCHMARK = False


def main():

    """ Locate words file and process. """

    if os.access('/usr/share/dict/words', os.R_OK): # Debian
        words_file = '/usr/share/dict/words'
    elif os.access('/usr/share/dict/linux.words', os.R_OK): # CentOS
        words_file = '/usr/share/dict/linux.words'
    elif os.access('words.txt', os.R_OK): # current dir, Windows, user-placed file
        words_file = 'words.txt'
    else:
        sys.exit("Could not locate the system dictionary file - please manually edit the file location.")


    if BENCHMARK:
        start_time = time.time()


    wfile = open(words_file, 'r')
    word_list = wfile.readlines()
    wfile.close()


    cryptogen = SystemRandom()

    wordindexes = [cryptogen.randrange(len(word_list)) for i in range(NUM_WORDS)]

    words = [word_list[index] for index in wordindexes]

    if MANGLE_LETTERS: # enact before capitalization
        words = [word.replace('o', '0') for word in words]
        words = [word.replace('a', '@') for word in words]
        # words = [word.replace('s', '5') for word in words]

    words = [word.capitalize() for word in words]
    words = [word.rstrip() for word in words] # remove line breaks
    words = [word.replace("'s", '') for word in words] # remove apostrophe s

    rnd_number = cryptogen.randrange(NUMBER_LIMIT)

    print('' . join(words) + str(rnd_number))


    if BENCHMARK:
        print('\ntime taken: %s secs ' % str.format('{0:.5f}', (time.time() - start_time)))

    # end main()


if __name__ == '__main__':
    main()
