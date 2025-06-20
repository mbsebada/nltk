"""Look up synonyms for a word using NLTK's WordNet interface."""

from nltk.corpus import wordnet


def main():
    syns = wordnet.synsets("dog")
    lemmas = {lemma.name() for syn in syns for lemma in syn.lemmas()}
    print("Synonyms:", sorted(lemmas))


if __name__ == "__main__":
    main()
