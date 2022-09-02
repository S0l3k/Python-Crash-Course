fBook = 'PrideandPrejudice.txt'
sBook = 'TheAdventuresofSherlockHolmes.txt'
tBook = 'Frankenstein.txt'

with open(fBook, encoding= 'utf-8') as venv:
    contents = venv.read()

words = contents.split()
num_words = len(words)
print(f"File {fBook} has about {num_words} words.")
print("Word 'the'", contents.lower().count('the'))

with open(sBook, encoding= 'utf-8') as venv:
    contents2 = venv.read()

words2 = contents2.split()
num_words2 = len(words2)
print(f"File {sBook} has about {num_words2} words.")
print("Word 'the'", contents2.lower().count('the'))

with open(tBook, encoding= 'utf-8') as venv:
    contents3 = venv.read()

words3 = contents3.split()
num_words3 = len(words3)
print(f"File {tBook} has about {num_words3} words.")
print("Word 'the'", contents3.lower().count('the'))