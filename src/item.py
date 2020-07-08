

class Item:
    """
    Base class for all sorts of items.
    """
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value

    def on_take(self, custom=None):
        if not custom:
            print(f"You have picked up a {self.name}")
        else:
            print(custom)

    def on_drop(self, custom=None):
        if not custom:
            print(f"You have dropped a {self.name}")
        else:
            print(custom)

class Weapon(Item):
    def __init__(self, name, desc, value, damage):
        super().__init__(name, desc, value)
        self.damage = damage

class Gold(Item):
    def __init__(self, name, desc, value):
        super().__init__(name, desc, value)

    def on_take(self, custom=None):
        print(f"You picked up {self.value} gold pieces.")

class LightSource(Item):
    def __init__(self, name, desc, value):
        super().__init__(name, desc, value)

    def on_drop(self, custom=None):
        if not custom:
            print(f"You have dropped your lightsource. You get the distinct feeling that this is unwise, but you do it anyway.")
        else:
            print(custom)