import re

print("Python Calulator")
print("Type 'quit' to exit")

previous = 0
run = True

def performCalc():
    global run
    global previous

    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Goodbye! whoever.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()!" "]', '', equation)

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)


while run:
    performCalc()
