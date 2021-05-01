def main():
	virus=input()
	virus_copy=virus
	no_of_person=int(input())
	for i in range(no_of_person):
		codes=input()
		virus=virus_copy
		for i,word in enumerate(codes):
			if word in virus:
				if i==len(codes)-1:
					print("POSITIVE")
				virus=virus[virus.index(word):]
			else:
				print("NEGATIVE")
				break
		
main()


