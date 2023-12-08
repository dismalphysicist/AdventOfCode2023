import re 

def parse_line(line,pattern):
  return [int(m.group()) if m.group()[0].isdigit() else m.group() \
                for m in re.finditer(pattern,line)]

def parse_map(data,map_name):
  mapdata = data[re.search(map_name,data).end():]
  endmap = re.search(r"[a-z]",mapdata)
  if endmap != None:
    mapdata = mapdata[:re.search(r"[a-z]",mapdata).start()]
  mapdata = mapdata.strip().splitlines()
  mapdata = [[int(i) for i in m.split(" ")] for m in mapdata]
  dest_starts   = [s[0] for s in mapdata]
  source_starts = [s[1] for s in mapdata]
  lengths       = [s[2] for s in mapdata]
  return dest_starts, source_starts, lengths

def map_lookup(maptuple,num):
  dest_starts,source_starts,lengths = maptuple
  for i,start in enumerate(source_starts):
    diff = num-start
    if diff >= 0 and diff < lengths[i]:
      # num needs to be remapped
      return dest_starts[i]+diff
  # num does not need to be remapped
  return num

with open("input5.txt") as f:
  seeds = parse_line(f.readline(),r"\d+")
  data = f.read()
  seed_soil        = parse_map(data,"seed-to-soil map:")
  soil_fertilizer  = parse_map(data,"soil-to-fertilizer map:")
  fertilizer_water = parse_map(data,"fertilizer-to-water map:")
  water_light      = parse_map(data,"water-to-light map:")
  light_temp       = parse_map(data,"light-to-temperature map:")
  temp_humidity    = parse_map(data,"temperature-to-humidity map:")
  humidity_loc     = parse_map(data,"humidity-to-location map:")

  locations = []
  for seed in seeds:
    location = map_lookup(humidity_loc,map_lookup(temp_humidity, \
                map_lookup(light_temp,map_lookup(water_light, \
                  map_lookup(fertilizer_water,map_lookup(soil_fertilizer, \
                    map_lookup(seed_soil,seed)))))))
    locations.append(location)

  print("Answer to part 1 is {}".format(min(locations)))
