
class golden_point:
    
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def __str__(self) -> str:
        return "G"

class silver_point:
    
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.score = 0

    def __str__(self) -> str:
        return "G-" + str(self.score)
    
class silver_point:
    
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.score = 0
        
    def __str__(self) -> str:
        return "S-" + str(self.score)
    

class tile:
    
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.id = 0
        self.cost = 0
        
    def __str__(self) -> str:
        return str(self.id) + '-' + str(self.cost)