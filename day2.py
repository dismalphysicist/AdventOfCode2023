with open("input2.txt","r") as f:
  lines = f.read().splitlines()

  # minimum numbers of cubes to test against
  reqmin = [12,13,14]
  sumid = 0
  sumpowmin = 0

  for line in lines:
    # minimum number of red, green, blue cubes needed respectively
    minima = [0,0,0]
    colourkey = ["red","green","blue"]
    
    game = line.split(":",maxsplit=1)
    id = int(game[0][5:])
    game = [g.strip() for g in game[1].split(";")]
    
    for handful in game:
      cubes = [c.strip() for c in handful.split(",")]
      for c in cubes:
        for i in range(len(minima)):
          if c.split(" ",maxsplit=1)[1] == colourkey[i]:
            newN = int(c.split(" ",maxsplit=1)[0])
            minima[i] = max(minima[i],newN)

    possible = True
    for i,n in enumerate(minima):
      if n > reqmin[i]:
        possible = False
        break

    if (possible):
      sumid += id

    sumpowmin += minima[0]*minima[1]*minima[2]

  print("Answer to part 1 is: {}".format(sumid))
  print("Answer to part 2 is: {}".format(sumpowmin))