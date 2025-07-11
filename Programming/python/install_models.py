import spacy.cli
import stanza

def main():
    print("✅ Installing spaCy model: el_core_news_sm")
    spacy.cli.download("el_core_news_sm")

    stanza.download("el")

if __name__ == "__main__":
    main()