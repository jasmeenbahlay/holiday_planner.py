# Welcome to the holiday planner!
print("""Welcome to the holiday planner!
      Please see the flights avaliable from the list below: """)

# Print the list of flights available
flight_list = {'Paris: 50','Rhodes: 80','Capeverde: 170','Cancun: 200','Hurghada: 150'}
print(flight_list)

# Ask user to input the city, number of nights and car rental period
city_flight = input("Please enter the city you will be flying to from the list below: ").capitalize()
        
num_nights = int(input("Please enter the number of nights you will be staying at a hotel: "))

rental_days = int(input("Please enter the number of days would you like to hire a car for: "))

# Calculate the hotel cost
def hotel_cost(num_nights):
    return num_nights * 100

# If/Else Statement to create a cost for the flight chosen from the list
def plane_cost(city_flight):
    if city_flight == 'Paris':
        return 50

    elif city_flight == 'Rhodes':
        return 80

    elif city_flight == 'Capeverde':
        return 170

    elif city_flight == 'Cancun':
        return 200
        
    elif city_flight == 'Hurghada':
        return 150

    else: 
        print('You have not entered a flight from the menu')

# Calculate the car rental cost
def car_rental(rental_days):
    return rental_days * 60

# Calculate the holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# Create variables using the functions
car_rentalprice = car_rental(rental_days)
hotel_costprice = hotel_cost(num_nights)
plane_costprice = plane_cost(city_flight)
total_cost = holiday_cost(hotel_costprice, plane_costprice, car_rentalprice)

# Display each cost individually and then the total cost
print(f'Your hotel cost is: {hotel_costprice}')

print(f'Your car rental will cost is: {car_rentalprice}')

print(f'Your flight will cost: {plane_costprice}')

print(f'Your total holiday cost is: {total_cost}')
