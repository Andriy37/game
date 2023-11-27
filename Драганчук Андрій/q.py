with open("quotes.txt", "r", encoding='UTF-8') as file:
    data = file.read()
    print(data)

autor = input("Хто написав ці рядки?")

with open("quotes.txt", "a", encoding='UTF-8') as file:
    file.write(f"\n{autor}\n")
    print(data)
               
with open("quotes.txt", "r", encoding='UTF-8') as file:
    data = file.read()
    print(data)