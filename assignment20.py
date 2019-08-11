def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['a','b','c','d','e']
show_magicians(magicians)

def make_great(magicians):
    for number in range(0,len(magicians)):
        magicians[number] = "the Great " + magicians[number]
        print(magicians[number])
make_great(magicians[:])
show_magicians(magicians)

print("hahaha")

