#skrypt8.py
imie = input("Jak masz na imię?")
print ("Witaj",imie,"!")
skala = int(input('Podaj liczbę opisującą intensywność wiatru w skali Beauforta: '))
if skala == 0:
    print('Że niby będziesz wiosłować?')
elif skala <= 4:
    print('Spokojnie. Możesz wypływać!')
elif skala >= 8 and skala <= 12:
    print('To sobie wybrałeś pogodę na żeglowanie.')
elif skala < 0 or skala > 12:
   print('Chyba za dużo dzisiaj wypiłeś.')
else:
    print('Zostań w porcie!')
