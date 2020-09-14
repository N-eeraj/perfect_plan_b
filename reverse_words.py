from read import Read

sentence = Read(str, 'Sentence')

words = sentence.split() #spliting string into list on blank spaces
words.reverse() #reversing lists

print(' '.join(words)) #joining list items with blank spaces
