class Animal():
    def __init__(self, kind, legs):
        self.kind = kind
        self.legs = legs 

    def description(self):
        if self.legs == 1: print(self.kind, "має", self.legs, "кінцівку")
        else: print(self.kind, "має", self.legs, "кінцівки")

cat = Animal("cat", 4)    
bird = Animal("bird", 1)  
print(cat.description()) 
print(bird.description()) 