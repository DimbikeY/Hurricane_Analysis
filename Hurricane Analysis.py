# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
conversion = {"M": 1000000,
              "B": 1000000000}
# Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".
updated_damage = []
def updated():
  for element in damages:
    if element[-1] == "M":
      updated_damage.append(1000000 * float(element[:-1]))
    elif element[-1] == "B":
        updated_damage.append(1000000000 * float(element[:-1]))
    else:
       updated_damage.append(element)
  print(updated_damage)

updated()
print()

# Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.
tables = {}
def table(name):
  for element in range(len(names)):
      names_element = names[element]
      if names_element == name:
        months_element = months[element]
        years_element = years[element]
        sustained_element = max_sustained_winds[element]
        affected_element = areas_affected[element]
        damage_element = updated_damage[element]
        deaths_element = deaths[element]
        tables.update({"Name": names_element, "Month": months_element, "Year": years_element, "Max Sustained Wind": sustained_element, "Areas Affected": affected_element, "Damage": damage_element, "Deaths": deaths_element})
        print(tables)
        break
table("Cuba II")
print()
# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
list_one_year = []
def one_year(year):
  for goda in range(len(years)):
    if years[goda] == year:
        months_element = months[goda]
        years_element = years[goda]
        sustained_element = max_sustained_winds[goda]
        affected_element = areas_affected[goda]
        damage_element = updated_damage[goda]
        deaths_element = deaths[goda]
        names_element = names[goda]
        list_one_year.append({"Name": names_element, "Month": months_element, "Year": years_element, "Max Sustained Wind": sustained_element, "Areas Affected": affected_element, "Damage": damage_element, "Deaths": deaths_element})
  print(list_one_year)
one_year(1932)
# 5
# Calculating Maximum Hurricane Count
print()
count = {}
def count_of_diseases(list):
  for element in list:
    for subelement in element:
      count[subelement] = 0
  for element in list:
    for subelement in element:
      count[subelement] += 1
  return count
print(count_of_diseases(areas_affected))
# find most frequently affected area and the number of hurricanes involved in
print()

# Write a function that finds the area affected by the most hurricanes, and how often it was hit.
def area_most_often():
  max_int = 0
  key_int = ""
  dict = {}
  for key, value in count.items():
    if value > max_int:
      max_int = value
      key_int = key
  dict[key_int] = max_int
  return dict
print(area_most_often())

# Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.
def greatest_number_of_deaths():
  the_most_dangerous_hurricane = ""
  the_most_biggest_killed = 0
  dict = {}
  for element in range(len(deaths)):
      if deaths[element] > the_most_biggest_killed:
        the_most_biggest_killed = deaths[element]
        the_most_dangerous_hurricane = names[element]
  dict[the_most_dangerous_hurricane] = the_most_biggest_killed
  return dict
print(greatest_number_of_deaths())


# Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.
damage_scale = {0: 0,
                1: 10,
                2: 100,
                3: 1000,
                4: 50000}
def scale():
  dict_scale = {}
  for element in range(len(deaths)):
    if element > 50000:
      dict_scale[names[element]] = 4
    elif element > 1000:
      dict_scale[names[element]] = 3
    elif element > 100:
      dict_scale[names[element]] = 2
    elif element > 10:
      dict_scale[names[element]] = 1
    else:
      dict_scale[names[element]] = 0
  return dict_scale
print(scale())

# Write a function that finds the hurricane that caused the greatest damage, and how costly it was.
def greatest_damage():
  greatest_loss = 0
  greatest_loss_name = ""
  dict_of_greatest_damage = {}
  for element in range(len(updated_damage)):
    if isinstance(updated_damage[element], float):
      if updated_damage[element] > greatest_loss:
        greatest_loss = int(updated_damage[element])
        greatest_loss_name = names[element]
  dict_of_greatest_damage[greatest_loss_name] = greatest_loss
  return dict_of_greatest_damage
print(greatest_damage())
print()
# Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.
def money_damage():
  money_dict = {}
  for element in range(len(deaths)):
    if isinstance(updated_damage[element], float):
      if updated_damage[element] > 50000000000:
        money_dict[names[element]] = 4
      elif element > 10000000000:
        money_dict[names[element]] = 3
      elif updated_damage[element] > 1000000000:
        money_dict[names[element]] = 2
      elif updated_damage[element] > 100000000:
        money_dict[names[element]] = 1
      else:
        money_dict[names[element]] = 0
  return money_dict
print(money_damage())

# Have a nice day!