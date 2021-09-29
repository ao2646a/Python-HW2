#Problem Set 4
#Name: Arianna O'Brien Cannon
#Time Spent: 10 mins
#Last Modified: 9/23/19

#define main
def main ():
	#variables
	P = 1500
	r = .043
	t = 6
	n = 4
	#formula
	A = (P*(1+(r/n))**(n*t))
	#total paid is zero, haven't paid anything yet
	total_paid = 0
	#while statement
	while(total_paid < (A*n)):
		#print statement
		print(total_paid)
		#count statement (incrementing)
		total_paid+=A

if __name__ == '__main__':
	main()