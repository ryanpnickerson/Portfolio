def evenFib():
	sum = 0
	x = 1  
	y = 2  
	while x <= 4000000:
		if x % 2 == 0:
			sum += x
		x, y = y, x + y
	return str(sum)


if __name__ == "__main__":
	print(evenFib())
