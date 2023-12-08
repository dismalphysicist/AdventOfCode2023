import re 

def parse_line(line,pattern):
  return [int(m.group()) if m.group()[0].isdigit() else m.group() \
                for m in re.finditer(pattern,line)]

lines = []

with open("input4.txt") as f:
  lines = f.read().splitlines()

sumPoints = 0
for card in lines:
  matches = 0

  winningNums, myNums = card.split(":")[1].split("|")
  winningNums = parse_line(winningNums,r"\d+")
  myNums      = parse_line(myNums,r"\d+")

  for mn in myNums:
    if mn in winningNums:
      matches += 1

  sumPoints += 2**(matches-1) if matches>0 else 0

print(sumPoints)