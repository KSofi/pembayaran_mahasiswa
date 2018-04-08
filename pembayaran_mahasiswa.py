def pembayaran() :
    print ("**Pembayaran Mahasiswa**")
    print ("========================")
    nama = input("\nNama : " )
    nim = input("\nNIM : ")
    kelas = input("\nKelas : ")
    semester = input("\nSemester : ")
    print ("\n\t---Pilihan Pembayaran---")
    print ("\n\t1. Pembayaran SPP")
    print ("\n\t2. Pembayaran UTS")
    print ("\n\t3. Pembayaran UAS")
    print ("\n\t4. Pembayaran SPP & UTS")
    print ("\n\t5. Pembayaran SPP & UAS")

    pilih = input ("\n\tSilahkan Pilih : ")
    if pilih == "1" :
        spp ()
    elif pilih == "2" :
        uts ()
    elif pilih == "3" :
        uas ()
    elif pilih == "4" :
        spp_uts ()
    elif pilih == "5" :
        spp_uas ()
    else :
        exit
        
def spp () :
    bulan = int(input("\n\tJumlah Bulan = "))
    bulan = float(bulan)
    total_spp = 500000 * bulan
    total = total_spp + 5000
    print ("\n\tTotal SPP Rp. 500000 * ",bulan," = Rp. ", total_spp)
    print ("\n\tBiaya Tambahan Sever Rp. 5000")
    print ("============================================")
    print ("\tTotal yang Harus Dibayar = Rp. Rp. ", total)
    tanya ()

def uts () :
    mk = int(input("\n\tJumlah Mata Kuliah = "))
    mk = float(mk)
    total_uts = 50000 * mk
    total = total_uts + 5000
    print ("\n\tTotal UAS Rp. 50000 * ",mk," = Rp. ", total_uts)
    print ("\n\tBiaya Tambahan Server Rp. 5000")
    print ("===========================================")
    print ("\n\tTotal yang Harus Dibayar Rp. ", total)
    tanya ()

def uas () :
    matkul = int(input("\n\tJumlah Mata Kuliah = "))
    matkul = float(matkul)
    total_uas = 50000 * matkul
    total = total_uas + 5000
    print ("\n\tTotal UAS Rp. 50000 * ",matkul," = Rp. ", total_uas)
    print ("\n\tBiaya Tambahan Server Rp. 5000")
    print ("===========================================")
    print ("\n\tTotal yang Harus Dibayar Rp. ", total)
    tanya ()

def spp_uts () :
    bulan = int(input("\n\tJumlah Bulan = "))
    mk = int(input("\n\tJumlah Mata Kuliah = "))
    bulan = float(bulan)
    mk = float(mk)
    total_spp = 500000 * bulan
    total_uts = 50000 * mk
    total = total_spp + total_uts + 5000
    print ("\n\tTotal SPP Rp. 500000 * ",bulan," = Rp. ", total_spp)
    print ("\n\tTotal UTS Rp. 50000 * ",mk," = Rp. ", total_uts)
    print ("\n\tBiaya Tambahan Server Rp. 5000")
    print ("==========================================")
    print ("\n\tTotal yang harus dibayar Rp. ", total)
    tanya ()

def spp_uas () :
    bulan = int(input("\n\tJumlah Bulan = "))
    matkul = int(input("\n\tJumlah Mata Kuliah = "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp = 500000 * bulan
    total_uas = 50000 * matkul
    total = total_spp + total_uas + 5000
    print ("\n\tTotal SPP Rp. 500000 * ",bulan," = Rp. ", total_spp)
    print ("\n\tTotal UAS Rp. 50000 * ",matkul," = Rp. ", total_uas)
    print ("\n\tBiaya Tambahan Server Rp. 5000")
    print ("==========================================")
    print ("\n\tTotal yang Harus Dibayar Rp. ", total)
    tanya ()
    
def tanya () :
    tanya = input ("Lakukan Pembayaran Lagi (y/n)?")
    if tanya == "y" :
        pembayaran ()
    if tanya == "n" :
        exit
    else :
        print ("\n\tMaaf Pilihan Tidak Tersedia..!!")

pembayaran ()
