
word_w1 = { 'pos' : 'noun', 'gender' : 'neutral', 'case' : 'genitive', 'number' : 'singular'};

print(word_w1)
print(word_w1['gender'])

word_w1['case'] = 'accusative'
print(word_w1)

del word_w1['gender']
print(word_w1)

hw = word_w1.get('lemma','Does not exist!')
print(hw)

hw = word_w1.get('lemma')
print(hw)

print('----------------')
for key,val in word_w1.items():
  print(f"{key} = {val}")

print('----------------')
for key in word_w1.keys():
  print(f"Key = {key}")

print('----------------')
for val in word_w1.values():
  print(f"Value = {val}")

print('----------------')
for key in sorted(word_w1.keys()):
  print(f"Key: {key} = Value: {word_w1[key]}")

print('----------------')
word_w2 = { 'pos' : 'adj', 'gender' : 'neutral', 'case' : 'accusative', 'number' : 'singular'};
word_w3 = { 'pos' : 'adj', 'gender' : 'neutral', 'case' : 'nominative', 'number' : 'plural'};


words = [ word_w1, word_w2, word_w3]

print(words)