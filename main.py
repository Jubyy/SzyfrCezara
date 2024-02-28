
def stworz_alfabet():
    alphabet = []
    for i in range(65, 91):
        char = chr(i)
        alphabet.append(char)
    for i in range(48, 58):
        char = chr(i)
        alphabet.append(char)
    return alphabet




def szyfr_cezara():

    alphabet = stworz_alfabet()
    przesuniety_alfabet = []
    tryb = int(input('1 szyfrowanie ------- 2 deszyfrowanie:'))
    przesuniecie = int(input('Podaj przesuniecie dla szyfru:'))
    wynik = ''

    if przesuniecie>len(alphabet):
        przesuniecie = przesuniecie%len(alphabet)

    if tryb == 1:
        plik = input('Podaj nazwe pliku zeby zaszyfrowac: ')
        przesuniety_alfabet = alphabet[przesuniecie:] + alphabet[:przesuniecie]
        try:
            with open(f'{plik}','r') as file:
                dane = file.read()
                for i in dane:
                    i=i.upper()
                    if i == '\n':
                        wynik += '\n'
                    elif i not in alphabet:
                        wynik += f'{i}'
                    else:
                        wynik+= przesuniety_alfabet[alphabet.index(i.upper())]
        except FileNotFoundError:
            print('zla nazwa pliku!')
        with open('szyfr.txt','w') as file:
            file.write(wynik)
    elif tryb == 2:
        plik = input('Podaj nazwe pliku aby deszyfrowac: ')
        przesuniety_alfabet = alphabet[-przesuniecie:] + alphabet[:-przesuniecie]
        try:
            with open(f'{plik}','r') as file:
                dane = file.read()
                for i in dane:
                    if i == '\n':
                        wynik+='\n'
                    elif i not in alphabet:
                        wynik += f'{i}'
                    else:
                        wynik += przesuniety_alfabet[alphabet.index(i.upper())]
        except FileNotFoundError:
            print('Nie ma takiego pliku!')
        with open('deszyfr.txt','w') as file:
            file.write(wynik)
    else:
        print('blad!')


is_on = True
szyfr_cezara()
while is_on:
    dalej = int(input('\n1 jesli chcesz uzyc tego jeszcze raz ------ 2 Koniec: '))
    if dalej == 1:
        szyfr_cezara()
    else:
        break



