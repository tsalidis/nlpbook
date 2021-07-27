
from random import randint

for i in range(1,6):
  print(randint(1, 10))

file_contents = 'contents.txt';
with open(file_contents) as fn:
  contents = fn.read();  
print(contents)

print('#######')

with open(file_contents) as fn:
  for line in fn:
    for word in line.split():
      print(word)

print('#######')

new_file = 'new_file.txt'
with open(new_file,'w') as nfl:
  nfl.write("Η πρώτη γραμμή του αρχείου\n")
  nfl.write("Η δεύτερη γραμμή του αρχείου\n")

with open(new_file) as fn:
  contents = fn.read();  
print(contents)
