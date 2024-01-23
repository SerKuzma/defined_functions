# Pseudo code
# input:
    # city_flight with options
    # number of nights
    # car_rental_days
# define functions:
    # hotel_cost: night_price * num_nights
    # plane_cost: city_flight == True
                        # if city:

                        # elif city

                        # else False:
                            # error
    # if user choose to rent a car
    # car_rental_cost: car_rental_days * car_rental_price

    # if user refused from car, return to 0 and proceed to final output
    # total_holiday_cost = sum(hotel_cost, plane_cost, car_rental_cost)
# print (hotel_cost, total_holiday_cost, plane_cost, car_rental_cost = total_holiday_cost)

# ANSI escape codes for text color
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    
# Ask user for the destination and provides options
print()
print("Choose your destination, please: ")
print()
print("There are available flights to the next destinations: ")
print("---------------------------------------------------------")
print("Flight to London - type 'LON'")
print("Flight to Belfast - type 'BFS'")
print("Flight to Edinburgh - type 'EDI'")
print("---------------------------------------------------------")
city_flight = input(Colors.BLUE + "Type your choice, please: " + Colors.RESET).lower()
print()

# Define the function to calculate plane cost, depend on chosen destination
def plane_cost(city_flight):
    # List of valid input for cities
    valid_cities = ['lon', 'bfs', 'edi']
    while city_flight not in valid_cities:
        print(Colors.RED + "Incorrect input, check spelling and try again, please" + Colors.RESET)
        city_flight = input("Enter the correct city code (lon/bfs/edi): ").lower()
        print()
        
    if city_flight == 'lon':
        ticket_price_lon = get_non_negative_float_input("What's the price of ticket to London? £")
        print()
        ticket_price = ticket_price_lon
        return ticket_price
    
    elif city_flight == 'bfs':
        ticket_price_bfs = get_non_negative_float_input("What's the price of ticket to Belfast? £")
        print()
        ticket_price = ticket_price_bfs
        return ticket_price
    
    elif city_flight == 'edi':
        ticket_price_edi = get_non_negative_float_input("What's the price of ticket to Edinburgh? £")
        print()
        ticket_price = ticket_price_edi
        return ticket_price
    
# Define the function to calculate hotel cost
def hotel_cost(number_nights, night_price):
    money_for_hotel = number_nights * night_price
    return money_for_hotel

# Define the function to calculate car cost
def car_rental_cost(car_rental_days, car_rental_price):
    car_cost = car_rental_days * car_rental_price
    return car_cost

def get_non_negative_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print(Colors.RED + "Invalid input. Please enter a value grater than zero." + Colors.RESET)
        except ValueError:
            print(Colors.RED + "Invalid input. Please enter a valid number." + Colors.RESET)

def get_non_negative_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print(Colors.RED + "Please enter a value grater than zero." + Colors.RESET)
        except ValueError:
            print(Colors.RED + "Invalid input. Please enter a valid integer." + Colors.RESET)

# Call the function to calculate plane cost
ticket_price = plane_cost(city_flight)

# Call function for hotel cost
number_nights = get_non_negative_integer_input("How many nights would you like to stay in hotel? ")
print()
night_price = get_non_negative_float_input("What is the price per night? £")
print()
money_for_hotel = hotel_cost(number_nights, night_price)


# Define the function car rental cost with option to refuse from rental
def get_car_rental_cost():
    # List of valid choices
    valid_car_choices = ["y", "n"]

    # Ask the user if they want to rent a car
    car_choice = input("Would you like to rent a car? Y/N? ").lower()

    # Validate the user's input
    while car_choice not in valid_car_choices:
        print(Colors.RED + "Incorrect input, try again, please" + Colors.RESET)
        car_choice = input("Enter the correct option (y/n): ").lower()
        print()

     # Calculate car rental cost if the user chooses 'y'
    if car_choice == 'y':
        car_rental_days = get_non_negative_integer_input("For how many days would you like to rent a car? ")
        print()
        car_rental_price = get_non_negative_float_input("What's the price of car rental per day? £")
        print()
        return car_rental_days * car_rental_price
    
    # Return 0 if the user chooses 'n'
    elif car_choice == 'n':
        return 0

# Define variable for output and call the function 
car_cost = get_car_rental_cost()

# Calculate total cost
holiday_total_cost = ticket_price + money_for_hotel + car_cost  

# Print results
print("---------------------------------------------------------")
print(Colors.YELLOW + f"""You will spend for the holiday:\n £{ticket_price:.2f} on flights
 £{money_for_hotel:.2f} on the hotel \n £{car_cost:.2f} on car""" + Colors.RESET)
print("---------------------------------------------------------")
print(Colors.PURPLE + f"Total: £{holiday_total_cost:.2f}" + Colors.RESET)
print()
print(Colors.CYAN + "We wish you a lovely journey!!!" + Colors.RESET)
print()
