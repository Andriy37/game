from PIL import ImageFilter , Image

with Image.open("pes.jpg") as pip_original:

    print("розмір", pip_original.size)
    print("форма ", pip_original.format)
    print("тип ", pip_original.mode)
    pip_original.show()

    pip_gray = pip_original.convert("L")
    pip_gray.save("pes1.jpg")
    print("розмір", pip_gray.size)
    print("форма ", pip_gray.format)
    print("тип ", pip_gray.mode)
   
    pip_gray.show()


