from object_oriented.FutureLearn_oop.shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color('Blue')
rect1.draw()
#rect1.set_x(100)
#rect1.set_y(100)

rect2 = Rectangle()
rect2.set_width(200)
rect2.set_height(100)
rect2.set_color('Yellow')
rect2.set_y(100)
rect2.set_x(100)
rect2.draw()

oval = Oval()
oval.randomize()
oval.draw()

paper.display()