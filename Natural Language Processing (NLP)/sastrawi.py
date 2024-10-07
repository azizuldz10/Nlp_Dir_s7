import string
import PyPDF2
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize

# Fungsi untuk membaca file PDF
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Fungsi untuk menghapus stopwords menggunakan Sastrawi saja
def remove_stopwords_sastrawi(text):
    # Buat stopword remover dari Sastrawi
    factory = StopWordRemoverFactory()
    stopword_remover = factory.create_stop_word_remover()
    stopwords_list = factory.get_stop_words()  # Mendapatkan daftar stopwords
    
    # Tokenisasi sebelum proses
    tokens = word_tokenize(text)
    
    # Kata-kata yang dihapus (stopwords)
    removed_words = [word for word in tokens if word.lower() in stopwords_list]
    
    # Hapus stopwords dari teks
    text_without_stopwords = stopword_remover.remove(text)
    
    # Hapus tanda baca dari teks yang sudah di-filter
    text_without_punctuation = text_without_stopwords.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenisasi ulang setelah menghapus tanda baca
    final_tokens = word_tokenize(text_without_punctuation)
    
    return final_tokens, removed_words

# Fungsi untuk menyimpan hasil ke file .txt
def save_to_txt(filtered_tokens, file_path):
    with open(file_path, 'w') as file:
        file.write(' '.join(filtered_tokens))

# Path ke file PDF
pdf_input_path = 'komentar.pdf'  # Ganti dengan path ke file PDF Anda
txt_output_path = 'komentar_filtered_sastrawi.txt'

# Baca komentar dari PDF
comments = read_pdf(pdf_input_path)

# Tokenisasi dan filtering menggunakan Sastrawi
filtered_comments, removed_words = remove_stopwords_sastrawi(comments)

# Simpan hasil ke file .txt
save_to_txt(filtered_comments, txt_output_path)

# Tampilkan hasil kata yang dihapus dalam bentuk list di terminal
print("Kata-kata stopwords yang dihapus:")
print(removed_words)

# Tampilkan pesan bahwa hasil sudah disimpan
print(f"Hasil filtering telah disimpan di {txt_output_path}")
