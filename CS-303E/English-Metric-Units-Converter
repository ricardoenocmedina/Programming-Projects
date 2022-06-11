ERRORMESSAGE = "\nERROR: Answer must be 1, 2 or 3. Try again."
QUITMESSAGE = "\nThanks for using our convertor. Goodbye!"
SPACE = "\n------------------------------------------------------------\n"
ONE = "1"
TWO = "2"
THREE = "3"
kilometer = 1.609

# This chunk of code is the header
print("\nWelcome to the English/Metric conversion utility.")
print("This utility allows you to convert between English units\n(miles, feet, inches) and metric units (kilometers, meters,\ncentimeters).")

while True:
    
    print(SPACE)
    # What direction to convert?
    print("Which direction would you like to convert:")
    print("   For English to Metric type:  1")
    print("   For Metric to English type:  2")
    print("   To Quit type:                3")
    userInputMain = input("\n   Input your answer (1, 2 or 3): ")

    # This branch of code is concerned with converting from English to Metric
    if userInputMain == ONE:
        print("\nSelect English units to convert to metric equivalent:")
        print("   For miles type:  1")
        print("   For feet type:   2")
        print("   For inches type: 3")
        userInput1 = input("\n   Chose English units to convert (1, 2 or 3): ")

        # Converts from miles to either kilometers, meters or centimeters
        if userInput1 == ONE:
            print("\nConvert to which metric units:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3")
            userInput1point1 = input("\n   Chose target metric units(1, 2 or 3): ")

            if userInput1point1 == ONE:
                userInput1point1point1 = eval(input("\nEnter the number of miles to convert to kilometers: "))
                calculation = userInput1point1point1 * kilometer

                userInput1point1point1 = format(userInput1point1point1, "0.1f")
                calculation = format(calculation, "0.3f")

                print("\nRESULT:", userInput1point1point1, "miles =", calculation, "kilometers")
                continue

            if userInput1point1 == TWO:
                userInput1point1point2 = eval(input("\nEnter the number of miles to convert to meters: "))
                calculation2 = userInput1point1point2 * kilometer * 1000

                userInput1point4 = format(userInput1point1point2, "0.1f")
                calculation2 = format(calculation2, "0.3f")

                print("\nRESULT:", userInput1point1point2, "miles =", calculation2, "meters")
                continue
            
            if userInput1point1 == THREE:
                userInput1point1point3 = eval(input("\nEnter the number of miles to convert to centimeters: "))
                calculation3 = userInput1point1point3 * kilometer * 100000

                userInput1point1point3 = format(userInput1point1point3, "0.1f")
                calculation3 = format(calculation3, "0.3f")

                print("\nRESULT:", userInput1point1point3, "miles =", calculation3, "centimeters")
                continue
                        
        # Converts from feet to either kilometers, meters or centimeters
        if userInput1 == TWO:
            print("\nConvert to which metric units:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3")
            userInput1point2 = input("\n   Chose target metric units(1, 2 or 3): ")
            
            if userInput1point2 == ONE:
                userInput1point2point1 = eval(input("\nEnter the number of feet to convert to kilometers: "))
                calculation4 = userInput1point2point1 * 0.0003048

                userInput1point2point1 = format(userInput1point2point1, "0.1f")
                calculation4 = format(calculation4, "0.3f")

                print("\nRESULT:", userInput1point2point1, "feet =", calculation4, "kilometers")
                continue

            if userInput1point2 == TWO:
                userInput1point2point2 = eval(input("\nEnter the number of feet to convert to meters: "))
                calculation5 = userInput1point2point2 * 0.3048

                userInput1point2point2 = format(userInput1point2point2, "0.1f")
                calculation5 = format(calculation5,"0.3f")

                print("\nRESULT:", userInput1point2point2, "feet = ", calculation5, "meters")
                continue

            if userInput1point2 == THREE:
                userInput1point2point3 = eval(input("\nEnter the number of feet to convert to centimeters: "))
                calculation6 = userInput1point2point3 * 30.48

                userInput1point2point3 = format(userInput1point2point3, "0.1f")
                calculation6 = format(calculation6, "0.3f")

                print("\nRESULT:",userInput1point2point3,"feet =",calculation6, "centimeters")
                continue
        # Converts from inches to either kilometers, meters or centimeters
        if userInput1 == THREE:
            print("\nConvert to which metric units:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3")
            userInput1point3 = input("\n   Chose target metric units(1, 2 or 3): ")

            if userInput1point3 == ONE:
                userInput1point3point1 = eval(input("\nEnter the number of inches to convert to kilometers: "))
                calculation7 = userInput1point3point1 * 2.45e-5

                userInput1point3point1 = format(userInput1point3point1, "0.1f")
                calculation7 = format(calculation7, "0.3f")

                print("\nRESULT:", userInput1point3point1, "inches =", calculation7, "kilometers")
                continue

            if userInput1point3 == TWO:
                userInput1point3point2 = eval(input("\nEnter the number of inches to convert to meters: "))
                calculation8 = userInput1point3point2 * 0.0254

                userInput1point3point2 = format(userInput1point3point2, "0.1f")
                calculation8 = format(calculation8, "0.3f")

                print("\nRESULT:", userInput1point3point2, "inches =", calculation8, "meters")
                continue

            if userInput1point3 == THREE:
                userInput1point3point3 = eval(input("\nEnter the number of inches to convert to centimeters: "))
                calculation9 = userInput1point3point3 * 2.54

                userInput1point3point3 = format(userInput1point3point3, "0.1f")
                calculation9 = format(calculation9, "0.3f")

                print("\nRESULT:", userInput1point3point3, "inches =", calculation9, "centimeters")
                continue
       
                
    # This branch of code is concerned with converting from Metric to English 
    if userInputMain == TWO:
        print("\nSelect metric units to convert to English equivalent:")
        print("   For kilometers type:  1")
        print("   For meters type:      2")
        print("   For centimeters type: 3")
        userInput2 = input("\n   Chose metric units to convert (1, 2 or 3): ")

        # Converts from kilometers to either miles, feet or inches
        if userInput2 == ONE:
            print("\nConvert to which Englsih units:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            userInput2point1 = input("\n   Choose metric units to convert (1, 2 or 3): ")

            if userInput2point1 == ONE:
                userInput2point1point1 = eval(input("\nEnter the number of kilometers to convert to miles: "))
                calculation10 = userInput2point1point1 * .621371

                userInput2point1point1 = format(userInput2point1point1, "0.1f")
                calculation10 = format(calculation10, "0.3f")
                
                print("\nRESULT:", userInput2point1point1, "kilometers =", calculation10, "miles")
                continue

            if userInput2point1 == TWO:
                userInput2point1point2 = eval(input("\nEnter the number of kilometers to convert to feet: "))
                calculation11 = userInput2point1point2 * 3280.84

                userInput2point1point2 = format(userInput2point1point2, "0.1f")
                calculation11 = format(calculation11, "0.3f")

                print("\nRESULT:", userInput2point1point2, "kilometers =", calculation11, "feet")
                continue

            if userInput2point1 == THREE:
                userInput2point1point3 = eval(input("\nEnter the number of kilometers to convert to inches: "))
                calculation12 = userInput2point1point3 * 39370.1

                userInput2point1point3 = format(userInput2point1point3, "0.1f")
                calculation12 = format(calculation12, "0.3f")

                print("\nRESULT:", userInput2point1point3, "kilometers =", calculation12, "inches")
                continue
        # Converts from meters to either miles, feet or inches
        if userInput2 == TWO:
            print("\nConvert to which English units:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            userInput2point2 = input("\n   Choose metric units to convert (1, 2 or 3): ")

            if userInput2point2 == ONE:
                userInput2point2point1 = eval(input("\nEnter the number of meters to convert to miles: "))
                calculation13 = userInput2point2point1 * 0.000621371

                userInput2point2point1 = format(userInput2point2point1, "0.1f")
                calculation13 = format(calculation13, "0.3f")

                print("\nRESULT:", userInput2point2point1, "meters =", calculation13, "miles")
                continue

            if userInput2point2 == TWO:
                userInput2point2point2 = eval(input("\nEnter the number of meters to convert to feet: "))
                calculation14 = userInput2point2point2 * 3.2808

                userInput2point2point2 = format(userInput2point2point2, "0.1f")
                calculation14 = format(calculation14, "0.3f")

                print("\nRESULT:",userInput2point2point2, "meters =", calculation14, "feet")
                continue
            
            if userInput2point2 == THREE:
                userInput2point2point3 = eval(input("\nEnter the number of meters to convert to inches: "))
                calculation15 = userInput2point2point3 * 39.3701

                userInput2point2point3 = format(userInput2point2point3, "0.1f")
                calculation15 = format(calculation15, "0.3f")

                print("\nRESULT:", userInput2point2point3, "meters =", calculation15, "inches")
                continue

        # Converts from centimeters to either miles, feet or inches
        if userInput2 == THREE:
            print("\nConvert to which English units:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            userInput2point3 = input("\n   Choose metric units to convert (1, 2 or 3): ")

            if userInput2point3 == ONE:
                userInput2point3point1 = eval(input("\nEnter the number of centimeters to convert to miles: "))
                calculation16 = userInput2point3point1 * 6.21371e-6

                userInput2point3point1 = format(userInput2point3point1, "0.1f")
                calculation16 = format(calculation16, "0.3f")

                print("\nRESULT:", userInput2point3point1, "centimeters =", calculation16,"miles")
                continue

            if userInput2point3 == TWO:
                userInput2point3point2 = eval(input("\nEnter the number of centimeters to convert to feet: "))
                calculation17 = userInput2point3point2 * 0.0328084

                userInput2point3point2 = format(userInput2point3point2, "0.1f")
                calculation17 = format(calculation17, "0.3f")

                print("\nRESULT:", userInput2point3point2, "centimeters =", calculation17, "feet")
                continue

            if userInput2point3 == THREE:
                userInput2point3point3 = eval(input("\nEnter the number of centimeters to convert to inches: "))
                calculation18 = userInput2point3point3 * .393701

                userInput2point3point3 = format(userInput2point3point3, "0.1f")
                calculation18 = format(calculation18, "0.3f")

                print("\nRESULT:", userInput2point3point3, "centimeters =", calculation18, "inches")
                continue

    # Kills the program
    if userInputMain == THREE:
        print(QUITMESSAGE)
        break
    
    # Edge case if input is not 1, 2 or 3
    if userInputMain != ONE or userInputMain != TWO or userInputMain != THREE:
        print(ERRORMESSAGE)
        continue
