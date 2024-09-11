class Player:
    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0


    def move(self, steps):
        if (self.position + steps) < Player.MAX_POSITION:
            self.position += steps
        else:
            self.position = Player.MAX_POSITION   

       
   
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()