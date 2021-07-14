class Item():
    """The base class for all items."""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return "{}\n=====\n{}\n".format(self.name, self.description) 
    
class Weapon(Item):
    """A template for all weapons"""
    def __init__(self, name, description, damage, techniques):
        self.damage = damage
        self.techniques = techniques
        super().__init__(name, description)
    def __str__(self):
        return ""


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         damage=2,
                         techniques={'tech_1': 'Stab',
                                     'tech_2': 'Slice'})

class Fists(Weapon):
    def __init__(self):
        super().__init__(name="Fists",
                         description="They're just fists",
                         damage=2,
                         techniques={'tech_1': 'Punch',
                                     'tech_2': 'Smack'})
class Key(Item):
    """The player must have the Key item to walk through doors"""
    def __init__(self):
        super().__init__(name="Key",
                         description="An ornate golden key with red gems encrusted")
