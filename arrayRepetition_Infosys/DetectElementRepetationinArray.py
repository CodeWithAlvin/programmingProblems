Date="29/3/2021"
source="infosys sample paper"
"""
Question :
    given the space separated string like 'string' below
    the first no is the no of rows in the array form the array 
    from above information and perform following find out

    if any no is repeated conductively four times
    either diganolly , horizontaly or vertically
    if yes return that number
    and if multiple such pattern exist 
    return smallest of them

    else return -1
    assume row is always greatwr than 3
"""
"""
    For visualising during problem solving
        1(0,0) 2(0,1) 3(0,2) 0(0,3)
        1(1,0) 0(1,1) 0(1,2) 2(1,3) 
        1(2,0) 0(2,1) 5(2,2) 9(2,3) 
        1(3,0) 0(3,1) 5(3,2) 6(3,3)
        1(4,0) 5(4,1) 6(4,2) 0(4,3)
        2(5,0) 0(5,1) 8(5,2) 5(5,3)
"""
from pprint import pprint


    
# question input string
string="5 4 4 2 5 2 2 4 1 1 3 1 5 4 2 5 3 4 8 4 2 6 8 5 1 4 5 6 1 8 5"

class Solver:
    def __init__(self,string):
        self.returnVal=-1
        # convertying to an int list for performing operation
        self.numList=[int(x) for x in string.split(" ")]
        # extracting first no as it is no of rows
        self.rows=self.numList[0]
        #finding the width by dividing total elements with the no of rows
        self.width=int((len(self.numList)-1)/self.rows)
        
    def FormArray(self):
        """
        forms an array that could be easily operationable
        """
        self.array=[]
        lastiter=1
        for i in range(self.rows):
            self.array.append(self.numList[lastiter:lastiter+self.width])
            lastiter+=self.width
            
     
    def TryReplace(self,n):
        if self.returnVal == -1 or self.returnVal > n:
            self.returnVal = n
        
        else:
            None

    def HorizontalPattern(self):
        """
        checking if any horizontal pattern exist 
        if exist return that no which is repted more than four time 
        if multiple pattern return the smalllest of them
        """
        for i in self.array:
            for j in range(len(i)-3):               
                if i[j] == i[j+1] == i[j+2] == i[j+3]:
                    self.TryReplace(i[j])
                        
            
    def VerticalPattern(self):
        """
        checking if any vertical pattern exist 
        if exist return that no which is repted more than four time 
        if multiple pattern return the smalllest of them
        """
        for i in range(self.width):
            for j in range(self.rows-3):
                if self.array[j][i] == self.array[j+1][i] == self.array[j+2][i] == self.array[j+3][i]:
                    self.TryReplace(self.array[j][i])
                
            
    
    def DigonallPattern(self):
        #Todo implementation
        pass
      
    def build(self):
        self.FormArray()
        self.HorizontalPattern()
        self.VerticalPattern()
        self.DigonallPattern()
        
        return self.returnVal
        
        
        
s=Solver(string)
print(s.build())
pprint(s.array)
