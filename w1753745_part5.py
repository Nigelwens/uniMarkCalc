##functions


def histogram(stars):
    star = ""
    for i in range(stars):
        star += "*"
    return star

starList = [0,0,0,0]
dataList = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

##datalist loop
for i in range(len(dataList)):
    ##data entery
    crPass = dataList[i][0]
    crDefer = dataList[i][1]
    crFail = dataList[i][2]
    
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
            

##horizontal histogram
print("\nHorizontal Histogram")
print("Progress  {}: {}".format(starList[0], histogram(starList[0])))
print("Trailer   {}: {}".format(starList[1], histogram(starList[1])))
print("Retriever {}: {}".format(starList[2], histogram(starList[2])))
print("Excluded  {}: {}".format(starList[3], histogram(starList[3])))
print("\n{} outcome(s) in total.".format(starList[0]+starList[1]+starList[2]+starList[3]))





            




