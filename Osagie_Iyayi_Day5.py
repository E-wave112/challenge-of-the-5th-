#faithful numbers
print('Ciao')
def faithful(n):
	'''
	this function is aimed at finding the value of a faithful number within a given position
	'''
	n>0
	x = str(int(bin(n)[2:]))
	y = x[::-1]
	f = 0
	p = 0
	for i in y :
		t = int(i)*7**f
		f = f + 1
		p = p + t
	return str(p) +  ' is our faithful number in this case'


n = int(input('Enter number : '))
print(faithful(n))
print('Molto grazie, ci vediamo dopo!')