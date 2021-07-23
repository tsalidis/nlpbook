
print("lists")
pos_tags = [ 'NOUN', 'ADJ', 'ADV', 'INTJ', 'PROPN', 'VERB' ]

print(pos_tags[0])
print(pos_tags[-1])

print(pos_tags)

tmp = pos_tags[1]
pos_tags[1] = pos_tags[0]
pos_tags[0] = tmp

print(pos_tags)

pos_tags.append('PRON')
print(pos_tags)

pos_tags.insert(1,'PART')
print(pos_tags)

del pos_tags[1]
print(pos_tags)

ptag = pos_tags.pop()
print(ptag)
print(pos_tags)

ptag2 = pos_tags.pop(2)
print(ptag)
print(pos_tags)

pos_tags.append('PART')
pos_tags.append(ptag)
pos_tags.append(ptag2)
print(pos_tags)

sorted_tags = sorted(pos_tags)
print(pos_tags)
print(sorted_tags)

pos_tags.sort()
print(pos_tags)

pos_tags.reverse()
print(pos_tags)

ptags_len = len(pos_tags)
print(ptags_len)

#for

for ptag in pos_tags:
  print(ptag.lower())

numbers = list(range(1,6))
print(numbers)
 
cubes = []
for num in numbers:
  cub = num ** 3
  cubes.append(cub)
print(cubes)  

cubes2 = [ num ** 3 for num in range(1,6)]
print(cubes2)

print(cubes[0:3])
print(cubes[:3])
print(cubes[3:])
print(cubes[-3:])
print(cubes[:])

cubes3 = cubes
cubes.append(6**3)
print(cubes)
print(cubes3)
