import random
import items, enemies, actions, world, config
from player import Player
 
class MapTile:
    """Parent tile class"""
    config.init()
    def __init__(self, x, y, ):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()
    
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = []
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        for a in config.player.inventory:
            if isinstance(a, items.Dagger):
                if config.player.equipped_weapon != items.Dagger:
                    moves.append(actions.EquipDagger())
                    break
        
        return moves
    
        
        
    
class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
    
class EntranceTile(MapTile):
    """A tile that acts as the introduction to the entire room."""
    def intro_text(self):
        return """You are in a large room that is empty save for a terminal to the north."""
    def modify_player(self, player):
        player.room_text = self.intro_text()
    
class Door(MapTile):
    """Doors will always face south to north. Anything north of the door is blocked until the door is unlocked"""
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def intro_text(self):
        for a in config.player.inventory:
            if isinstance(a, items.Key):
                return """The door is unlocked. You may walk through."""
                break
        return """The door is locked. Find a key to unlock it."""
        
                
    def modify_player(self, player):
        pass
    
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x - 1, self.y):
            for a in config.player.inventory:
                if isinstance(a, items.Key):
                    moves.append(actions.MoveNorth())
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveSouth())
        return moves
    
    
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = []
        #try recreating adjacent moves instead of removing a single adjacent move
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        for a in config.player.inventory:
            if isinstance(a, items.Dagger):
                if config.player.equipped_weapon != items.Dagger:
                    moves.append(actions.EquipDagger())
                    break
        
        return moves
    
    
class LootRoom(MapTile):
    """Template for all tiles with items"""
    def __init__(self, x, y, item):
        self.item = [item]
        super().__init__(x, y)
 
    def available_actions(self):
        moves = []
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        for a in config.player.inventory:
            if isinstance(a, items.Dagger) and config.player.equipped_weapon != items.Dagger:
                moves.append(actions.EquipDagger())
                break
        print(config.player.equipped_weapon)
        if len(self.item) > 0:
            config.player.grab_string = []
            item_string = "Grab {}".format(self.item[0].name.lower())
            print(item_string)
            config.player.grab_string.append(item_string)
            moves.append(actions.GrabItem(item=self.item))
            
        return moves
            
    def modify_player(self, player):
        pass


class EnemyRoom(MapTile):
    """Template for all tiles with enemies"""
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            #make this loop repeat infinitely
            random_attack = random.randrange(len(self.enemy.attacks))
            print(self.enemy.attacks[random_attack])

    def available_actions(self):
        moves = []
        if self.enemy.is_alive():
            for a in config.player.equipped_weapon.techniques.values():
                for b in self.enemy.weaknesses.values():
                    string = "{} {}".format(a, b)
                    config.player.available_attacks.append(string)
                    print(string)
                    moves = [actions.Attack(enemy=self.enemy)]
            for a in config.player.inventory:
                if isinstance(a, items.Dagger) and config.player.equipped_weapon != items.Dagger:
                    moves.append(actions.EquipDagger())
                    break
                    
            return moves
        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            for a in config.player.inventory:
                if isinstance(a, items.Dagger) and config.player.equipped_weapon != items.Dagger:
                    moves.append(actions.EquipDagger())
        
            return moves
    
        
        
class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class RightCorner(MapTile):
    """Same as EmptyCavePath, but different flavor text."""
    def intro_text(self):
        return """
        The corridor turns east.
        """

class LeftCorner(MapTile):
    """Same as EmptyCavePath, but different flavor text."""
    def intro_text(self):
        return """
        The corridor turns west.
        """

class HealingFountain(MapTile):
    """Heals the player to full HP."""
    def intro_text(self):
        return """
        You see a glowing fountain before you. The water looks so cool and refreshing that you are filled with determination for whatever lies ahead. You dunk your entire face in and drink as much as you can. Full HP!
        """
    def modify_player(self):
        config.player.hp = 16

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """

class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A vicious, giant ogre wobbles towards you with a huge belly and
            long dangly arms.
            """
        else:
            return """
            You see the remains from the intense skirmish with the ogre.
            """
class ImpRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Imp())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You hear a deafening screech above you just as a vicious looking,
            fiery imp flies towards you. It has large, thin wings and a
            disgusting, unprotected head.
            """
        else:
            return """
            You see the scorch marks from your battle with the imp.
            """

class DraugrRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Draugr())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            As you make your way through the cavern, you hear what sounds like chimes. Suddenly, a rotten Draugr crawls out of a nearby coffin, equipped with a huge broadsword. It is wearing rusted armor, with an exposed ribcageand pelvis. He immediately sees you and attacks.
            """
        else:
            return """
            You see a pile of bones.
            """
 
class FinalBoss(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.TieflingKing())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            insert dramatic boss description and let the battle commence.
            """
        else:
            return """
            You see the entrance ahead of you. Victory is within your grasp!
            """ 
class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
        
    def intro_text(self):
        if len(self.item) >= 1:
            return """You notice a large rug in the center of the room"""
        else:
            return """
            An unremarkable part of the cave. You must forge onwards.
            """
        
class FindKeyTile(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Key())
    def intro_text(self):
        if len(self.item) >=1:
            return """You notice a golden key on a pedestal."""
        else:
            return """You see a wooden pedestal where the golden key once was."""
    

class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold())
        
    def intro_text(self):
        return """
        You notice a small coin purse on the ground. You pick it up!"""
    
    
class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
         
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True
