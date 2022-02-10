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

starList = [0,0,0,0]
print("-"*63,"\nStaff Version with Histogram")
##continue
cont = "y"
while cont != "q":
    ##total validation and loop
    validation = False
    while validation == False:
        
        ##pass validation and loop for false validation        
        while validation == False:
            crPass = input("\nPlease enter your credit(s) at pass: ")
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
                starList[3] += 1  
            elif(crPass < 100):
                print("Do not Progress - module retriever")
                starList[2] += 1 
            elif(crPass < 120):
                print("Progress(module trailer)")
                starList[1] += 1 
            else:
                print("Progress")
                starList[0] += 1 
            cont = input("\nWould you like to enter another set of data? \nEnter \'y\' for yes or \'q\' to quit and view results: ")
            

##horizontal histogram
print("-"*63)
print("Horizontal Histogram")
print("Progress {}  : {}".format(starList[0], histogram(starList[0])))
print("Trailer {}   : {}".format(starList[1], histogram(starList[1])))
print("Retriever {} : {}".format(starList[2], histogram(starList[2])))
print("Excluded {}  : {}".format(starList[3], histogram(starList[3])))
print("\n{} outcome(s) in total.".format(starList[0]+starList[1]+starList[2]+starList[3]))
print("-"*63)
##vertical histogram
print("Progress",starList[0]," | Trailer",starList[1]," | Retriever",starList[2]," | Excluded",starList[3])
for i in range(max(starList)): ##rows
    for t in range(len(starList)): ##columns
        if starList[t] >= i+1:
            print(" "*3, "*"," "*7, end=" ")
        else:
            print(" "*13, end=" ")
    print()
print("\n{} outcome(s) in total.".format(starList[0]+starList[1]+starList[2]+starList[3]))
print("-"*63)


            




