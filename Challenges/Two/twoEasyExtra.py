#interest calculator

def simpleInterest(principle, rate, time): 
    return principle * rate * time

def compoundInterest(principle, rate, cycles):
    return principle*((1 + rate)**cycles-1)

principle =float(raw_input("Principle: "))

rate = float(raw_input("Rate: "))

time = float(raw_input("Times Interest is calculated: ")) 

interest = simpleInterest(principle, rate, time)

compoundInterest = compoundInterest(principle, rate, time);

print "Amount of interest: " + str(interest)
print "Total owed: " + str(interest + principle)

print "Compound Interest: " + str(compoundInterest)
print "Total owed: " + str(compoundInterest + principle)
