name = "simeon"
print(name)
i = 1
favNum = 6
while i <= favNum*favNum:
	print (i)
	i+=1
print("My favorite number squared is "+ str(i-1))

class Engineer:
  def __init__(self, name, type, experience):
    self.skill = "Problem Solver"
    self.name = name
    self.type = type
    self.experience = experience

p1 = Engineer("John", "Electrical", "5 years")
p2 = Engineer("Pete", "Mechenical", "3 years")

print(vars(p1))
print(vars(p2))

nameReverse = name [::-1]
print(nameReverse)