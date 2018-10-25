# By: Marcos Gil

def factorial(num): # Function to calculate the factorial of a number using recursion
	
	if (num == 1) or (num == 0):
		return 1
	else:
		return (num*factorial(num-1))	

def combination(row, column): # Function that does the provided combination equation on the Assignment Outline

	return (factorial(row)) / ((factorial(column)) * (factorial(row-column)))
	
def userInput(): # Function for getting the user input and also making sure they don't enter 0 or a negative integer, and restricting the input to integers
	
	while True:
		try:
			userNum = int(input("What number would you like find in Pascals' Triangle? "))
			
			while userNum <= 0:
				print('Sorry, you can only enter an integer above 0. Please try again. ')
				userNum = int(input("What number would you like find in Pascals' Triangle? "))
			break
		
		except:
			print('Floats/characters are not allowed to be entered. Please try again. ')
			continue

	return userNum
			
def findRow(userNum, row): # Function for going through the rows using recursion
	
	for column in range(row + 1):
		if userNum == combination(row, column):
			return row
	return findRow(userNum, row + 1)
	
def pascalTriangle(row): # Function for creating a list that contains the values of Pascals' Triangle that will be printed out
	
	triangleList = []
	for x in range(row):
		rows = []
		for y in range(x + 1): 
			rows.append(combination(x, y))
		triangleList.append(rows)
    
	return triangleList

	
def trianglePrint(triangleList): # Function that goes through the list created in pascalTriangle and prints it out as a string so that the center function can be used
	for x in triangleList:
		pascalLine = []
		for y in x:
			y = int(y)
			pascalLine.append(str(y))
		triangle = " ".join(pascalLine)
		print(triangle.center(60))
	
	
def main(): # Main function with the necessary function calls to run the program

	userNum = userInput()
	row = findRow(userNum, 0)
	triangleList = pascalTriangle(row + 1)
	trianglePrint(triangleList)
	
main() # Initializing the program 