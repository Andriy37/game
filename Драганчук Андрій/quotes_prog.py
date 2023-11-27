#напиши тут свою програму
with open('quotes.txt', "r" ,encoding='UTF-8') as file:
    data = file.read()
    print(data)

author = input('Хто написав ці рядки ?')

with open('quotes.txt', 'w', encoding='UTF-8') as file:
    file.write(f"\n{author}\n")

with open('quotes.txt', "r" ,encoding='UTF-8') as file:
    data = file.read()
    print(data)