crPass = int(input("Please enter your credit(s) at pass: "))
crDefer = int(input("Please enter your credit(s) at defer: "))
crFail = int(input("Please enter your credit(s) at fail: "))

if(crFail > 60):
    print("Exclude")
elif(crPass < 100):
    print("Do not Progress - module retriever")
elif(crPass < 120):
    print("Progress(module trailer)")
else:
    print("Progress")


