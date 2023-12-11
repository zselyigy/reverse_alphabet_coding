# letters to be replaced
alphabet = 'aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz'
# capital version also replaced
capitalalphabet = alphabet.upper()
la = len(alphabet)

a = input('Írd be az átalakítandó szöveget! ')

b = ''
for i in range(len(a)):
    if a[i] in alphabet:
        mychr = alphabet[la - alphabet.find(a[i])-1]
    elif a[i] in capitalalphabet:
        mychr = capitalalphabet[la - capitalalphabet.find(a[i])-1]
    else:
        # what is missing from the alphabet is kept as it
        mychr = a[i]
    b = b + mychr

print(b)
