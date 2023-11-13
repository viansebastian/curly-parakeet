# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan
    
#     def tambah_kecepatan(self):
#         self.kecepatan += 10


# class MobilSport(Mobil):
#     def turbo(self):
#         self.kecepatan += 50

# # Kelas Mobil Dasar
# mobil_1 = Mobil("Merah", "DicodingCar", 160)
# print(mobil_1.kecepatan)

# # Kelas Mobil Sport
# mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
# print(mobil_sport_1.kecepatan)
# mobil_sport_1.turbo()
# print(mobil_sport_1.kecepatan)

# """
# Output:
# 160
# 160
# 210
# """

"""
TODO:
1. Buatlah class bernama Animal dengan ketentuan:
    - Memiliki properti:
      - name: string
      - age: int
      - species: string
    - Memiliki constructor untuk menginisialisasi properti:
      - name
      - age
      - species
2. Buatlah class bernama Cat dengan ketentuan:
    - Merupakan turunan dari class Animal
    - Memiliki method:
      - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
        "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
      - bernama "suara" yang akan mengembalikan nilai string "meow!"
 3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
    - Atribut name bernilai: "Neko"
    - Atribut age bernilai: 3
    - Atribut species bernilai: "Persian".
"""

#TODO: Silakan buat kode Anda di bawah ini.

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
class Cat(Animal): 
    def deskripsi(self): 
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    
    def suara(self): 
        return "meow!"

myCat = Cat("Neko", 3, "Persian")
myCat.deskripsi()
myCat.suara()