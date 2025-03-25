import datetime
name = input("What is your name?\n")

age = int(input("How old are you going to turn this year? \n"))

currentYear = datetime.datetime.now().year

year = currentYear - age

def get_zodiac_animal(year):
    if year in [1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]:
        return "Rat"
    elif year in [1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021]:
        return "Ox"
    elif year in [1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022]:
        return "Tiger"
    elif year in [1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023]:
        return "Rabbit"
    elif year in [1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024]:
        return "Dragon"
    elif year in [1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025]:
        return "Snake"
    elif year in [1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026]:
        return "Horse"
    elif year in [1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027]:
        return "Goat"
    elif year in [1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028]:
        return "Monkey"
    elif year in [1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029]:
        return "Rooster"
    elif year in [1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030]:
        return "Dog"
    elif year in [1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031]:
        return "Pig"
    else:
        return "Unknown Zodiac"


animal = get_zodiac_animal(year)
print(f"Hello {name}, The Chinese Zodiac animal for the year {year} is {animal}.")