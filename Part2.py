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
            



