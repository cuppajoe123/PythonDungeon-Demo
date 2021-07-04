class Enemy:
    """Parent enemy class"""
    def __init__(self, name, hp, damage, weaknesses, attacks):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weaknesses = weaknesses
        self.attacks = attacks
 
    def is_alive(self):
        return self.hp > 0
    
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=6, damage=2, 
                weaknesses={'weakness_1': 'eyes',
                            'weakness_2': 'legs'},
                attacks=['The spider sinks its fangs into your arm.', 'The spider shoots a web at you.'])
 
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Vicious Ogre", hp=10, damage=1,
                weaknesses={'weakness_1': 'belly', 
                            'weakness_2': 'arms'}, 
                attacks=['The ogre punches you.', 'The ogre slams his club into you.'])

class Imp(Enemy):
    def __init__(self):
        super().__init__(name="Fiery Imp", hp=4, damage=3, 
                weaknesses={'weakness_1': 'wings', 
                            'weakness_2': 'head'}, 
                attacks=['The imp throws a fireball in your direction and it glances off your shoulder.', 
                         'The imp swoops down to you and slices with its long sharp claws.']) 
        
class Draugr(Enemy):
    def __init__(self):
        super().__init__(name="Draugr", hp=6, damage=3, 
                weaknesses={'weakness_1': 'ribcage', 
                            'weakness_2': 'pelvis'}, 
                attacks=['The Draugr swings his sword at you.', 
                         'The Draugr kicks you in the shin, knocking you off balance.'])

class TieflingKing(Enemy):
    def __init__(self):
        super().__init__(name="Akmenos the Tiefling King", hp=10, damage=3, 
                weaknesses={'weakness_1': 'tail', 
                            'weakness_2': 'jaw', 
                            'weakness_3': 'hands', 
                            'weakness_4': 'arms'}, 
                attacks=[
                    'The Tiefling King lunges towards you with its razor sharp teeth ands takes a bite out of your arm. There is no bleeding, for its teeth are as hot as lava.', 
                    'The Tiefling King casts a fireball at you.',
                    'The Tiefling King charges at you with its long red horns, impaling you.', 
                    'The Tiefling King swings its tail at you. It was so fast, it sliced one of your fingers clean off.',
                    ]
                )

