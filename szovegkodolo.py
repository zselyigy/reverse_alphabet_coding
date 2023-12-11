alphabet = 'aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz'
la = len(alphabet)

a = input('Írd be az átalakítandó szöveget! ')

b = ''
for i in range(len(a)):
    if a[i] == ' ':
        mychr = ' '
    else:
        mychr = alphabet[la - alphabet.find(a[i])-1]
    b = b + mychr

print(b)
