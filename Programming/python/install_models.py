import spacy.cli

def main():
    print("✅ Installing spaCy model: el_core_news_sm")
    spacy.cli.download("el_core_news_sm")

if __name__ == "__main__":
    main()