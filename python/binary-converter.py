class Stack(object):
	def __init__(self):
		self.__stacklist = []
	def isEmpty(self):
		return len(self.__stacklist) ==0
	def push(self,p):
		self.__stacklist.append(p)
	def pop(self):
		return self.__stacklist.pop()	
	def printStack(self):
		print self.__stacklist
	def returnList(self):
		return self.__stacklist


def decimalToBinary(decimal):
	binaryStack = Stack()
	tempDecimal = decimal
	while (tempDecimal > 0):
		remainder = tempDecimal % 2
		binaryStack.push(remainder)
		tempDecimal = tempDecimal // 2
	print  "Converting %s into binary : %s " % (decimal, str(list(reversed(binaryStack.returnList()))))

def binaryToDecimal(binary):
	binaryList = [ int(x) for x in str(binary)]  
	decimalNumber = 0 
	numberOfDigits = len(binaryList) - 1
	for digit in binaryList:
		decimalNumber += digit * 2**numberOfDigits
		numberOfDigits -= 1
	print  "Converting %s into decimal : %s " % (binary,decimalNumber)

def main():
	decimalToBinary(756)
	binaryToDecimal(110101001)
	
if __name__ == '__main__' :
	main()

