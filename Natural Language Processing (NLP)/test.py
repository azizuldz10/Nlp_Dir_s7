import nltk
nltk.download('stopwords')
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

kalimat = "Cuaca hari ini sangat cerah dan menyenangkan untuk berolahraga."
kalimat = kalimat.translate(str.maketrans('', '', string.punctuation)).lower()

tokens = word_tokenize(kalimat)
listStopword = set(stopwords.words('indonesian'))

removed = []
for t in tokens:
    if t not in listStopword:
        removed.append(t)

print(removed)
