# for i in range(1, 3):    
#     for j in range(1, 3):    
#     print(i,j) 

""""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.

# def minimal(a, b): 
#     result = min(a,b)
#     return result

minimal = lambda a, b: min(a,b)
greet = lambda name: print(f"hello {name}")

print(minimal(10,10))
greet("alana")