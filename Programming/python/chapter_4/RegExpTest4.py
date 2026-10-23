import re

pattern = re.compile(r"(\w+)(\s+)(\w+)", flags=re.MULTILINE)

test_string = "ένα    παράδειγμα "

matches = pattern.finditer(test_string)

for match_num, match in enumerate(matches, start=1):
  print(f"Match {match_num} was found at {match.start()}-{match.end()}: {match.group()}")

  for group_num, group in enumerate(match.groups(), start=1):
    print(f"Group {group_num} found at {match.start(group_num)}-{match.end(group_num)}: {group}")
