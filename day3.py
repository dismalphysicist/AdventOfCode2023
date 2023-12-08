import re 

def parse_line(line,pattern):
  return [(m.start(),int(m.group()) if m.group()[0].isdigit() else m.group()) \
                for m in re.finditer(pattern,line)]

def parse_data(data,pattern):
  return [parse_line(data[i],pattern) for i in range(len(data))]


lines = []
with open("input3.txt") as f:
  lines = f.read().splitlines()

# regexes
numbers = parse_data(lines, r"\d+")
symbols = parse_data(lines, r"[^\d\.]")
gears   = parse_data(lines,r"\*")

# part 1
sumPartNums = 0
for i,instances in enumerate(numbers):
  for (j,number) in instances:
    # get all the symbol rows in the same list
    adjRows = []
    adjRows += symbols[i] # hack to copy instead of reference
    if i!=0:
      adjRows += symbols[i-1]
    if i!=len(lines)-1:
      adjRows += symbols[i+1]

    for (jsymb,symbol) in adjRows:
      if jsymb >= j-1 and jsymb <= j+len(str(number)):
        # print("{} is adjacent to {}".format(number,symbol))
        sumPartNums += number
        break

print("Answer to part 1 is {}".format(sumPartNums))

# part 2
sumGearRatios = 0
for i,instances in enumerate(gears):
  for (j,gear) in instances:
    gearRatio = 1
    adjNumCount = 0
    # get all the number rows in the same list
    adjRows = []
    adjRows += numbers[i] # hack to copy instead of reference
    if i!=0:
      adjRows += numbers[i-1]
    if i!=len(lines)-1:
      adjRows += numbers[i+1]

    for (jnum,number) in adjRows:
      if jnum+len(str(number)) >= j and jnum <= j+1:
        # print("{} is adjacent to {}".format(gear,number))
        gearRatio *= number
        adjNumCount += 1

    # check it actually is a gear
    if adjNumCount == 2:
      sumGearRatios += gearRatio

print("Answer to part 2 is {}".format(sumGearRatios))