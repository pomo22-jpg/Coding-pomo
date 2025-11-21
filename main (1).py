print("======================program penerimaan karyawan==========================")
nama=input("masukan nama anda :")
jenis_kelamin=input("masukan jenis kelamin L/P :")
usia=int(input("masukan usia anda :"))
kerja=int(input("masukan pengalaman kerja anda :"))
ijasah=input("masukan ijasah anda :")

if jenis_kelamin=="l" and usia >=17 and usia<=30 and kerja >=3 and ijasah in ["sma","smp","smk","s1"]:
    print("selamat anda lulus ketahap selanjutnya")
elif usia==16:
    print("ananda lolos tapi masih dalam masa tunggu")
else:
    print("selamat anda telah gagal")