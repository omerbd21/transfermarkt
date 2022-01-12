class Player():
    def __init__(self):
        self.player_data = {}

    def to_json(self):
        return self.player_data    
    
    @property
    def shirt_number(self):
        return self.player_data["shirt_number"]
    @shirt_number.setter
    def shirt_number(self, number):
        self.player_data["shirt_number"] = number
    
    
    @property
    def name(self):
        return self.player_data["name"]
    @name.setter
    def name(self, name):
        self.player_data["name"] = name
    
    
    @property
    def position(self):
        return self.player_data["position"]
    @position.setter
    def position(self, position):
        self.player_data["position"] = position
    

    @property
    def age(self):
        return self.player_data["age"]
    @age.setter
    def age(self, age):
        self.player_data["age"] = age