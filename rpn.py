import operator
import readline
import colorama
from colorama import Fore, Back, Style
OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod,
	'~': operator.inv,
	'|': operator.abs,
	'n': operator.neg,
	'p': operator.pos,
	'<': operator.lt,
	'>': operator.gt,
	'=': operator.eq,
}
def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)

		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			print(Back.BLUE + Fore.YELLOW,arg2, arg1)
			operator_fn = OPERATORS[operand]
			print(Back.YELLOW + Fore.BLUE + str(operator_fn))
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()
def main():
	print(Fore.RED + "THIS")
	print(Fore.GREEN + "IS")
	print("AN")
	print(Fore.BLUE + "RPN")
	print("CALCULATOR")
	while True:
		result = calculate(input('rpn calc> '))
		print(Style.RESET_ALL)
		print("Result:", result)

if __name__ == '__main__':
	main()
