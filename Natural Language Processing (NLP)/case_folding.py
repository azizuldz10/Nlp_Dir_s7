import PyPDF2
import re
import string

def baca_pdf(nama_file):
    teks_pdf = ""
    with open(nama_file, "rb") as file:
        pembaca_pdf = PyPDF2.PdfReader(file)
        jumlah_halaman = len(pembaca_pdf.pages)
        
        # Membaca setiap halaman
        for halaman in range(jumlah_halaman):
            halaman_pdf = pembaca_pdf.pages[halaman]
            teks_pdf += halaman_pdf.extract_text()
    
    return teks_pdf

def case_folding(teks):
    return teks.lower()

# Fungsi untuk menghapus angka dari teks
def hapus_angka(teks):
    return re.sub(r'\d+', '', teks)

# Fungsi untuk menghapus tanda baca dari teks
def hapus_tanda(teks):
    return teks.translate(str.maketrans('', '', string.punctuation))

# Fungsi untuk menyimpan teks ke file .txt
def simpan_teks(nama_file, teks):
    with open(nama_file, "w") as file:
        file.write(teks)

# Fungsi utama
def tugas_case_folding_pdf(pdf_file, txt_file_output):
    # Langkah 1: Membaca file PDF
    teks_pdf = baca_pdf(pdf_file)

    # Langkah 2: Melakukan case folding
    teks_case_folding = case_folding(teks_pdf)

    # Langkah 3: Menghapus angka
    teks_tanpa_angka = hapus_angka(teks_case_folding)

    # Langkah 4: Menghapus tanda baca
    teks_bersih = hapus_tanda(teks_tanpa_angka)

    # Langkah 5: Menyimpan hasil ke file teks
    simpan_teks(txt_file_output, teks_bersih)
    
    print(f"Hasil case folding, tanpa angka dan tanpa tanda baca disimpan di {txt_file_output}")

# Contoh penggunaan
pdf_file = "jarkom.pdf"  # Nama file PDF
txt_file_output = "hasil_casefolding_jarkom_pypdf2_bersih.txt"  # Nama file output

tugas_case_folding_pdf(pdf_file, txt_file_output)
