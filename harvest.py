############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):

        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code



def make_melon_types():
    """Returns a list of current melon types."""
    melon_musk = MelonType(
        "musk", 
        "1998", 
        "green",
        True, 
        True, 
        "Muskmelon")
    melon_musk.add_pairing("mint")
    
    melon_casaba = MelonType(
        "cas", 
        "2003", 
        "orange", 
        False, 
        False,
        "Casaba")
    melon_casaba.add_pairing("strawberries")
    melon_casaba.add_pairing("mint")

    melon_cren = MelonType(
        "cren",
        "1996",
        "green",
        False,
        False,
        "Crenshaw"
    )
    melon_cren.add_pairing("prosciutto")

    melon_yellow_w = MelonType(
        "yw", 
        "2013", 
        "yellow", 
        False, 
        True, 
        "Yellow Watermelon")
    melon_yellow_w.add_pairing("ice cream")


    all_melon_types = [melon_musk, melon_casaba, melon_cren, melon_yellow_w]

    # Fill in the rest

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
            print(f"{melon_type.name} pairs with")
            for pairing in melon_type.pairings:
                print(f"- {pairing}")
            print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    res = {}
    for melon_type in melon_types:
        res[melon_type.code] = melon_type

    for key, value in res.items():
        print(f"{key}: {value}")
    return res

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, type, shape, color, origin, person):
        self.melon_type = type
        self.shape_rating = shape
        self.color_rating = color
        self.origin = origin
        self.person = person

    def is_sellable(melon):

        return self.shape_rating > 5 and self.color_rating > 5 
        and self.origin != 3



def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon1 = Melon("yw", 8, 7, 2, "Sheila")
    melon2 = Melon("yw", 3, 4, 2, "Sheila")
    melon3 = Melon("yw", 9, 8, 2, "Sheila")
    melon4 = Melon("cas", 10, 6, 35, "Sheila")
    melon5 = Melon("cren", 8, 9, 35, "Micheal")
    melon6 = Melon("cren", 8, 2, 35, "Micheal")
    melon7 = Melon("cren", 2, 3, 4, "Micheal")
    melon8 = Melon("musk", 6, 7, 4, "Micheal")
    melon9 = Melon("yw", 7, 10, 3, "Sheila")
    melon_list = [melon1, melon2, melon3, melon4, melon5, 
    melon6, melon7, melon8, melon9]

    return melon_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
