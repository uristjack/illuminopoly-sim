import random

class Faction(object):
    """A class to create factions - or players - for Illuminopoly."""
    def __init__(self, name, idnumber):
        self.money = 1500000
        self.name = name
        self.idnumber = idnumber
        self.political_favour = 0 # Number of "Political Favour" cards left
        self.jail_turns = 0 # Number of turns left in jail
        self.position = 0


class RealEstate(object):
    """Provides class for all 'normal' spaces on the board - all colour spaces.
    """
    holding_company = {}

    def __init__(self, name, position, cost, rent_site, rent_1_house,
                 rent_2_house, rent_3_house, rent_4_house, rent_hotel,
                 colour):
        self.name = name
        self.position = position
        self.cost = cost
        self.rent_site = rent_site
        self.rent_1_house = rent_1_house
        self.rent_2_house = rent_2_house
        self.rent_3_house = rent_3_house
        self.rent_4_house = rent_4_house
        self.rent_hotel = rent_hotel

        self.is_buyable = True
        self.colour = colour
        self.is_owned = False
        self.owner = 0


class Railroads(object):
    """Provides a class for all railroad spaces."""
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
        self.cost = 200000
        self.rent = 25000
        self.double_rent = 2*self.rent
        self.triple_rent = 3*self.rent
        self.quad_rent = 4*self.rent

        self.is_buyable = True
        self.is_railroad = True
        self.is_owned = False
        self.owner = 0


class SpecialRealEstate(object):
    """Provides a class for all "special" real estate in Illuminopoly.
    In other words, spaces with functions for them. E.g.:
    - Chance Cards
    - Community Chest Cards
    - Go
    - Go to Jail
    - Free Parking
    - Tax"""
    def __init__(self, name, position):
        self.name = name
        self.position = position
        # These tokens used for special reasons.
        self.is_chance_card = False # Have a function for if someone lands on this
        self.is_chest_card = False # Have a function for if someone lands on this
        self.is_go = False # Function for money creation
        self.is_go_to_jail = False # This will send people to jail, specific function
        self.is_free_parking = False # Specific functions for free parking
        self.is_tax = False # Specific function for taxing people
        self.is_owned = False
        self.is_buyable = False


class Utility(object):
    """Provides a class for all utilities. These will have specific functions
    regarding rent - what with the rolling dice thingo. """
    def __init__(self, name, position, cost):
        self.name = name
        self.position = position
        self.cost = cost
        self.is_utility = True
        self.is_owned = False
        self.owner = 0


class CommunityChestCard(SpecialRealEstate):
    """Imports most of its stuff from SpecialRealEstate. Only difference is
    that the is_chest_card token is set to true. A function will use this."""
    def __init__(self, name, position):
        SpecialRealEstate.__init__(self, name, position)
        self.is_chest_card = True


class ChanceCard(SpecialRealEstate):
    """Imports most of its stuff from SpecialRealEstate. Only difference is
    that the is_chance_card token is set to true. A function will use this."""
    def __init__(self, name, position):
        SpecialRealEstate.__init__(self, name, position)
        self.is_chance_card = True


class Go(SpecialRealEstate):
    """Imports most of its stuff from SpecialRealEstate. Only difference is
    that the is_go token is set to true. A function will use this."""
    def __init__(self, name, position):
        SpecialRealEstate.__init__(self, name, position)
        self.is_go = True


class GoToJail(SpecialRealEstate):
    """Imports most of its stuff from SpecialRealEstate. Only difference is
    that the is_go_to_jail token is set to true. A function will use this."""
    def __init__(self, name, position):
        SpecialRealEstate.__init__(self, name, position)
        self.is_go_to_jail = True


class FreeParking(SpecialRealEstate):
    """Imports most of its stuff from SpecialRealEstate. Only difference is
    that the is_free_parking token is set to true. A function will use this."""
    def __init__(self, name, position):
        SpecialRealEstate.__init__(self, name, position)
        self.is_free_parking = True


class TaxCard(SpecialRealEstate):
    """Imports most of its stuff from SpecialRealEstate. Only difference is
    that the is_tax token is set to true. A function will use this."""
    def __init__(self, name, position):
        SpecialRealEstate.__init__(self, name, position)
        self.is_tax = True


"""Now we begin the tedious process of creating 40 different spaces. While it's
certainly quicker than if we hadn't used classes, it's still going to take a
while. Also, I'll need some way of determining how the board works properly.
I'll probably have a list of numbers that relate to the locations
"""
old_kent = RealEstate("Old Kent Road", 1, 60000, 2000, 10000, 30000, 90000, 160000, 250000, "brown")
whitechapel = RealEstate("Whitechapel Road", 3, 60000, 4000, 20000, 60000, 180000, 320000, 450000, "brown")

angel_islington = RealEstate("The Angel Islington", 6, 100000, 6000, 30000, 90000, 270000, 400000, 550000, "cyan")
euston = RealEstate("Euston Road", 8, 100000, 6000, 30000, 90000, 270000, 400000, 550000, "cyan")
pentonville = RealEstate("Pentonville Road", 9, 120000, 8000, 40000, 100000, 300000, 450000, 600000, "cyan")

pall_mall = RealEstate("Pall Mall", 11, 140000, 10000, 50000, 150000, 450000, 625000, 750000, "pink")
whitehall = RealEstate("Whitehall", 13, 140000, 10000, 50000, 150000, 450000, 625000, 750000, "pink")
northumberland = RealEstate("Northumberland Avenue", 14, 160000, 12000, 60000, 180000, 500000, 700000, 900000, "pink")

bow = RealEstate("Bow Street", 16, 180000, 14000, 70000, 200000, 550000, 750000, 950000, "orange")
marlborough = RealEstate("Marlborough Street", 18, 180000, 14000, 70000, 200000, 550000, 750000, 950000, "orange")
vine = RealEstate("Vine Street", 19, 200000, 16000, 80000, 220000, 600000, 800000, 1000000, "orange")

strand = RealEstate("The Strand", 21, 220000, 18000, 90000, 250000, 700000, 875000, 1050000, "red")
fleet = RealEstate("Fleet Street", 23, 220000, 18000, 90000, 250000, 700000, 875000, 1050000, "red")
trafalgar = RealEstate("Trafalgar Square", 24, 240000, 20000, 100000, 300000, 750000, 925000, 1100000, "red")

leicester = RealEstate("Leicester Square", 26, 260000, 22000, 110000, 330000, 800000, 975000, 1150000, "yellow")
coventry = RealEstate("Coventry Street", 27, 260000, 22000, 110000, 330000, 800000, 975000, 1150000, "yellow")
piccadilly = RealEstate("Piccadilly", 29, 280000, 22000, 120000, 360000, 850000, 1025000, 1200000, "yellow")

regent = RealEstate("Regent Street", 31, 300000, 26000, 130000, 390000, 900000, 1100000, 1275000, "green")
oxford = RealEstate("Oxford Street", 32, 300000, 26000, 130000, 390000, 900000, 1100000, 1275000, "green")
bond = RealEstate("Bond Street", 34, 320000, 28000, 150000, 450000, 1000000, 1200000, 1400000, "green")

park_lane = RealEstate("Park Lane", 37, 350000, 35000, 175000, 500000, 1100000, 1300000, 1500000, "blue")
mayfair = RealEstate("Mayfair", 39, 400000, 50000, 200000, 600000, 1400000, 1700000, 2000000, "blue")

marylebone = Railroads("Marylebone Station", 5)
fenchurch = Railroads("Fenchurch Station", 15)
kings_cross = Railroads("Kings Cross Station", 25)
liverpool = Railroads("Liverpool Street Station", 35)

go_space = Go("Global Offices", 0)
visiting_jail = FreeParking("Jail", 10)
free_parking_space = FreeParking("Business Management Incorporated", 20)
go_to_jail_space = GoToJail("Go To Jail", 30)

chest_space_1 = CommunityChestCard("Community Chest", 2)
chest_space_2 = CommunityChestCard("Community Chest", 17)
chest_space_3 = CommunityChestCard("Community Chest", 33)

chance_space_1 = ChanceCard("Chance", 7)
chance_space_2 = ChanceCard("Chance", 22)
chance_space_3 = ChanceCard("Chance", 36)

tax_space_1 = TaxCard("Income Tax", 4)
tax_space_2 = TaxCard("Property Tax", 38)

electric_company = Utility("Electric Company", 12, 150000)
water_works = Utility("Water Works", 28, 150000)

board = {0:go_space,
         1:old_kent,
         2:chest_space_1,
         3:whitechapel,
         4:tax_space_1,
         5:marylebone,
         6:angel_islington,
         7:chance_space_1,
         8:euston,
         9:pentonville,
         10:visiting_jail,
         11:pall_mall,
         12:electric_company,
         13:whitehall,
         14:northumberland,
         15:fenchurch,
         16:bow,
         17:chest_space_2,
         18:marlborough,
         19:vine,
         20:free_parking_space,
         21:strand,
         22:chance_space_2,
         23:fleet,
         24:trafalgar,
         25:kings_cross,
         26:leicester,
         27:coventry,
         28:water_works,
         29:piccadilly,
         30:go_to_jail_space,
         31:regent,
         32:oxford,
         33:chest_space_3,
         34:bond,
         35:liverpool,
         36:chance_space_3,
         37:park_lane,
         38:tax_space_2,
         39:mayfair,
        }

"""Now we create the factions. I'll probably have to figure out how to deal with
special winning conditions. Probably a function to determine at the end of each
turn?

Also, a random name generation schema for the factions - using JSON dicts probably
- would be cool. But that's for later.
"""

aristocratic_faction = Faction("The Bavarian Illuminati", 1)
patternmaker_faction = Faction("The Globalist Council", 2)
automotive_faction = Faction("Castiglione Automotive Group", 3)
anarchist_faction = Faction("Class Soldiers", 4)
infrastructure_faction = Faction("RJFC Infrastructure", 5)
    #Heh. Note to self: RJFC stands for Russo-Japanese Fishing Colony
slumlord_faction = Faction("Tenament Holdings", 6)
alien_faction = Faction("The Greys", 7)
tramp_faction = Faction("Hobo Bob", 8)

faction_ids = {1:aristocratic_faction,
               2:patternmaker_faction,
               3:automotive_faction,
               4:anarchist_faction,
               5:infrastructure_faction,
               6:slumlord_faction,
               7:alien_faction,
               8:tramp_faction
              }

def turn(player):
    dice = random.randint(1,6)+random.randint(1,6)
    player.position = (player.position + dice)%40
    property_here = board[player.position]
    print("%s moves to %s." % (player.name, property_here.name))
    if hasattr(property_here, "cost") == True:        
        if property_here.is_owned == False:
            if player.money >= property_here.cost:
                player.money = player.money - property_here.cost
                property_here.is_owned = True
                property_here.owner = player.idnumber
                print("%s buys %s for $%s." % (player.name, property_here.name, property_here.cost))
                print("%s has $%s left." % (player.name, player.money))
            if player.money < property_here.cost:
                print("%s is unable to buy land at %s." % (player.name, property_here.cost)) 
        elif property_here.is_owned == True:
            print("The property at %s is owned by %s." % (property_here.name, faction_ids[property_here.owner].name))    
    else:
        print("NOPE")

