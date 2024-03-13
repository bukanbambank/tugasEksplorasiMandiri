Pria = {'p1', 'p2', 'p3', 'p4'}  # Himpunan pria
Wanita = {'w1', 'w2', 'w3', 'w4'}  # Himpunan wanita
Preferensi_Pria = {'p1': ['w2', 'w3', 'w1', 'w4'],
                   'p2': ['w3', 'w1', 'w4', 'w2'],
                   'p3': ['w4', 'w2', 'w3', 'w1'],
                   'p4': ['w1', 'w3', 'w2', 'w4']}
Preferensi_Wanita = {'w1': ['p3', 'p1', 'p2', 'p4'],
                     'w2': ['p4', 'p3', 'p2', 'p1'],
                     'w3': ['p1', 'p4', 'p3', 'p2'],
                     'w4': ['p2', 'p1', 'p3', 'p4']}
Pasangan = {}
Pria_Belum_Bertunangan = list(Pria)

def masalah_pencocokan_stabil(Pria, Wanita, Preferensi_Pria, Preferensi_Wanita):
    Pasangan = {}
    Pria_Belum_Bertunangan = list(Pria)

    while Pria_Belum_Bertunangan:  # Selama masih ada pria yang belum bertunangan
        pria = Pria_Belum_Bertunangan.pop(0)  # Pilih pria dari Pria_Belum_Bertunangan
        wanita = Preferensi_Pria[pria][0]  # Pilih wanita dari daftar preferensi pria

        if wanita not in Pasangan:  # Jika wanita belum bertunangan
            Pasangan[wanita] = pria  # Wanita bertunangan dengan pria
        else:
            pria_terpilih_sekarang = Pasangan[wanita]  # Pria yang saat ini bertunangan dengan wanita
            if Preferensi_Wanita[wanita].index(pria) < Preferensi_Wanita[wanita].index(pria_terpilih_sekarang):  # Jika wanita lebih suka pria baru
                Pria_Belum_Bertunangan.append(pria_terpilih_sekarang)  # Pria saat ini menjadi bebas
                Pasangan[wanita] = pria  # Wanita bertunangan dengan pria baru
            else:
                Pria_Belum_Bertunangan.append(pria)  # Pria baru menjadi bebas

    return Pasangan  # Kembalikan himpunan pasangan yang telah bertunangan

hasil = masalah_pencocokan_stabil(Pria, Wanita, Preferensi_Pria, Preferensi_Wanita)
print("Pasangan yang telah bertunangan:", hasil)
