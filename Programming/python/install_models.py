import spacy.cli
import stanza
import nltk

def main():
    print("✅ Installing spaCy model: el_core_news_sm")
    spacy.cli.download("el_core_news_sm")
    spacy.cli.download("en_core_web_sm")

    stanza.download("el")
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('punkt')

if __name__ == "__main__":
    main()