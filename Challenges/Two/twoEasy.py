#simple interest calculator

def simpleInterest(principle, rate, time): 
    return principle * rate * time

principle =float(raw_input("Principle: "))

rate = float(raw_input("Rate: "))

time = float(raw_input("Times Interest is calculated: ")) 

interest = simpleInterest(principle, rate, time)

compoundPrinciple = compoundInterest(principle, rate, time);

print "Amount of interest: " + str(interest)
print "Total owed: " + str(interest + principle)
