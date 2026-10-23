
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

print("#English Stop Words")
print(stopwords.words('english'))

print("\n#Greek Stop Words")
print(stopwords.words('greek'))
