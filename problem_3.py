##Problem Set 3
#Name: Arianna O'Brien Cannon
#Time Spent: 20 mins
#Last Modified: 9/23/19


#def main
def main ():
	#create empty dictionary
	empty_dict = {}
	#make actual dictionary
	dict_1 = {'Jeff Bezos & family':160, 'Bill Gates':97, 'Warren Buffett':88.3, 'Mark Zuckerberg':61, 'Larry Ellison':58.4, 'Larry Page':53.8, 'Charles Koch':53.5}
	#update empty dictionary to actual dictionary
	(empty_dict.update(dict_1))
	#for statement
	for key in empty_dict:
		#print keys
		print(key)
	#print values
	print(empty_dict.values())


if __name__ == '__main__':
	main()