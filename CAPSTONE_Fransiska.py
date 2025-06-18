
#Menampilkan Menu Utama
menu_instruction = """
========== Daftar Nilai Siswa Job Connector Data Science Purwadhika BSD ==========

Daftar Menu:
1. Report Nilai Siswa.
2. Cari dan Tampilkan Data Nilai Siswa Tertentu.
3. Menambah Daftar Nilai Siswa.
4. Menghapus Data Nilai Siswa.
5. Mengubah Data Nilai Siswa.
6. Mengurutkan Data Siswa.
7. Exit program.
"""

#Data awal siswa dalam bentuk list
nama_siswa = ['Adinda Permatasari', 'Elsa Perpetua', 'Doh Kyungsoo', 'Hanjun Kim', 'Mark Lee', 'Haechan Sihombing', 'Johnny Suh', 'Siska Tho', 'Baekhyun', 'Doyoung']
nilai_modul1 = [90, 80, 80, 100, 50, 65, 80, 90, 70, 80]
nilai_modul2 = [90, 80, 80, 90, 90, 70, 70, 80, 75, 75]
nilai_modul3 = [85, 70, 85, 95, 100, 75, 75, 85, 80, 80]
nis = ['JCDS01', 'JCDS02', 'JCDS03', 'JCDS04', 'JCDS05', 'JCDS06', 'JCDS07', 'JCDS08', 'JCDS09', 'JCDS10']

#List kosong untuk nilai rata-rata dan keterangan kelulusan
avg_nilai, keterangan = [], []

#Fungsi untuk menampilkan/mencetak header tabel
def data_header():
    print("\nReport Nilai Siswa Job Connector Data Science Purwadhika BSD :")
    print("\nNo.\t| NIS\t\t| Nama Siswa\t\t| Ujian Modul 1\t| Ujian Modul 2\t| Ujian Modul 3\t| Nilai Rata-Rata\t| Keterangan ")
    print("-" * 150)

#Fungsi untuk menampilkan/mencetak satu baris data siswa
def data_row(no, nis_, name, m1, m2, m3, avg, desc):
    print("{}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}".format(
        str(no).ljust(5),
        nis_.ljust(10), 
        name.ljust(20),
        str(m1).ljust(12), 
        str(m2).ljust(12),
        str(m3).ljust(12), 
        str(avg).ljust(15), 
        desc.ljust(12)))
    
#Fungsi untuk menampilkan seluruh daftar nilai siswa
def daftar_nilai():
    data_header()
    for i, data in enumerate(zip(nis, nama_siswa, nilai_modul1, nilai_modul2, nilai_modul3, avg_nilai, keterangan), 1):
        data_row(i, *data)

#Fungsi untuk memperbarui nilai rata-rata dan keterangan kelulusan
def update_nilai():
    avg_nilai.clear()
    keterangan.clear()
    for a, b, c in zip(nilai_modul1, nilai_modul2, nilai_modul3):
        avg = round((a + b + c) / 3, 2)
        avg_nilai.append(avg)
        keterangan.append("Lulus" if avg >= 80 else "Tidak Lulus")

#Fungsi untuk input nilai ujian, dengan validasi angka dan rentang (0-100)
def input_nilai(modul_ke):
    while True:
        nilai_input = input(f"Masukkan Hasil Ujian Modul {modul_ke} (0-100): ")
        if nilai_input.isdigit():
            nilai = int(nilai_input)
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai Harus Antara 0 Sampai 100.")
        else:
            print("Input Harus Berupa angka!")

#Fungsi untuk konfirmasi "Ya" atau "Tidak"
def konfirmasi_ya_tidak(pesan):
    while True:
        jawab = input(pesan).strip().capitalize()
        if jawab in ["Ya", "Tidak"]:
            return jawab
        print("Input Tidak Valid. Harap Masukkan 'Ya' atau 'Tidak'.")

#Fungsi untuk menampilkan data dari nis yang dipilih untuk ditempilkan kembali
def konfirmasi_data_kembali():
    print(f"\nData Saat Ini dari Siswa dengan NIS {nis[index]} :")
    print(f"Nama        : {nama_siswa[index]}")
    print(f"Modul 1     : {nilai_modul1[index]}")
    print(f"Modul 2     : {nilai_modul2[index]}")
    print(f"Modul 3     : {nilai_modul3[index]}")

#Fungsi untuk secara otomatis menghasilkan NIS baru
def generate_nis():
    existing_numbers = [int(n[4:]) for n in nis]
    next_number = max(existing_numbers, default=0) + 1
    return f"JCDS{str(next_number).zfill(2)}"

#Fungsi untuk input nilai ujian, dengan validasi angka dan rentang (0-100)
def input_nilai(modul_ke):
    while True:
        nilai_input = input(f"Masukkan Hasil Ujian Modul {modul_ke} (0-100): ")
        if nilai_input.isdigit():
            nilai = int(nilai_input)
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai Harus Antara 0 Sampai 100.")
        else:
            print("Input Harus Berupa angka!")

#fungsi untuk menghitung total jumlah siswa, jumlah siswa lulus dan tidak lulus
def count_siswa():
    total = len(nis)
    lulus = keterangan.count("Lulus")
    tidak_lulus = keterangan.count("Tidak Lulus")

    print("\n--- Ringkasan Data Siswa ---")
    print(f"Total Siswa              : {total}")
    print(f"Jumlah Siswa Lulus       : {lulus}")
    print(f"Jumlah Siswa Tidak Lulus : {tidak_lulus}")


update_nilai() #Hitung nilai awal

#Program pertama dengan menu interaktif
while True:
    print(menu_instruction)
    instruction = input("Masukkan Angka Menu yang Ingin Dijalankan (1-7): ").strip()

    #Validasi input menu, jika nilai tidak sesuai maka akan mengeluarkan notifikasi bahwa menu tidak tersedia
    if not instruction.isdigit() or not 1 <= int(instruction) <= 7:
        print("Menu yang Anda Pilih Tidak Tersedia!")
        continue
    instruction = int(instruction)

#Instruction 1, Menampilkan seluruh daftar nilai siswa, dan rincian total jumlah siswa kelas, siswa lulus dan tidak lulus
    if instruction == 1:
        daftar_nilai()
        count_siswa()

#Instruction 2, Cari dan tampilkan data by nama/nis/keterangan lulus/tidak lulus
    elif instruction == 2:
        while True:
            print("\n--- Menu Filter dan Pencarian Data ---")
            print("1. Cari Berdasarkan Nama.")
            print("2. Cari Berdasarkan NIS.")
            print("3. Tampilkan Hanya Siswa yang LULUS.")
            print("4. Tampilkan hanya siswa yang TIDAK LULUS.")
            print("0. Kembali ke Menu Utama")

            pilihan_filter = input("Pilih Opsi Filter (0-4): ")

            #Filter berdasarkan nama
            if pilihan_filter == '1': 
                keyword = input("Silahkan Masukkan Nama (atau Bagian Dari Nama) Siswa yang Ingin Dicari: ").strip().lower()
                ditemukan = False
                count = 0
                for data in zip(nis, nama_siswa, nilai_modul1, nilai_modul2, nilai_modul3, avg_nilai, keterangan):
                    if keyword in data[1].lower():
                        count += 1
                        data_header()
                        data_row(count, *data)
                        ditemukan = True
                if not ditemukan:
                    print(f"\nMaaf, Tidak Ada Siswa Dengan Nama Mengandung '{keyword}'.")

            #Filter berdasarkan NIS
            elif pilihan_filter == '2':
                nis_input = input("Silahkan Masukkan NIS Siswa: ").strip().upper()
                if nis_input in nis:
                    i = nis.index(nis_input)
                    data_header()
                    data_row(1, nis[i], nama_siswa[i], nilai_modul1[i], nilai_modul2[i], nilai_modul3[i], avg_nilai[i], keterangan[i])
                else:
                    print(f"NIS {nis_input} Tidak Ditemukan.")

            #Filter siswa lulus
            elif pilihan_filter == '3':
                data_header()
                count = 0
                total_siswa = len(keterangan)
                for i, desc in enumerate(keterangan):
                    if desc == "Lulus":
                        count += 1
                        data_row(count, nis[i], nama_siswa[i], nilai_modul1[i], nilai_modul2[i], nilai_modul3[i], avg_nilai[i], keterangan[i])
                print(f"\nJumlah Siswa LULUS       : {count} dari {total_siswa} siswa")

            #Filter siswa tidak lulus
            elif pilihan_filter == '4':
                data_header()
                count = 0
                total_siswa = len(keterangan)
                for i, desc in enumerate(keterangan):
                    if desc == "Tidak Lulus":
                        count += 1
                        data_row(count, nis[i], nama_siswa[i], nilai_modul1[i], nilai_modul2[i], nilai_modul3[i], avg_nilai[i], keterangan[i])
                print(f"\nJumlah Siswa TIDAK LULUS : {count} dari {total_siswa} siswa")

            #Kembali ke menu utama
            elif pilihan_filter == '0':
                break
            else:
                print("Pilihan Tidak Tersedia. Silakan Coba Lagi atau Ketik 0 Untuk Kembali.")

#Instruction 3, Menambah daftar nilai siswa
    elif instruction == 3:
        lanjutkan_input = True

        while True:
            name = input("Masukkan Nama Siswa : ").title()

            if name in nama_siswa:
                print(f"Nama '{name}' Sudah Ada Dalam Daftar.")
                lanjut = konfirmasi_ya_tidak("Apakah Tetap Ingin Melanjutkan Penambahan? (Ya/Tidak): ")
                if lanjut == "Tidak":
                    print("Penambahan Dibatalkan.")
                    lanjutkan_input = False
                    break
                else:
                    break
            else:
                break

        if not lanjutkan_input:
            continue

        #input nilai dengan validasi dan konfirmasi
        m1 = input_nilai(1)
        m2 = input_nilai(2)
        m3 = input_nilai(3)
        print("\n--- Konfirmasi Data ---")
        print(f"Nama Siswa     : {name}")
        print(f"Ujian Modul 1  : {m1}")
        print(f"Ujian Modul 2  : {m2}")
        print(f"Ujian Modul 3  : {m3}")

        konfirmasi = konfirmasi_ya_tidak("Apakah Data Sudah Sesuai dan Ingin Ditambahkan? (Ya/Tidak) : ")

        if konfirmasi == 'Ya':
            nama_siswa.append(name)
            nilai_modul1.append(m1)
            nilai_modul2.append(m2)
            nilai_modul3.append(m3)
            nis.append(generate_nis())
            update_nilai()
            print("Data Berhasil Ditambahkan.")
            daftar_nilai()
            count_siswa()

        else:
            print("Penambahan Dibatalkan.")

#Instruction 4, Hapus data siswa berdasarkan NIS
    elif instruction == 4:
        daftar_nilai()
        while True:
            nis_input = input("Masukkan NIS Siswa yang Ingin Dihapus (Atau Ketik 'Batal' Untuk Kembali): ").strip().upper()
            if nis_input == "BATAL":
                break
            if nis_input in nis:
                index = nis.index(nis_input)
                konfirmasi_data_kembali()
                konfirmasi = konfirmasi_ya_tidak("Yakin Ingin Menghapus? (Ya/Tidak): ")
                if konfirmasi == "Ya":
                    for lst in [nama_siswa, nilai_modul1, nilai_modul2, nilai_modul3, nis]:
                        del lst[index]
                    update_nilai()
                    print("Data Berhasil Dihapus!")
                    daftar_nilai()
                else:
                    print("Penghapusan Dibatalkan.")
                break
            else:
                print(f"NIS {nis_input} Tidak Ditemukan.")

#Instruction 5, Ubah data nilai siswa
    elif instruction == 5:
        daftar_nilai()
        while True:
            nis_input = input("Masukkan NIS Siswa yang Ingin Diubah Datanya (Atau Ketik 'Batal'): ").strip().upper()
            if nis_input == "BATAL":
                break
            if nis_input in nis:
                index = nis.index(nis_input)

                # Menampilkan data lama siswa
                konfirmasi_data_kembali()

                # Input data baru
                name_baru = input("Masukkan Nama Baru (Tekan ENTER jika tidak ingin mengubah): ").title().strip()
                m1 = input_nilai(1)
                m2 = input_nilai(2)
                m3 = input_nilai(3)

                # Konfirmasi perubahan
                print("\n--- Konfirmasi Perubahan ---")
                print(f"Nama Lama        : {nama_siswa[index]}")
                print(f"Nama Baru        : {name_baru if name_baru else nama_siswa[index]}")
                print(f"Nilai Baru Modul : {m1} \n{m2} \n{m3}")
                konfirmasi = konfirmasi_ya_tidak("Yakin Ingin Menyimpan Perubahan? (Ya/Tidak): ")

                if konfirmasi == 'Ya':
                    if name_baru:  # hanya ubah nama jika input tidak kosong
                        nama_siswa[index] = name_baru
                    nilai_modul1[index] = m1
                    nilai_modul2[index] = m2
                    nilai_modul3[index] = m3
                    update_nilai()
                    print("Data Siswa Berhasil Diperbarui!")
                    daftar_nilai()
                else:
                    print("Perubahan Dibatalkan.")
                
            else:
                print(f"NIS {nis_input} Tidak Ditemukan.")

#Instruction 6, Urutkan berdasarkan nilai tertinggi atau terendah, dan abjad nama
    elif instruction == 6:
        while True:
            print("\n--- Urutkan Data Siswa ---")
            print("1. Berdasarkan Nilai Rata-Rata (Tertinggi ke Terendah)")
            print("2. Berdasarkan Nilai Rata-Rata (Terendah ke Tertinggi)")
            print("3. Berdasarkan Nama (A - Z)")
            print("4. Berdasarkan Nama (Z - A)")
            print("0. Kembali ke Menu Utama")

            pilihan_sort = input("Pilih Angka (1/2/3/4/0): ").strip()

            if pilihan_sort == '0':
                break

            data_siswa = list(zip(nis, nama_siswa, nilai_modul1, nilai_modul2, nilai_modul3, avg_nilai, keterangan))

            if pilihan_sort == '1':
                data_siswa.sort(key=lambda x: x[5], reverse=True)
                print("\nData Siswa Diurutkan Berdasarkan Nilai Rata-Rata (Tertinggi ke Terendah):")

            elif pilihan_sort == '2':
                data_siswa.sort(key=lambda x: x[5])
                print("\nData Siswa Diurutkan Berdasarkan Nilai Rata-Rata (Terendah ke Tertinggi):")

            elif pilihan_sort == '3':
                data_siswa.sort(key=lambda x: x[1].lower())
                print("\nData Siswa Diurutkan Berdasarkan Nama (A - Z):")

            elif pilihan_sort == '4':
                data_siswa.sort(key=lambda x: x[1].lower(), reverse=True)
                print("\nData Siswa Diurutkan Berdasarkan Nama (Z - A):")

            else:
                print("Pilihan Tidak Valid. Silahkan Coba Lagi!")
                continue

            data_header()
            for i, siswa in enumerate(data_siswa, 1):
                data_row(i, *siswa)

            count_siswa()  

                
#Instruction 7, Keluar dari program
    elif instruction == 7:
        print("Terima kasih! Program Selesai.")
        print("Semoga Hari Anda Menyenangkan!")
        break
