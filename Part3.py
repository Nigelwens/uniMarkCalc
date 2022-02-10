##functions
def checkRangeInt(credit):
    validation = True               ##return

    ##checking integer
    try:
        credit = int(credit)
    except ValueError:
        print("Integer required")
        validation = False

    ##checking range   
    if validation == True:
        if credit in range(0,121,20):
            return True
        else:
            print("Out of range")
            validation = False
    return validation

def histogram(stars):
    star = ""
    for i in range(stars):
        star += "*"
    return star

exclude = 0
retriever = 0
trailer = 0
progress = 0

##continue
cont = "y"
while cont != "q":
    ##total validation and loop
    validation = False
    while validation == False:
        
        ##pass validation and loop for false validation        
        while validation == False:
            crPass = input("Please enter your credit(s) at pass: ")
            validation = checkRangeInt(crPass)
        crPass = int(crPass)
          
        ##defer validation and loop for false validation
        validation = False   
        while validation == False:   
            crDefer = input("Please enter your credit(s) at defer: ")
            validation = checkRangeInt(crDefer)
        crDefer = int(crDefer)

        ##fail validation and loop for false validation
        validation = False    
        while validation == False: 
            crFail = input("Please enter your credit(s) at fail: ")
            validation = checkRangeInt(crFail)
        crFail = int(crFail)

        if crPass + crDefer + crFail != 120:
            print("Total incorrect")
            validation = False
        else:
            ##progression outcome
            if(crFail > 60):
                print("Exclude")
                exclude += 1
            elif(crPass < 100):
                print("Do not Progress - module retriever")
                retriever +=1
            elif(crPass < 120):
                print("Progress(module trailer)")
                trailer +=1
            else:
                print("Progress")
                progress +=1
            cont = input("Would you like to enter another set of data? \nEnter \'y\' for yes or \'q\' to quit and view results: ")

##histogram
print("\nHorizontal Histogram")
print("Progress {}  : {}".format(progress, histogram(progress)))
print("Trailer {}   : {}".format(trailer, histogram(trailer)))
print("Retriever {} : {}".format(retriever, histogram(retriever)))
print("Excluded {}  : {}".format(exclude, histogram(exclude)))
print("\n {} outcome(s) in total.".format(progress+trailer+retriever+exclude))






