from wlcm import welcome_message

welcome_message('Dokumen Rahasia')

nama_user = input ('Masukkan nama anda terlebih dahulu untuk keamanan dokumen : ')

while nama_user == '' :
    nama_user = input ('Tolong masukkan nama anda sesuai prosedur : ')
    
id_karyawan = input ('Masukkan ID karyawan anda : ') 

while id_karyawan == '' :
    id_karyawan = input ('Masukkan ID karyawan terlebih dulu : ')
    
from wlcm import passwordmenu
from wlcm import passwordkaryawanmenu
from wlcm import passwordkrabbypatty


password_user = input (f'\nHallo selamat datang {nama_user} dengan ID {id_karyawan}, Tolong masukkan password terlebih dahulu : ')

while True :
    if password_user == passwordmenu :
        Main_menu = input('\nSelamat datang di System Restoran Krusty Crab, Silahkan pilih System Menu : \n "List harga" "Info karyawan" "Resep Kraby Patty" \n\n*note pastikan format kalimat menu yang kalian masukkan sesuai dengan yang list menu diatas\nSilahkan pilih menu mana yang ingin kalian akses? : ' )
    else :
        print ('Anda Memasukan Pasword yang salah!!!!')
        print ('System akan diberhentikan')
        break
        
    from wlcm import list_harga
    from wlcm import data_karyawan 
    from wlcm import resep_krabbypatty    

    if Main_menu == 'List harga' :
        list_harga ()
        kembali = input('\nKetik "Back" untuk kembali, "Exit" untuk keluar dari System : ')
        if kembali == 'Back' :
            continue
        elif kembali == 'Exit' :
            print (' "Tolong tetap jaga kerahasiaan data kita!!!" ')
            break
    elif Main_menu == 'Info karyawan':
        passcode = input('\nMasukan Password untuk masuk ke menu info karyawan : ')
        if passcode == passwordkaryawanmenu : 
            data_karyawan ()
            kembali = input('\nKetik "Back" untuk kembali, "Exit" untuk keluar dari System : ')
            if kembali == 'Back' :
                continue
            elif kembali == 'Exit' :
                print (' "Tolong tetap jaga kerahasiaan data kita!!!" ')
                break
        else:
            print ('\nKamu dikeluarkan dari system dikarenakan password yang kamu input salah!!!')
            break
    elif Main_menu == 'Resep Kraby Patty' :
        passresep = input('\nMasukan Password untuk masuk ke menu Resep Krabby Patty : ')
        if passresep == passwordkrabbypatty :
            resep_krabbypatty ()
            kembali = input('\nKetik "Back" untuk kembali, "Exit" untuk keluar dari System : ')
            if kembali == 'Back' :
                continue
            elif kembali == 'Exit' :
                print (' "Tolong tetap jaga kerahasiaan data kita!!!" ')
                break
        else :
            print ('Password yang kamu masukkan salah!!! Kamu akan dikeluarkan dari system')
            break
            

