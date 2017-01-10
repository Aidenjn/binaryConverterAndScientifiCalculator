#######################################################################
# Program Filename: assignment5
# Author: Aiden Nelson
# Date: 10/22/2016
# Description: Will convert decimal numbers of any size into binary numbers. Will also function as a basic calculator.
# Input: Decimal number or operands.
# Output: Binary number or operands output.
######################################################################

#######################################################################
# Function: numCheck
# Description: Will make sure that the number recieved is a positive integer.
# Parameters:
# Return values: 1 - incorrect value, 2 - correct value
# Pre-Conditions:
# Post-Conditions:
#######################################################################
def numCheck(inputString):
	incorrectCount = 0;
	characters = list(str(inputString));
	for x in range(0,len(characters)):
		for y in range(48,58):
			if characters[x] == chr(y):
				break;
			else:
				incorrectCount = incorrectCount + 1;
		if incorrectCount > 9:
			print("I can't take your input. Please try again.");
			return 1;
			break;
		else:
			incorrectCount = 0;
	return 0;

#######################################################################
# Function: binaryConverter
# Description: Will convert a positive decimal integer into a binary output.
# Parameters:
# Return values: binary number
# Pre-Conditions:
# Post-Conditions:
#######################################################################
def binaryConverter():
	correctNumber = 1;
	decimalNumber = input('Please input the number that you wish to convert into binary: ');
	correctNumber = numCheck(decimalNumber);
	while (correctNumber != 0):
		decimalNumber = input();
		correctNumber = numCheck(decimalNumber);
	
	decimalNumber = int(decimalNumber);
	binaryNumber = str("");
	startNum = 0; # For checking when to start writing the binary number
	
	divisNumber = 2;
	counter = 0;
	while (divisNumber <= decimalNumber):
		divisNumber = 2;
		divisNumber = divisNumber**counter;
		counter = counter + 1;
	x = 0;
	for x in range(0, counter):
		if decimalNumber >= divisNumber:
			decimalNumber = decimalNumber - divisNumber;
			binaryNumber = binaryNumber + '1';
			startNum = 1;
		else:
			if startNum == 1:
				binaryNumber = binaryNumber + '0';
	
		divisNumber = divisNumber / 2;
	
	print('The binary conversion is: ' + binaryNumber);
	return 0;

def decimalConverter():
	binaryNumber = input('Please input a binary number that you wish to convert: ');
	binaryArray = list(binaryNumber);
	print(binaryArray);
	return 0;
#######################################################################
# Function: sCalculator
# Description: a basic two operand calculator 
# Parameters: 
# Return values: the output of the inputed variables
# Pre-Conditions:
# Post-Conditions:
#######################################################################
def sCalculator():
	op1 = float(input("First operand: "));
	op = str(input("Operator: "));
	op2 = float(input("Second operand: "));
	ans = 0;
	if (op == "+"):
		ans = op1 + op2;
	elif (op == "-"):
                ans = op1 - op2;
	elif (op == "*"):
                ans = op1 * op2;
	elif (op == "/"):
                ans = op1 / op2;
	elif (op == "**"):
                ans = op1 ** op2;
	print("The output is " + str(ans));

	return 0;

exitProg = 0;
exitVar = 1;
choice = 0;
choice2 = 0;
#choice = int(input("Type 1 if you would like to enter programmer mode or 2 if you would like to enter the scientific calculator mode(you can also type 3 to exit the program)!!! "));

while (exitProg != 1):
	choice = int(input("Type 1 if you would like to enter programmer mode or 2 if you would like to enter the scientific calculator mode(you can also type 3 to exit the program)!!! "));
	if choice == 1:
			while (exitVar == 1):
				#choice2 = int(input("Would you like to convert decimal to binary(type 1
				binaryConverter();
				exitVar = int(input("Would you like to convert another decimal to binary? (type 1 for yes or 2 for no) "));
	elif choice == 2:
			while (exitVar == 1):
				sCalculator();
				exitVar = int(input("Would you like to keep calculating? (type 1 for yes or 2 for no) "));
	elif choice == 3:
				exitProg = 1;
	else:
				print("That wasn't a correct input ya hooligan!");
	
	exitVar = 1;
	#choice = int(input("Type 1 if you would like to enter programmer mode or 2 if you would like to enter the scientific calculator mode(you can also type 3 to exit the program)!!! "));
