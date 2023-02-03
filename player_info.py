class Hero:

    # Create a Hero with specific attributes
    def __init__(self):
        
        # Hero name
        self.name = "player"

        # Min/Max attributes for the Hero
        self.attri = {
            "end": False,
            "hp":  -100, # 100
            "str": -10,  # 10
            "dex": -10,  # 10
            "con": -10,  # 10
            "int": -10,  # 10
            "wis": -10,  # 10
            "cha": -10   # 10
        }
    
    # Changes a specific attribute value
    def set_attri(self, attri, new_value):
        self.attri[attri] = new_value
