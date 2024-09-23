import nltk

nltk.download('punkt_tab')

import string



def pemisah_kata(kalimat):
    # Tokenisasi kata
    kata = nltk.word_tokenize(kalimat)
    
    # Menghilangkan tanda baca
    kata_bersih = [word for word in kata if word.isalnum()] 
    
    # Menghitung jumlah kata
    jumlah_kata = len(kata_bersih)
    
    return kata_bersih, jumlah_kata

# Contoh kalimat
kalimat = "Universitas Pelita Bangsa, yang terletak di Cikarang, Bekasi, adalah salah satu universitas swasta yang terus berkembang pesat di Indonesia! Kampus ini menawarkan berbagai program studi, mulai dari Teknik Informatika, Manajemen, hingga Ilmu Hukum, yang semuanya dirancang untuk membekali mahasiswa dengan keterampilan yang relevan di dunia kerja. Dengan lokasi strategis di kawasan industri (apakah ini bukan keuntungan besar?), Universitas Pelita Bangsa memiliki banyak keunggulan, termasuk akses mudah ke berbagai perusahaan besar untuk keperluan magang dan kerja sama industri! Visi kampus ini adalah mencetak lulusan yang berdaya saing tinggi melalui pengajaran yang berkualitas dan fasilitas modern (wow!), yang didukung oleh dosen-dosen berpengalaman."

kata_bersih, jumlah_kata = pemisah_kata(kalimat)

print("Kata-kata yang dipisahkan:", kata_bersih)
print("Jumlah kata:", jumlah_kata)
