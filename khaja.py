n=int(input("enter the number"))
n=str(n)
dup=n[::-1]
if(n[::-1]==dup):
	print("pal")
else:
	print("not palindrome")
