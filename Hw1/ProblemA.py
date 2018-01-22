#Polynomial class
# args: List 
class polynom(object):
        poly = []
        # initialize method
        # sets instance variable poly to the object that was passed in.
        def __init__(self,object):
            self.poly = checkLeading(object)
                if(type(object) == list):
                        self.poly = checkLeading(object)
                else:
                        self.poly = []
            
        # + operator overload
        # args: two polynomial lists, list1 and list2
        # returns: new polynomial with the new polynomial instance variable inside.
        def __add__(list1,list2):
                copyList1 = checkBigger(list1.poly,list2.poly)
                copyList2 = checkSmaller(list1.poly,list2.poly)
                if(len(copyList1) == len(copyList2)):
                        for i in range(0, len(copyList1)):
                                copyList1[i] += copyList2[i]
                else:
                        for i in range(0, len(copyList2)):
                                cl1StartPoint = len(copyList1) - len(copyList2)
                                copyList1[cl1StartPoint+i] += copyList2[i]
                newPoly = polynom(copyList1)
                return newPoly
        # - operator overload
        # args: two polynomial lists, list1 and list2
        # returns: new polynomial with the new polynomial instance variable inside. 
        def __sub__(list1,list2):
                copyList1 = list1.poly
                copyList2 = list2.poly
                if(len(copyList1) == len(copyList2)):
                        for i in range(0, len(copyList1)):
                                copyList1[i] -= copyList2[i]

                        newPoly = polynom(copyList1)
                else:
                        if(len(copyList1) > len(copyList2)):
                                for i in range(0, len(copyList2)):
                                        cl1StartPoint = len(copyList1) - len(copyList2)
                                        copyList1[cl1StartPoint+i] -= copyList2[i]
                                newPoly = polynom(copyList1)
                        elif(len(copyList1) < len(copyList2)):
                                for i in range(0, len(copyList1)):
                                        cl1StartPoint = len(copyList2) - len(copyList1)
                                        copyList2[cl1StartPoint+i] -= copyList1[i]
                                for i in range(0, len(copyList2)):
                                        copyList2[i] = -copyList2[i]
                                newPoly = polynom(copyList2)

                return newPoly
        
        # * operator overload
        # args: two polynomial lists, list1 and list2
        # returns: new polynomial with the new polynomial instance variable inside.
        def __mul__(list1,list2):
                copyList1 = checkBigger(list1.poly,list2.poly)
                copyList2 = checkSmaller(list1.poly,list2.poly)
                if(len(copyList1) != 1) and (len(copyList2) != 1):
                        newListLen = len(copyList1) + len(copyList2) - 1
                        newList = [0] * newListLen
                        for i in range(0, len(copyList1)):
                                for j in range(0, len(copyList2)):
                                        newList[i+j] = newList[i+j] + copyList1[i] * copyList2[j]

                elif(len(copyList2) == 1):
                        newList = [0] * len(copyList1)
                        for i in range(0, len(copyList1)):
                                newList[i] = copyList1[i] * copyList2[0]
                                
                else:
                        copyList1[0] = copyList1[0] * copyList2[0]
                        newList= copyList1       
                newPoly = polynom(newList)
                return newPoly
                                        

        # Integration method
        # args: int a, int b
        # integrates self.poly from a to b.
        # returns: value of the integration
        def intg(self,a,b):
                totalInt = 0
                for i in range(0,len(self.poly)):
                        totalInt += 1.0/(len(self.poly)-i) * power(b,(len(self.poly)-i)) * self.poly[i] - 1.0/(len(self.poly)-i) * power(a,(len(self.poly)-i)) *  self.poly[i]
                if(len(self.poly) > 0):
                        for i in range(0,len(self.poly)):
                                totalInt += 1.0/(len(self.poly)-i) * power(b,(len(self.poly)-i)) * self.poly[i] - 1.0/(len(self.poly)-i) * power(a,(len(self.poly)-i)) *  self.poly[i]

                return totalInt
                        
        # Derivative method
        # takes the current polynomial and does the derivative.
        # returns: the list of the polynomial
        def drv(self):
                copyList = self.poly
                for i in range(0, len(self.poly)):
                        copyList[i] = copyList[i] * (len(self.poly) - i - 1)
                newList = allButLast(copyList)
                newPoly = polynom(newList)
                if(len(self.poly) > 1):
                        for i in range(0, len(self.poly)):
                                copyList[i] = copyList[i] * (len(self.poly) - i - 1)
                        newList = allButLast(copyList)
                        newPoly = polynom(newList)
                else:
                        newPoly = polynom([])
                return newPoly                

        # len operator overload
        # returns: length of self.poly
        def __len__(self):
                return len(self.poly)

# exponent method
# returns: a to the power b
def power(a,b):
        newA = a
        for i in range(1,b):
                newA = newA*a

        return newA

# checkLeading method
# checks the beginning of the list for leading 0s, doing so recursively until no 0s are in the front. calls a function to create the new list if needed.
# args: a list
# returns: the new list without leading zeroes.
def checkLeading(list):
        if(len(list) > 1 and list[0] == 0 ):
                newList = allButFirst(list)
                list = checkLeading(newList)
                return list
        elif(len(list) == 1 and list[0] == 0):
                return []
        else:
                return list
# allButFirst method
# Takes a list and returns the tail.
# args: a list
# returns: a new list without the head element.
def allButFirst(list):
        newList = []
        for i in range(0, len(list)-1):
                newList.append(list[i+1])
                
        return newList

# allButLast method
# Takes the given list and returns a list that has everything except the very last element.
def allButLast(list):
        newList = []
        for i in range(0, len(list)-1):
                newList.append(list[i])

        return newList

# checkBigger method
# determines which list of the two has more elements.
# args: list1, list2
# returns: whichever list is bigger.
def checkBigger(list1,list2):
        if(len(list1)>len(list2)):
                return list1
        elif(len(list1) < len(list2)):
                return list2
        else:
                return list1

# checkSmaller method
# determines which list of the two has less elements.
# args: list1, list2
# returns: whichever list is smaller.
def checkSmaller(list1,list2):
        if(len(list1)>len(list2)):
                return list2
        elif(len(list1) < len(list2)):
                return list1
        else:
                return list2


