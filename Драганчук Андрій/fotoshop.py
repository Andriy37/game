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
   
    pip_180 = pip_original.rotate(180)
    pip_180.save("pip_180.jpg")
    print("розмір", pip_180.size)
    print("форма ", pip_180.format)
    print("тип ", pip_180.mode)
    
    pip_180_2 = pip_original.rotate(180)
    pip_180_2.save("pip_180_2.jpg")
    print("розмір", pip_180_2.size)
    print("форма ", pip_180_2.format)
    print("тип ", pip_180_2.mode)

    pip_blur = pip_original.filter(ImageFilter.BLUR)
    pip_blur.save("pip_blur.jpg")
    print("розмір", pip_blur.size)
    print("форма ", pip_blur.format)
    print("тип ", pip_blur.mode)
   
    pip_gray.show()
    pip_180.show()
    
    pip_blur.show()


