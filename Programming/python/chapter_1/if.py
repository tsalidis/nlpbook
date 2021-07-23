
pos_tags = [ 'NOUN', 'ADJ', 'ADV', 'INTJ', 'PROPN', 'VERB' ]

for ptag in pos_tags:
  if ptag == 'ADJ':
    print('Adjective')
  else:
    print(ptag.lower())

print('\n###########\n')

ptag = 'PRON'
if ptag not in pos_tags:
  print(ptag.title())

if ptag not in pos_tags and 'VERB' in pos_tags:
  print('Found')

if ptag == 'NOUN':
  print('Noun')
elif ptag == 'ADJ':
  print('Adjective')
elif ptag == 'ADV':
  print('Adverb')
elif ptag == 'INTJ':
  print('Interjection')
elif ptag == 'VERB':
  print('Verb')
else:
  print('Proper Noun')
