print "Welcome to the March Madness Predictor, 1.0"
print "_______________________"
print ""

# get data for team 1
t1 = str(raw_input("What is the first team?"))
ppg1 = float(raw_input("PPG?"))
opp_ppg1 = float(raw_input("OPP PPG?"))
assist1 = float(raw_input("ASSISTS?"))
rebound1 = float(raw_input("REBOUNDS?"))
ftp1 = float(raw_input("FREE THROW %? (IN DECIMAL FORM)"))
threep1 = float(raw_input("THREE POINT %? (IN DECIMAL FORM)"))
print ""

# get data for team 2
t2 = str(raw_input("What is the second team?"))
ppg2 = float(raw_input("PPG?"))
opp_ppg2 = float(raw_input("OPP PPG?"))
assist2 = float(raw_input("ASSISTS?"))
rebound2 = float(raw_input("REBOUNDS?"))
ftp2 = float(raw_input("FREE THROW %? (IN DECIMAL FORM)"))
threep2 = float(raw_input("THREE POINT %? (IN DECIMAL FORM)"))
print ""


# code to calculate percentages to add up
def percent_calc(n1, n2):
	x = 0
	if n1 != n2:
		x = (n1 - n2) / n2
		return x
	else:
		return x


# run percent_calc for every category
p1 = percent_calc(ppg1, ppg2)
p2 = percent_calc(opp_ppg1, opp_ppg2)
p3 = percent_calc(assist1, assist2)
p4 = percent_calc(rebound1, rebound2)
p5 = percent_calc(ftp1, ftp2)
p6 = percent_calc(threep1, threep2)

# add up percentages
total = 1*p1 + (-0.5)*p2 + 0.8*p3 + 0.5*p4 + 0.8*p5 + 0.8*p6

# total > 0 if in favor of t1, < 0 if in favor of t2
if total > 0:
	print t1 + " is more likely to win."

elif total < 0:
	print t2 + " is more likely to win."
else:
	print "Both teams are equally likely to win...flip a coin?"

print "\n"    