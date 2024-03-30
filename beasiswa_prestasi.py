nama = str(input('Masukan Nama Anda : '))
asal_sekolah = str(input('Masukan Asal Sekolah Anda : '))
nama_prestasi = str(input('Masukan Kejuaraan atau Prestasi Yang Pernah Anda Dapatkan. Contoh "Juara satu indonesia idol " : '))
prestasi = str(input('Masukan Kategori Tingkat Prestasi Anda ( kabupaten / kota / provinsi / nasional / internasional ): '))
seleksi_prestasi = ['kota','Kota','KOTA','kabupaten','Kabupaten','KABUPATEN','provinsi','Provinsi','PROVINSI','nasional','Nasional','NASIONAL','internasional','Internasional','INTERNASIONAL']
if nama and asal_sekolah and nama_prestasi and prestasi in seleksi_prestasi:
    print(f'Selamat {nama} dari {asal_sekolah}. dengan prestasi {nama_prestasi}, tingkat {prestasi}.')
    if prestasi in ['kota','Kota','KOTA', 'kabupaten','Kabupaten','KABUPATEN']:
        print('--//-- Anda telah mendapatkan Beasiswa Gratis Biaya Pendaftaran + Potongan Total SPI 25% --//--')
    if prestasi in ['provinsi','Provinsi','PROVINSI']:
        print('--//-- Anda telah mendapatkan Beasiswa Gratis Biaya Pendaftaran + Potongan Total SPI 50% --//--')
    if prestasi in ['nasional','Nasional','NASIONAL','internasional','Internasional','INTERNASIONAL']:
        print('---//---Anda telah mendapatkan Beasiswa Gratis Biaya Pendaftaran + Potongan Total SPI 75%---//---')
else:
    print(f'Mohon Maaf {nama}, Anda Gagal Dalam Mendapatkan Beasiswa Prestasi. Tetap Semangat Dan Jangan Menyerah')