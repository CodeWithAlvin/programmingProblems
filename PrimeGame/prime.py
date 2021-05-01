def isPrime(n):
	if n in [0,1,4,6]:
		return False
	if n==2 or n==3 or n==5:
		return True
	else:
		for i in range(2,int(n/2)):
			if n%i==0:
				return False
		return True
	
# 3 5
def main():
	cases=int(input())
	for i in range(cases):
		no=input()
		lower=int(no.split(" ")[0])
		upper=int(no.split(" ")[1])
		
		if lower==upper:
			if isPrime(lower):
				print(0)
				continue
			print(-1)
			continue

		firstprime=lower
		while True:
			if lower>upper:
				firstprime=-1
				break
			if isPrime(lower):
				firstprime=lower
				break
			lower+=1
				
		lastprime=upper
		while True:
			if upper<lower:
				lastprime=-1
				break
			if isPrime(upper):
				lastprime=upper
				break
			upper-=1

		if firstprime==-1 and lastprime==-1:
			print(-1)
		elif firstprime==lastprime:
			print(0)
		else:
			print(lastprime-firstprime)
	
	
main()