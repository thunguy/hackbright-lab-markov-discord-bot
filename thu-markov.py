"""Generate Markov text from text files."""

from random import choice
import sys



def open_and_read_file(filenames):

    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # text = ""
    # for filename in filenames:
    #     text += open(filename).read()
    #     open(filename).close()

    # return text

    return " ".join([open(filename).read() for filename in filenames])
    
# print(open_and_read_file(sys.argv[1]))
# print(type(open_and_read_file(sys.argv[1])))



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    words = text_string.split()

    # append None to the end of our word list to set stopping point
    words.append(None)

    for i, word in enumerate(words[:-2]):

        k = (words[i], words[i + 1])
        v = words[i + 2]

        chains[k] = chains.get(k,[]) + [v]
        
        # if key not in chains:
        #     chains[k] = []

        # chains[k].append(v)

    return chains

# print(make_chains(open_and_read_file(sys.argv[1])))



def print_chains(chains):
    for k, v in chains.items():
        print(f"{k}: {v}")

print(print_chains(make_chains(open_and_read_file(sys.argv[1:]))))



def make_text(chains):
    """Return text from chains."""

    # choose a random key from {chains}
    k = choice(list(chains.keys()))
    # store in variable 'words' the randomly chosen key from line above
    words = [k[0], k[1]]
    # choose ONE random value of chains[k] & store in variable "word"
    word = choice(chains[k])

    while word is not None:
        k = (k[1], word)
        words.append(word)
        word = choice(chains[k])

    return " ".join(words) 


print(make_text(make_chains(open_and_read_file(sys.argv[1:]))))

# input_path = sys.argv[1]

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)