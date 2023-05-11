print(" ____        _   _                   _ _        _   _                       ")
print("|  _ \ _   _| |_| |__   ___  _ __   (_) | ___  | | | | ___  ___  __ _ _ __  ")
print("| |_) | | | | __| '_ \ / _ \| '_ \  | | |/ _ \ | |_| |/ _ \/ __|/ _` | '_ \ ")
print("|  __/| |_| | |_| | | | (_) | | | | | | |  __/ |  _  |  __/\__ \ (_| | |_) |")
print("|_|    \__, |\__|_| |_|\___/|_| |_| |_|_|\___| |_| |_|\___||___/\__,_| .__/ ")
print("       |___/                                                         |_|    ")
print(" __  __       _    _                 _ ")
print("|  \/  | __ _| | _(_)_ __   ___  ___(_)")
print("| |\/| |/ _` | |/ / | '_ \ / _ \/ __| |")
print("| |  | | (_| |   <| | | | |  __/\__ \ |")
print("|_|  |_|\__,_|_|\_\_|_| |_|\___||___/_|")
print("=========================================")
print("Author:azatmg")
print("""
______________________
|    =İSLEMLER=      |
|                    |
|    + = Toplama     |
|    - = Çıkarma     |
|    * = Çarpma      |
|    / = Bölme       |
|____________________|
""")
islem=input("islem gir:")
sayi1=int(input("sayi1:"))
sayi2=int(input("sayi2:"))
if islem=="+":
   sonuc=int(sayi1)+int(sayi2)
   print("sonuc:",str(sonuc))
elif islem=="-":
   sonuc=int(sayi1)-int(sayi2)
   print("sonuc:",str(sonuc))
elif islem=="*":
   sonuc=int(sayi1)*int(sayi2)
   print("sonuc:",str(sonuc))
elif islem=="/":
   sonuc=int(sayi1)/int(sayi2)
   print("sonuc:",str(sonuc))
