'''Project one create a class
Adding this comment 
demostrating editing code.
'''

print(f"__name__ in my home file: {__name__}")

class Home:

    def __init__(
        self,
        house_color: str = "green",
        front_door_color: str = "red", 
        number_of_windows: int = 5,
        number_of_bedrooms: int = 3,
        number_of_bathrooms: int = 2,
        number_of_car_garage: int = 2,
        air_conditioning = "Central Air",
        open_door: bool = False
        ):

        self.house_color = house_color
        self.front_door_color = front_door_color
        self.number_of_windows = number_of_windows
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.number_of_car_garage = number_of_car_garage
        self.air_conditioning = air_conditioning
        self.open_door = open_door


    def locks_the_door (self):
        '''Locks the door, closed the door atribute of the class house.'''
        self.open_door = not self.open_door


    def __str__(self) -> str:
        '''Represent a house as a string or return that the door is locked.'''
        if self.open_door == False:
            outcome = "HOUSE IS LOCKED, plese enter 2 to unlocked the door and display your new home!"
        else:
            outcome =\
            f"++++++++++++++++++++++++++++++++++++++++++++++++++\n"\
            f"Your new home color is: {self.house_color}\n"\
            f"Your front door color is: {self.front_door_color}\n"\
            f"You have {self.number_of_windows} windows in your new home \n"\
            f"Your new home have {self.number_of_bedrooms} bedrooms\n"\
            f"And {self.number_of_bathrooms} bathroom\n"\
            f"With a {self.number_of_car_garage} cars size garage\n"\
            f"Your new home air conditioning systems: {self.air_conditioning}\n"\
            

        return outcome
    

        
            


        




