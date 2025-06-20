"""Part-of-speech tagging example using NLTK."""

import nltk


def main():
    sentence = "The quick brown fox jumps over the lazy dog."
    tokens = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)
    print("POS tags:", tags)


if __name__ == "__main__":
    main()
