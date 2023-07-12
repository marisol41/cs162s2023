'''Project one create a class

'''

class Home:

    def __init__(
        self,
        house_color = "green",
        front_door_color = "red", 
        number_of_windows = 5,
        number_of_bedrooms = 3,
        number_of_bathrooms = 2,
        number_of_car_garage = 2,
        air_conditioning = "Central Air",
        open_door = False
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
    
print("\nHi welcome to Home.com On our site you can build the home of your dreams.")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#menu program
user_input = "-1"
first_time_choosing_home = True
while user_input != "0":  
    
# Display a menu and ask user for input, and validate the input.
    # print("\nHi welcome to Home.com On our site you can build the home of your dreams.")
    # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    good_input = False
    while good_input == False:
        user_input= input(
            f"Would you like to virtually build and visit your new home?\n"
            "\nChoose from the menu below:\n"\
            "Enter 1 :For YES I want to desing my new home! Please enter the specificacions you want for your new home\n" \
            "Enter 2 :Open the door\n" \
            "Enter 3 :For Tour and display my new home\n"
            "Enter 0 :For NO I dont want to build or visit a home Good bye!!\n" \
            
            )

        if user_input not in ["0","1","2","3"]:
            print("INVALID ENTRY! Please enter a valid option")
        else:
            good_input = True

        #run user's requested input
    if first_time_choosing_home:
        your_new_home = None

    if user_input == "1":
        #if 1 request inputs from user for Home object
        house_color = input(f"What color you prefer for your new house?\n")
        front_door_color = input(f"What color you prefer for the front door of your new home?\n")
        number_of_windows = input(f"How many windows you want in your new house?\n")
        number_of_bedrooms = input(f"How many bedrooms you want for your new home?\n ")
        number_of_bathrooms = input(f"How many bathrooms you want?\n")
        
        your_new_home = Home(house_color,front_door_color,number_of_windows,number_of_bedrooms,number_of_bathrooms)


    elif user_input =="2":
        #opens the door of your new home and let's you display the new home
        if your_new_home != None:
            your_new_home.locks_the_door()
            if your_new_home.open_door:
                print("The front door is now open, and you can virtually tour the house, enter 3 to display your new home!")
            else:
                print("The front door is locked. To unlock the door enter 2 first")
        else:
            print("YOU HAVE TO DESING YOUR NEW HOME FIRST!. Enter 1 to desing your new home!")

    elif user_input == "3":
        #if 2 display current home objectif it exists
        if your_new_home == None:
            print("THERE IS NOTHING TO DISPLAY YET! Please enter 1 to desing your home.")
        else:
            print(your_new_home)
    
    elif user_input == "0":
            #if 0 quit
        pass

    first_time_choosing_home = False
        
print("Thanks for visiting Homes.com Good bye!!")
                   
             
        
            
# your_new_home = Home()
# print(your_new_home)


        




