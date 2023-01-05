# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# COMPARE TERROTORIAL AREA
# The data from the website need to be edited, erase the (,) and (' ')
spain_total_area = 505307
switzerland_total_area = 41277
"""""
print(spain_total_area > switzerland_total_area)
"""""

# COMPARE POPULATION
spain_total_population = 47163418
switzerland_total_population = 8508698
"""""
print(spain_total_population > switzerland_total_population)
"""""

# COMPARE MOST SPOKEN LANGUAGE
spain_most_language = 'Spanish'
switzerland_most_language = 'German'
print(spain_most_language == switzerland_most_language)

# COMPARE MOST PREVALENT RELIGION
spain_religon_prevalent = 'Roman Catholic'
switzerland_religon_prevalent = 'Roman Catholic'
print(spain_religon_prevalent == switzerland_religon_prevalent)

# COMPARE LENGTH OF CAPITAL'S NAME
spain_capital_lenght = len('madrid')
switzerland_capital_lenght = len('bern')
print(spain_capital_lenght != switzerland_capital_lenght)

# COMPARE GOP IN BILLIONS OF EUR
spain_gop = 1714.860
switzerland_gop = 590.710
print(switzerland_gop > spain_gop)

# POPULATION GROWTH RATE
spain_population_growth = 0.13
switzerland_population_growth = 0.65
print(spain_population_growth and switzerland_population_growth < 1)

# POPULATION
print(spain_total_population > 10000000 or switzerland_total_population > 10000000)

# EXACTLY ONE THE COUNTRIES HAS A OPOPULATION COUNT OVER 10 MILLIONS
print(spain_total_population >
      10000000 or switzerland_total_population > 10000000 is True)
