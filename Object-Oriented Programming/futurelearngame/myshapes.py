from shapes import Paper, Shape, Triangle, Rectangle, Oval
#*This Shape class is created in the shapes.py file

paper = Paper()

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_x(0)
rect1.set_y(0)
rect1.set_color("blue")
rect1.draw()

rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(100)
rect2.set_color("red")
rect2.draw()

oval1 = Oval()
oval1.randomize()
oval1.draw()

tri1 = Triangle(121,223,2,2,234,3)

tri1.draw()

paper.display()