import string
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize
import nltk

factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
kalimat = "Cuaca hari ini sangat cerah dan menyenangkan untuk berolahraga."
kalimat = kalimat.translate(str.maketrans('', '', string.punctuation)).lower()

stop = stopword.remove(kalimat)
tokens = nltk.tokenize.word_tokenize(stop)
print(tokens)

for token in tokens:
    print(f"Token: {token}, Type: {type(token)}")