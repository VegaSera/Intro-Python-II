# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc, n_to_err="You cannot move north.", s_to_err="You cannot move south.",
                 e_to_err="You cannot move east", w_to_err="You cannot move west.",
                 dark="This room is pitch black. You can't see or feel anything.",items=None, is_light=False):
        self.name = name
        self.desc = desc
        if items is None:
            self.items = []
        else:
            self.items = items
        self.is_light = is_light
        self.dark = dark

        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None

        self.n_to_err = n_to_err
        self.s_to_err = s_to_err
        self.e_to_err = e_to_err
        self.w_to_err = w_to_err