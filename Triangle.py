# Required for this boy
import math
import matplotlib.pyplot as plt 
import matplotlib.lines as lines

class Triangle:
    greeting = "Hi!! I'm a triangle!"
    dist = lambda a,b : math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    
    def getAngle(a, b, c):
        taninv = lambda a,b : math.atan2(b[1]-a[1], b[0]-a[0])
        theta = math.degrees(taninv(b, c) - taninv(b, a))
        return theta + 360 if theta < 0 else theta
    
    def __init__(self, pointA, pointB, pointC):
        print(Triangle.greeting, self.greeting) # instances have direct access to class variables
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
        self.angleA = Triangle.getAngle(self.pointC, self.pointA, self.pointB)
        self.angleB = Triangle.getAngle(self.pointA, self.pointB, self.pointC)
        self.angleC = Triangle.getAngle(self.pointB, self.pointC, self.pointA)
        self.sideA = Triangle.dist(self.pointB, self.pointC)
        self.sideB = Triangle.dist(self.pointA, self.pointC)
        self.sideC = Triangle.dist(self.pointA, self.pointB)
    
    def printAngles(self, rad=False):
        theta = lambda a : str(a) + " deg" if not rad else str(math.radians(a)) + " rad"
        print("Angle A:", theta(self.angleA))
        print("Angle B:", theta(self.angleB))
        print("Angle C:", theta(self.angleC))
    
    def printSides(self):
        print("Side A:",self.sideA)
        print("Side B:",self.sideB)
        print("Side C:",self.sideC)

    def area(self, precision=5):
        s = (self.sideA + self.sideB + self.sideC)/2
        result = math.sqrt(s*(s-self.sideA)*(s-self.sideB)*(s-self.sideC))
        result = round(result, precision)
        return result if result != round(result) else round(result)

    def perimeter(self):
        return self.sideA + self.sideB + self.sideC

    def show(self):        
        # x and y points
        x = [self.pointA[0], self.pointB[0], self.pointC[0], self.pointA[0]]
        y = [self.pointA[1], self.pointB[1], self.pointC[1], self.pointA[1]]
        plt.plot(x, y) # plot the points
        ax=plt.gca() # get the axes (get current axes)
        ax.set_xlim(min(x)-1, max(x)+1) # set bounds based on max/min
        ax.set_ylim(min(y)-1, max(y)+1)
        plt.title("Triangle") # title of graph
        plt.show()  # show the plot!

if __name__ == "__main__":
    tri = Triangle([0,0], [0, 2], [2,2])
    print("Perimeter:",tri.perimeter())
    print("Area:",tri.area())
    print("Tri Side A:", tri.sideA)
    tri.printAngles()
    tri.printSides()
    tri.show()
