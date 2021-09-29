#Problem Set 2
#Name: Arianna O'Brien Cannon
#Time Spent: 20 mins
#Last Modified: 9/23/19

#def main
def main ():
	#def range, start stop and incrementation
	a = list(range(1,22,1))
	#def odd
	odd = (1,3,5,7,9,11,13,15,17,19)
	# print reversed
	print(list(a[::-1]))
	# print a range within range
	print(a[2:7])
	#for loop to search for odd numbers
	for number in a:
		if (number in odd):
			print("odd")


if __name__ == '__main__':
	main()