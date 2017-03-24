import operator
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
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()
def main():
	print("THIS")
	print("IS")
	print("AN")
	print("RPN")
	print("CALCULATOR")
	while True:
		result = calculate(input('rpn calc> '))
		print("Result:", result)
if __name__ == '__main__':
	main()
