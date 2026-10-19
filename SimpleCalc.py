class calculator:

	print ("Simple calculator made by LarvaMonkey")


	def questions(self):
		while True:
			number = input("First Number: ")

			if number.isdigit():
			   self.first_number = int(number)
			   break
			else:
				print("Not a number! Try again.")


		while True:
			number = input("Second Number: ")

			if number.isdigit():
				self.second_number = int(number)
				break
			else:
				print("Not a number! Try again.")

		while True:
			self.symbol = input("Desired symbol: ")

			if self.symbol not in ["x", "+", "-", "/"]:
				print("Invalid symbol! Try again.")
			else:
				break

	def calculate(self):
		if self.symbol == "x":
			answer = self.first_number * self.second_number
		elif self.symbol == "+":
			answer = self.first_number + self.second_number
		elif self.symbol == "-":
			answer = self.first_number - self.second_number
		elif self.symbol == "/":
			answer = self.first_number / self.second_number
				
		return answer
	
	def result(self):
		answer = self.calculate()
		print(f"The answer to your equasion is: {answer}")

larvas_calc = calculator()
larvas_calc.questions()
larvas_calc.result()

# Made by LarvaMonkey.