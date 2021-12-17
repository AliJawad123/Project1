class Myvector:
    j = []
    def __init__(self,*args):
        try:
            self.next=[]
            self.j=[]
            self.square=[]
            self.count=0
            self.res_list = []
            for i in args:
                self.component=int(i)
                self.j.append(self.component)
                self.count=self.count+1
        except ValueError:
            print("Invalid input.")

    def __str__(self):
        return "Myvector"+str(tuple(self.j))


    def __len__(self):
        return self.count

    def __iter__(self):
        return iter(self.j)

    def __getitem__(self,item):
        return self.j[item]

    def __abs__(self):
        for i in self.j:
           self.square.append(i*i)
        x=sum(self.square)
        return x**(1/2)

    def __bool__(self):
        x=self.__abs__()
        if x>0:
            return False
        else:
            return True
    def __add__(self,other):
        for i in range(0, len(self.j)):
            self.res_list.append(self.j[i] + other.j[i])
        vector=Myvector()
        vector.j=self.res_list
        return vector

    def __mul__(self, other):
        multiplied_list = [element * other for element in self.j]
        return "Myvector"+str(tuple(multiplied_list))



    def __iadd__(self, other):
        for i in range(0, len(self.j)):
            self.next.append(self.j[i] + other.j[i])
        vector = Myvector()
        vector.j = self.next
        return vector

    def __lshift__(self, other):
        self.j = [self.j[(i + other) % len(self.j)]
                     for i, x in enumerate(self.j)]
        return "Myvector"+str(tuple(self.j))

if __name__=='__main__':

  x0 = Myvector()
  x0.__str__()
  # my=Myvector('jawad',4)
  #my.__str__()

  x1 = Myvector(1, 1, 4)
  print(len(x1))
  print(x1)


  for element in x1:
    print(element)

  print(x1[0])
  # print(x1[5])	# raises 'IndexError' exception
  #x1[2] = 33
  #print(x1)  # MyVector(3,5,33,0)

  x2 = Myvector(3, 4)
  print(abs(x2))

  if x2:
    print("this line will print")
  else:
    print("this line will NOT print")

  #####################################
  ## Arithmetic
  #####################################

  x1 = Myvector(1, 2, 3)
  x2 = Myvector(4, 5, 6)
  x3=x1+x2
  print(x1)
  print(x2)
  print(x3)


  x1 += x2
  print(x1)  # MyVector(5,7,9)
  print(x2)


        # for print the object

x1 = Myvector(1,2,3)
x2=x1*2

print(x2)

print()
x1 = Myvector(1,2,3)
x2 = x1<<1
print(x2) 	# MyVector(2,3,1)