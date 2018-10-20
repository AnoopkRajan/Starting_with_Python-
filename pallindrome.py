a=list() 
for x in range(12):
	n=input("Enter a string : ")
	#this adds 12 strings to the list a
	a.append(str(n))
b=""#declaring an empty string to concatenate 3 at a time
for y in range(12):
	b=b+a[y]
	if((y+1)%3==0): 
		#concatenates 3 at a time
		word=b		
		print("Real Word : ",word)
		revword=b[::-1]
		print("New Word : ",revword) 
		if(word==revword):
			print("The Concatenated words produce a Palindrome")
		else:
			print("The Concatenated words do not produce a Palindrome")
		b=""
