with open("input1.txt","r") as f:
  lines = f.read().splitlines()

  sum = 0
  for line in lines:
    digits = ""
    for c in line:
      if c.isdigit():
        digits += c
    sum += int(digits[0]+digits[-1])

  print(sum)