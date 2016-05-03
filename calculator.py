import math

# constant
eCharge = 1.6e-19
eMass = 9.10938356e-31 #kg mass of electron
boltz = 1.38e-23
pi = math.pi
eps_0 = 8.854e-12 #F/m  permitivity of free space
mu_0 = 4e-7*pi #magnetic permeability   henries/meter
c_light = 3*10**8 #speed of light m/s
R_gas = 8.314 #Jmol^-1K^-1  ideal gas constant 
N_a = 6.02e23 #molecules/m avogadro constant
planck = 6.626e-34 #m^2 kg / s

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
def cos(a):
	return math.cos(a)
def sin(a):
	return math.sin(a)
def tan(a):
	return math.tan(a)
#rounding off function start
def sf(num): #return number
	sig = 5
	if num > 10**sig:
		return '%.4e'%num
	if num < 10**-sig:
		return '%.4e'%num

	#get the power
	power = math.floor(math.log10(num))
	#remove the power, reducing to x.xxxxx form
	sci = num*10**-power
	#trim away insignificant figure
	rounded = round(sci,sig-1)*10**power
	# return rounded*10**power
	return rounded

#integration function
def integration(lower, upper, integrand): #fundamental theory
	#case for even limit, odd integrand 
	if lower == -upper:
		if integrand(1) == -integrand(-1):
			return 0

	#normal case
	step = 1e-6
	incremented = step if lower == 0 else lower
	total = 0
	while incremented <= upper:	
		total += integrand(incremented)*step
		incremented += step

	return total 
def printPolar(real, imaginary):
	length = sqrt(real**2+imaginary**2)
	angle =  math.atan(imaginary/real)
	degree = angle*180/pi
	print(sf(length),"e^(j"+str((angle))+")",degree )

def collision(M,T,P):
	if M<1.17*T**P:
		print("False")
		return False
	else:
		print("True")
		return True
#---------------------------------------------------------------------------------
def cal():
	print(boltz*300/eCharge*1300)
# cal()

def sinkSort(alist): #lock onto on number and sink it to lowest
	for index in range(1, len(alist)):
		pos = index
		current = alist[index]
		while pos > 0 and alist[pos-1] > current:
			alist[pos] = alist[pos-1]
			pos = pos -1
		alist[pos] = current

def circularAntenna():
	S = 2
	W = 2
	kai = W/(W+S)
	k = math.tan(pi*kai/4)**2
	def integrand(t):
		a = 1 - t**2
		b = 1-k**2*t**2
		return div(1,sqrt(a*b))

	def cal():
		area = integration(0,1,integrand)
		print(area)
	cal()	
	
def pc2113t7q3():
	M_cd = 112.41 #gmol^-1
	M_se = 78.96 #gmol^-1
	w_cd = div(M_cd,M_cd+M_se)
	print('weight fraction of Cd =',sf(w_cd*100),'%')
	print('weight fraction of Se =', sf(100-w_cd*100),'%' )
def fizzBuzz(x,y,n):
    for i in range(1,n+1):
        if i%x == 0 and i%y == 0:
            print("Fizz Buzz")
        elif i%x == 0:
            print("Fizz")
        elif i%y == 0:
        	print("Buzz")
        else: 
        	print(i)

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
# pc2113t7q3()
def pc2113t7q2():
	M = 1.763
	B_ev = 7.442e-5 #eV nm^9
	m = 9
	r_0 = 0.357 #nm
	epsilon_o = epsilon_0*10**-9
	E_min = div(-eCharge*M,4*pi*epsilon_o*r_0)+B_ev/r_0**9
	print('ii =',sf(E_min),'eV')
# pc2113t7q2()
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
	AF = 152.4 #mm
	BC = 101.6 #mm
	DAE = 10 # degree
	FCA = math.atan(3)

	def print_length():
		print ("AF = ",AF,"mm")
		print ("BC = ",BC,"mm")
		print ("angle DAE = ",DAE," degree")
		print ("FE = ",AF*math.tan(0.5*DAE*pi/180)," mm")
		print("angle FCA =", FCA*180/pi,"degree")


	def print_ratio(initial, ratio, summ):
		incrementedValue = initial
		total = 0
		count = 1
		while total < summ:
			#add vertical to total
			total += incrementedValue
			#print out horizontal
			horizontal = total*2/3
			print(str(count)+".", "Horizontal =",horizontal,"   total =",total)
	
			#increment
			incrementedValue*=ratio
			count+=1

	print_board(board)
	print_length()
	print("\n")
	print_ratio(1,1.1,AF)
# designProject()
def inputImpedance():
	epsilon_r = 3.02
	c = 3e8 #speed of light
	h = 0.0004 #thick of dielectric in mm
	fr = 2.4e9
	w1 = 0.00005
	epsilon_reff = w1/h
	w1_eff = div(c,2*fr)*sqrt(div(2,epsilon_r+1))
	deltaL = h*0.412*div(epsilon_reff+0.3,epsilon_reff-0.258)*div(w1_eff/h+0.264,w1_eff/h+0.8)  #change in L
	L = div(1*c,2*fr*sqrt(epsilon_reff))-deltaL
	# T = 0.05 #thickness of copper in mm
	# fr = div(c,2*L*sqrt(epsilon_r))  #resonance frequency
	Zc = div(120*pi,sqrt(epsilon_reff)*( div(w1_eff,h)+1.393+0.667*ln(div(w1_eff,h)+1.444)))
	print("epsilon_reff = ",epsilon_reff)
	print("w1_eff = ",w1_eff)
	print( "input impedance = ",Zc)
# inputImpedance()

# find all permutation of a string
def stringPermutation():
	pass

def breadthFirstSearch():
	class Vertex:
		def __init__(self, name):
			self.name = name
			self.neightbors = list()

			self.distance = 9999
			slef.color = 'black'

		def add_neighbor(self,v):
			if v not in self.neightbors:
				self.neightbors.append(v)
				self.neightbors.sort()
	class Graph:
		vertices = {}

		def add_vertex(self,vertex):
			if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
				self.vertices[vertex.name] = vertex
				return True
			else:
				return False

def checkSf():
	array = [6844200000000.0,1e6,3e-2,2.35e+2,5.7E-1,1.23456789e-4]
	sig = 5
	for x in array:
		diff = div(x-float(sf(x)),x)
		print( diff  ) 
		
	# 	if math.floor(math.log10(x-sf(x))) != -sig:
	# 		print(i,"pops error")
	# 		break
	# print("No error")
# checkSf()


def printPoint():
	a = 5
	step = 100
	theta = 0
	counter = 0
	while counter < step:
		theta += 1/step
		r = a*theta
		print((math.cos(r)), math.sin(r))
		counter+=1
# printPoint()



def probabilityStack(array):
	noWin = 1
	for i in array:
		noWin *= (1-i)
	return 1-noWin
# initial = 0.01
# step = 0.03
# count = 0
# abc = []
# abc.append(initial)
# while(probabilityStack(abc)<0.90):
# 	initial+= step
# 	count += 1
# 	abc.append(initial)
# print(count)