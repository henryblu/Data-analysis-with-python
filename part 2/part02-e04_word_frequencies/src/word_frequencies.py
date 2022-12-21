#!/usr/bin/env python3

# the function word_frequencies gets a filename as a parameter and returns a dict with the word frequencies. All punctuation is removed. In the output, there should be a word and its count per line separated by a tab:

def word_frequencies(filename):
    with open(filename, 'r') as f:
        ret = {}
        for line in f:
            for word in line.split():
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word in ret:
                    ret[word] += 1
                else:
                    ret[word] = 1
    return ret
def main():
    print(word_frequencies("alice.txt"))

if __name__ == "__main__":
    main()
