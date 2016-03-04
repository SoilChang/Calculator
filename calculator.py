import math

# constant
eCharge = 1.6e-19
boltz = 1.38e-23
pi = math.pi
espilon_0 = 8.854e-12 #F/m  permitivity of free space

# divide function
def div(a,b):
	return a/b
# exponential function
def exp(a):
	return math.exp(a)
# square root
def sqrt(a):
	return math.sqrt(a)
# ln function
def ln(a):
	return math.log(a)
#rounding off function start
def sf(number): #return number
	sf = 5
	count = 0
	reached_e = False
	string = str(number)
	rounded = ""
	for x in string:
		# checking if it is "e"
		if x != "e":
			if x in '1234567890' :
				# if the x is a number
				count += 1
			if count <= sf or reached_e:
				# if count sf has been reached, or if it is after "e"
				rounded += x
		else:
			rounded += x
			reached_e = True
	# return rounded #as string
	try:
		num = float(rounded)
		return(num)
	except:
		print("unable to conver number string back to number")
#integration function
def integration(lower, upper, integrand): #fundamental theory
	step = 2**-15
	incremented = step if lower == 0 else lower
	total = 0
	while incremented <= upper:	
		total += integrand(incremented)*step
		incremented += step

	return total 


def cs2107():
	def secondToMinute(x):
		return x/60
	cyclePerSec = 4*2e30
	tryPerSec = cyclePerSec/512
	totalTime = 2**32/tryPerSec
	print(secondToMinute(totalTime))
	# print(1.17*100000**0.1)
	print(1e9-2e30)
# cs2107()


def pc2133T4Q1():
	Na = 1e23 #m^-3
	Nd = 5e21 #m^-3
	Vbi = 0.736 #v
	epsilon_r = 11.7
	epsilon_si = espilon_0*epsilon_r #in meter
	#d)
	Xn = div(1,Nd)*sqrt(div(2*epsilon_si*Vbi*Na*Nd, eCharge*(Na+Nd)))
	print('d)'+ sf(Xn))
# pc2133T4Q1()


def designProject():
	
	board = []
	rowNumber = 13
	colNumber = 30
	for x in range(rowNumber): #  rows
	    board.append([" "] * colNumber) # column

	def print_board(board):
	    for row in board:
	        print (" ".join(row))
	
	def setBoundary(currentR,currentC, symbol):
		try:
			board[currentR][currentC] = symbol
		except IndexError:
			print(" alert: index out of range")
			

	def setTriangle(startRow,startCol,height):
		startCol = height if startCol<height else startCol
		startR = startRow
		startC = startCol
		height = height
		currentR = startR
		currentC = startC
		#set first point
		setBoundary(currentR,currentC,'/')
		#set point A
		setBoundary(currentR-1,currentC,'A')
		#draw left slope
		for i in range(height-1):
			currentR +=1
			currentC -=1
			setBoundary(currentR,currentC,'/')
		#set point B,C,D,E,F
		quater_length = math.ceil((height+1)/2)
		pointC = currentC+height*2
		setBoundary(currentR+1,currentC-1,'B')
		setBoundary(currentR+1,pointC,'C')
		setBoundary(currentR+1,startC,'F')
		setBoundary(currentR+1,currentC-1+quater_length,'D')
		setBoundary(currentR+1,pointC-quater_length,'E')
		
		#draw bottom line
		for i in range(height*2-1):
			currentC +=1
			setBoundary(currentR,currentC,'_')
		#set right vertices
		setBoundary(currentR,currentC,'\\')
		#set point C
		#draw right slope
		for i in range(height-1):
			currentR -=1
			currentC -=1
			setBoundary(currentR,currentC,'\\')	
	setTriangle(1,8,10)	



	#set length
	AF = 300 #mm
	BC = 200 #mm
	DAE = 10 # degree
	
	def print_length():
		print ("AF = "+str(AF)+" mm")
		print ("BC = "+str(BC)+" mm")
		print ("angle DAE = "+str(DAE)+" degree")
		print ("FE = "+str(sf(AF*math.tan(0.5*DAE*pi/180)))+" mm")


	def print_ratio(step, initial, ratio, summ):
		incrementedValue = initial
		total = 0
		for x in range(0,step):
			incrementedValue = initial*ratio**x
			total += incrementedValue
			if summ <= total:
				break
			print( str(x+1)+". "+str(round(incrementedValue,2))+ " mm\n  total length= "+str(round(total,2))+"mm")

	print_board(board)
	print_length()
	print("\n")
	print_ratio(100,5,1.1,AF)
# designProject()

