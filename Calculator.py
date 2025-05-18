n1 = int(input("Enter a number: "))
n2 = int(input("Enter a second number: "))
op = input("What operation do you want to perform: ")
ans = ""

if op == "+":
    ans = n1 + n2
if op == "-":
    ans = n1 - n2
if op == "x" or op == "*":
    ans = n1 * n2
if op == "/":
    ans = n1 / n2

print(ans)
