# Problem 5: Discovering Planets

# Goal: Check if a planet is habitable or not

def main():
    
    n = int(input())

    for i in range(n):

        temp, withWater, withField, eccen = input().split(" ")
        temp = float(temp)
        withWater = boolean_parser(withWater)
        withField = boolean_parser(withField)
        eccen = float(eccen)

        print(test_planet(temp, withWater, withField, eccen))

def boolean_parser(strBool):
    
    return False if strBool.lower() == "false" else True

def test_planet(temp, withWater, withField, eccen):
    """Determine whether a planet is habitable or not"""

    if temp > 100:
        return "The planet is too hot."
    
    elif temp < 0:
        return "The planet is too cold."
    
    elif not withWater:
        return "The planet has no water."
    
    elif not withField:
        return "The planet has no magnetic field."
    
    elif eccen > 0.6:
        return "The planet's orbit is not ideal."
    
    else:
        return "The planet is habitable."

main()