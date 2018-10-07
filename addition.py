inp = input()
inp1 = input()
while inp.isdigit() is False and inp1.isdigit() is False:
    print("Enter only digits")
    inp = input()
    inp1 = input()


if inp.isdigit() and inp.isdigit():
    total = int(inp)+int(inp1)
    print("Total: ", total)


