
class Vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str1 =""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} + " 
            index += 1
        return str1[:-2]

    def __add__(self, vec2):
        newLIst = []
        for i in range(len(self.vec)):
            newLIst.append(self.vec[i] + vec2.vec[i])
        return Vector(newLIst)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i]*vec2.vec[i]
        return sum

v1 = Vector([2, 4, 6, 8])
v2 = Vector([3, 5, 7, 9])
print(v1 + v2)
print(v1*v2)
        