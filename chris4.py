n=int(input("enter the no of rows:"))
for i in range(1,n+1):
	print(" "*(n+12-i),end=" ")
	for j in range(1,i+1):
		print("*",end=" ")
	print()
for i in range(1,n+1):
	print(" "*(n+8-i),end=" ")
	for j in range(1,i+3):
		print("*",end=" ")
	print()
for i in range(1,n+1):
	print(" "*(n+4-i),end=" ")
	for j in range(1,i+5):
		print("*",end=" ")
	print()
for i in range(1,n+1):
	print(" "*(n-i),end=" ")
	for j in range(1,i+7):
		print("*",end=" ")
	print()
for i in range(1,n+1):
	print(" "*(n-1),end=" ")
	for j in range(1,n-4):
		print("*",end=" ")
	print()

