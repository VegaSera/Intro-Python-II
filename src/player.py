# Write a class to hold player information, e.g. what room they are in
# currently.
class Actor:
    """
    Generic Actor class that serves as a master class for players and monsters.
    """
    def __init__(self, name, cur_loc, cur_hp, max_hp, gold, inventory=None):
        self.name = name
        self.cur_loc = cur_loc
        self.hp = cur_hp
        self.max_hp = max_hp
        self.gold = gold
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def move(self, direction, is_light):
        if direction in ['n', 'north']:
            if self.cur_loc.n_to is not None:
                self.cur_loc = self.cur_loc.n_to
                return "You move north."
            else:
                if is_light:
                    return self.cur_loc.n_to_err
                else:
                    return "You stumble through the darkness and find that you cannot go north."
        elif direction in ['s', 'south']:
            if self.cur_loc.s_to is not None:
                self.cur_loc = self.cur_loc.s_to
                return "You move south."
            else:
                if is_light:
                    return self.cur_loc.n_to_err
                else:
                    return "You stumble through the darkness and find that you cannot go south."
        elif direction in ['e', 'east']:
            if self.cur_loc.e_to is not None:
                self.cur_loc = self.cur_loc.e_to
                return "You move east."
            else:
                if is_light:
                    return self.cur_loc.n_to_err
                else:
                    return "You stumble through the darkness and find that you cannot go east."
        elif direction in ['w', 'west']:
            if self.cur_loc.w_to is not None:
                self.cur_loc = self.cur_loc.w_to
                return "You move west."
            else:
                if is_light:
                    return self.cur_loc.w_to_err
                else:
                    return "You stumble through the darkness and find that you cannot go west."
        else:
            return f"Unrecognized Direction: {direction}"




class Player(Actor):
    def __init__(self, name, cur_loc, cur_hp, max_hp, inventory=None):
        super().__init__(name, cur_loc, cur_hp, max_hp, inventory)

    def show_inventory(self):
        if len(self.inventory) > 0 or self.gold > 0:
            print("You have:")
            print(f"{self.gold} Gold Pieces.")
            for item in self.inventory:
                print(f"{item.name} - {item.desc}")
        else:
            print("You have no gold and no items in your inventory.")