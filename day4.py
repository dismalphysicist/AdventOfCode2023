import re 

def parse_line(line,pattern):
  return [int(m.group()) if m.group()[0].isdigit() else m.group() \
                for m in re.finditer(pattern,line)]

def score_card1(card):
  matches = 0
  winningNums, myNums = card.split(":")[1].split("|")
  winningNums = parse_line(winningNums,r"\d+")
  myNums      = parse_line(myNums,r"\d+")

  for mn in myNums:
    if mn in winningNums:
      matches += 1

  return matches

def score_card2(ids,cards):
  
  if len(ids)==0:
    # no matches
    return 0
  
  elif len(ids)==1:
    # add 1 to total and score matches as copies
    matches = score_card1(cards[ids[0]-1])
    return 1 + score_card2([i for i in range(ids[0]+1,ids[0]+matches+1)],cards)
  
  else:
    # need to reduce further
    # evaluate first + rest
    first = ids.pop(0)
    return score_card2([first],cards) + score_card2(ids,cards)

lines = []

with open("input4.txt") as f:
  lines = f.read().splitlines()

ids = []
sumPoints = 0
for card in lines:
  # make list of ids for part 2
  id = parse_line(card.split(":")[0],r"\d+")[0]
  ids.append(id)

  # score points on cards for part 1
  matches = score_card1(card)
  sumPoints += 2**(matches-1) if matches>0 else 0

print("Answer to part 1 is {}".format(sumPoints))

print("Answer to part 2 is {}".format(score_card2(ids,lines)))