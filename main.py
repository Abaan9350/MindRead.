#Raihan, Vedant Shetty, Ganesh, Abaan, Aryan, Dipesh

option = input("Is your character a boy?\n")
if option == "yes":
    option = input("Does he wear spectacles?\n")
    if option == "yes":
        option = input("Is he scolded in class?\n")
        if option == "yes":
            option = input("Does he invest in stock market?\n")
            if option == "yes":
                option = input("Does he have a cat?\n")
                if option == "yes":
                    print("You are thinking of Raihan!")
                else:
                    option = input("Is he good at driving?\n")
                    if option == "yes":
                        print("You are thinking of Vedant Shetty")
                    else:
                        print("You are thinking of Ganesh!")
            else:
                option = input("Does he go the gym?\n")
                if option == "yes":
                    option = input("Does he sleep in class regularly?\n")
                    if option == "yes":
                        option = input("Is he good at video games?\n")
                        if option == "yes":
                            print("You are thinking of Anish Masurkar!")
                else:
                    option = input("Does he wear shirts regularly?\n")
                    if option == "yes":
                        option = input("Nashik?\n")
                        if option == "yes":
                            print("You are thinking of Akshar!")
                        else:
                            option = input("Is he good at chess?\n")
                            if option == "yes":
                                print("You are thinking of Shreyash!")
        else:
            option = input("Is he really good at maths?\n")
            if option == "yes":
                print("You are thinking of Ashish!")
            else:
                option = input("Is he good at football?\n")
                if option == "yes":
                    print("You are thinking of Soham Desai!")
                else:
                    option = input("Does he go the gym?\n")
                    if option == "yes":
                        option = input("Does he sleep in class regularly?\n")
                        if option == "yes":
                            option = input("Is he good at video games?\n")
                            if option == "yes":
                                print("You are thinking of Anish Masurkar!")
                    else:
                        option = input("Does he wear shirts regularly?\n")
                        if option == "yes":
                            option = input("Nashik?\n")
                            if option == "yes":
                                print("You are thinking of Akshar!")

    else:
        option = input("Does he get scolded in class?\n")
        if option == "yes":
            option = input("Does he wear shirts usually? \n")
            if option == "yes":
                option = input("")
            else:
                option = input("Is he good at football?\n")
                if option == "yes":
                    option = input("Is he known for his hair?\n")
                    if option == "yes":
                        print("You are thinking of Aryan!")
                    else:
                        option = input("is he South Indian?\n")
                        if option == "yes":
                            print("You are thinking of Dipesh!\n")
                        else:
                            print("You are thinking of Abaan!\n")
                else:
                    option = input("Is he known for his hair?\n")
                    if option == "yes":
                        print("You are thinking of Aryan!")
        else:
            option = input("Does he help everyone with assignments?\n")
            if option == "yes":
                print("You are thinking of Sameer!")
            else:
                option = input("Does he have interest in cameras?\n")
                if option == "yes":
                    option = input("Is he good at video games?\n")
                    if option == "yes":
                        print("You are thinking of Amruthesh!")
                else:
                    option = input("Good at video games?\n")
                    if option == "yes":
                        option = input("Autistic?\n")
                        if option == "yes":
                            print("You are thinking of Uday!")
                    else:
                        option = input("Is he really good at football?\n")
                        if option == "yes":
                            print("You are thinking of Sai!")

else: #this is for lediz
    option = input("Does she wear spectacles?\n")
    if option == "yes":
        option = input("Is she in any college clubs?\n")
        if option == "yes":
            option = input("Does she go to the gym?\n")
            if option == "yes":
                print("You are thinking of Kavya!")
            else:
                option = input("Is she good in academics?\n")
                if option == "yes":
                    option = input("Extrovert?")
                    if option == "yes":
                        option = input("Is she known for singing?\n")
                        if option == "yes":
                            option = input("Is she in the college choir team?\n")
                            if option == "yes":
                                print("You are thinking of Janaki!")
                            else:
                                print("You are thinking of Vedshri!")
                        else:
                            print("You are thinking of Vedshri!")
        else: #this is for not in college clubs
            option = input("Is she good in academics?\n")
            if option == "yes":
                option = input("Does she have a pet fish?\n")
                if option == "yes":
                    print("You are thinking of Ketki!")
                else: #not a pet fish
                    option = input("Extrovert?\n")
                    if option == "yes":
                       print("")
                    else:
                        print("You are thinking of Aastha!")

    else:
        option = input("Is she in any college clubs?\n")
        if option == "yes":
            option = input("Is she known for singing?\n")
            if option == "yes":
                option = input("Is she good in academics? \n")
                if option == "yes":
                    option = input("")

        else:
            option = input("Does she have a pet cat?\n")
            if option == "yes":
                print("You are thinking of Fareen!")
            else:
                option = input("Extrovert?\n")
                if option == "yes":
                    print("You are thinking of Archi!")