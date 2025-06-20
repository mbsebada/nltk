"""Simple tokenization demo for NLTK."""

import nltk


def main():
    text = "The quick brown fox jumps over the lazy dog."
    tokens = nltk.word_tokenize(text)
    print("Tokens:", tokens)


if __name__ == "__main__":
    main()
