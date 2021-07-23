
pos_tags = [ 'NOUN', 'ADJ', 'ADV', 'INTJ', 'PROPN', 'VERB' ]

i=0
while i < len(pos_tags):
  ptag = pos_tags[i]
  print(ptag.lower())
  i += 1


message = 'Γράψτε κάτι: '
quit_while = False

while not quit_while:
  user_input = input(message)
  if user_input == 'quit':
    quit_while = True
  else:
    print(user_input)


while True:
  user_input = input(message)
  if user_input == 'quit':
    break
  else:
    print(user_input)
