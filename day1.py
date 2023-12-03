import re

with open("input1.txt","r") as f:
  lines = f.read().splitlines()

  sum = 0
  valid_digits = {"one":"1","two":"2","three":"3","four":"4","five":"5", \
                    "six":"6","seven":"7","eight":"8","nine":"9", \
                    "1":"1","2":"2","3":"3","4":"4","5":"5","6":"6", \
                    "7":"7","8":"8","9":"9"}
  for line in lines:
    print(line)
    digits_regex = r"[0-9]|one|two|three|four|five|six|seven|eight|nine"
    digits_reversed = r"[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin"
    
    first = valid_digits[re.search(digits_regex,line).group()]
    last = valid_digits[re.search(digits_reversed,line[::-1]).group()[::-1]]
    
    sum += int(first+last)

  print(sum)