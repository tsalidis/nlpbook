
num_of_documents = 100
num_of_words = 0

print(f"Number of documents: {num_of_documents}")

try:
  words_per_document = num_of_documents / num_of_words
except ZeroDivisionError:
  print("No words in documents!")
else:
  print(f"Average words per document: {words_per_document}")
