import random

class faction(object):
    def __init__(self, name):
        money = 1500000
        ownership = {"arrow_1": [],
                     "arrow_2": [],
                     "arrow_3": [],
                     "arrow_4": []
                     }
        self.name = name
        self.political_favour = 0 # Number of "Political Favour" cards left
        self.jail_turns = 0 # Number of turns left in jail
        self.position = 0


class real_estate(object):
    """Provides inheritance class for all 'normal' spaces on the board
    """
    holding_company = {}

    def __init__(self, name, position, cost, rent_site, rent_1_house, rent_2_house, rent_3_house, rent_4_house, rent_hotel):
        self.name = name
        self.position = position
        self.cost = cost
        self.rent_site = rent_site
        self.rent_1_house = rent_1_house
        self.rent_2_house = rent_2_house
        self.rent_3_house = rent_3_house
        self.rent_4_house = rent_4_house
        self.rent_hotel = rent_hotel
        
        # These 6 tokens are used for special stuff.
        is_railroad = False # Railroads are special for certain factions
        is_utility = False # Utilities are special for certain factions,
                           # and have special rolling for rent

class railroads(object):
    holding_company = {}

    def __init__(self, name, position):
        self.name = name
        self.position = position
        
        cost = 200000
        rent = 25000
        double_rent = 2*rent
        triple_rent = 3*rent
        quad_rent = 4*rent

        is_railroad = True

class special_real_estate(object):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        # These tokens used for special reasons.
        is_chance_card = False # Have a function for if someone lands on this
        is_chest_card = False # Have a function for if someone lands on this
        is_go = False # Function for money creation
        is_go_to_jail = False # This will send people to jail, specific function
        is_free_parking = False # Specific functions for free parking
        is_tax = False # Specific function for taxing people

class utility(object):
    def __init__(self, name, position, cost):
        self.name = name
        self.position = position
        self.cost = cost
        is_utility = True


class real_estate_brown(real_estate):
    holding_company = {}


class real_estate_cyan(real_estate):
    holding_company = {}


class real_estate_pink(real_estate):
    holding_company = {"arrow_1": []}


class real_estate_orange(real_estate):
    holding_company = {"arrow_1": []}


class real_estate_red(real_estate):
    holding_company = {"arrow_1": [],
                       "arrow_2": []}


class real_estate_yellow(real_estate):
    holding_company = {"arrow_1": [],
                       "arrow_2": []}


class real_estate_green(real_estate):
    holding_company = {"arrow_1": [],
                       "arrow_2": [],
                       "arrow_3": []}


class real_estate_blue(real_estate):
    holding_company = {"arrow_1": [],
                       "arrow_2": [],
                       "arrow_3": []}

class community_chest_card(special_real_estate):
    is_chest_card = True


class chance_card(special_real_estate):
    is_chance_card = True


class go(special_real_estate):
    is_go = True


class go_to_jail(special_real_estate):
    is_go_to_jail = True


class free_parking(special_real_estate):
    is_free_parking = True

class tax_card(special_real_estate):
    is_tax = True

"""Now we begin the tedious process of creating 40 different spaces. While it's
certainly quicker than if we hadn't used classes, it's still going to take a
while. Also, I'll need some way of determining how the board works properly.
I'll probably have a list of numbers that relate to the locations
"""
old_kent = real_estate_brown("Old Kent Road", 1, 60000, 2000, 10000, 30000, 90000, 160000, 250000)
whitechapel = real_estate_brown("Whitechapel Road", 3, 60000, 4000, 20000, 60000, 180000, 320000, 450000)

angel_islington = real_estate_cyan("The Angel Islington", 6, 100000, 6000, 30000, 90000, 270000, 400000, 550000)
euston = real_estate_cyan("Euston Road", 8, 100000, 6000, 30000, 90000, 270000, 400000, 550000)
pentonville = real_estate_cyan("Pentonville Road", 9, 120000, 8000, 40000, 100000, 300000, 450000, 600000)

pall_mall = real_estate_pink("Pall Mall", 11, 140000, 10000, 50000, 150000, 450000, 625000, 750000)
whitehall = real_estate_pink("Whitehall", 13, 140000, 10000, 50000, 150000, 450000, 625000, 750000)
northumberland = real_estate_pink("Northumberland Avenue", 14, 160000, 12000, 60000, 180000, 500000, 700000, 900000)

bow = real_estate_orange("Bow Street", 16, 180000, 14000, 70000, 200000, 550000, 750000, 950000)
marlborough = real_estate_orange("Marlborough Street", 18, 180000, 14000, 70000, 200000, 550000, 750000, 950000)
vine = real_estate_orange("Vine Street", 19, 200000, 16000, 80000, 220000, 600000, 800000, 1000000)

strand = real_estate_red("The Strand", 21, 220000, 18000, 90000, 250000, 700000, 875000, 1050000)
fleet = real_estate_red("Fleet Street", 23, 220000, 18000, 90000, 250000, 700000, 875000, 1050000)
trafalgar = real_estate_red("Trafalgar Square", 24, 240000, 20000, 100000, 300000, 750000, 925000, 1100000)

leicester = real_estate_yellow("Leicester Square", 26, 260000, 22000, 110000, 330000, 800000, 975000, 1150000)
coventry = real_estate_yellow("Coventry Street", 27, 260000, 22000, 110000, 330000, 800000, 975000, 1150000)
piccadilly = real_estate_yellow("Piccadilly", 29, 280000, 22000, 120000, 360000, 850000, 1025000, 1200000)

regent = real_estate_green("Regent Street", 31, 300000, 26000, 130000, 390000, 900000, 1100000, 1275000)
oxford = real_estate_green("Oxford Street", 32, 300000, 26000, 130000, 390000, 900000, 1100000, 1275000)
bond = real_estate_green("Bond Street", 34, 320000, 28000, 150000, 450000, 1000000, 1200000, 1400000)

park_lane = real_estate_blue("Park Lane", 37, 350000, 35000, 175000, 500000, 1100000, 1300000, 1500000)
mayfair = real_estate_blue("Mayfair", 39, 400000, 50000, 200000, 600000, 1400000, 1700000, 2000000)

marylebone = railroads("Marylebone Station", 5)
marylebone.holding_company = {}

fenchurch = railroads("Fenchurch Station", 15)
fenchurch.holding_company = {"arrow_1":[]}

kings_cross = railroads("Kings Cross Station", 25)
kings_cross.holding_company = {"arrow_1":[],"arrow_2":[]}

liverpool = railroads("Liverpool Street Station", 35)
liverpool.holding_company = {"arrow_1":[], "arrow_2":[], "arrow_3":[]}

go_space = go("Global Offices", 0)
visiting_jail = free_parking("Jail", 10)
free_parking_space = free_parking("Business Management Incorporated", 20)
go_to_jail_space = go_to_jail("Go To Jail", 30)

chest_space_1 = community_chest_card("Community Chest", 2)
chest_space_2 = community_chest_card("Community Chest", 17)
chest_space_3 = community_chest_card("Community Chest", 33)

chance_space_1 = chance_card("Chance", 7)
chance_space_2 = chance_card("Chance", 22)
chance_space_3 = chance_card("Chance", 36)

tax_space_1 = tax_card("Income Tax", 4)
tax_space_2 = tax_card("Property Tax", 38)

electric_company = utility("Electric Company", 12, 150000)
water_works = utility("Water Works", 28, 150000)
