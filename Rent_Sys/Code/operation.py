


import write




# Function to check if a land is available for rent
def is_land_available(kitta_no):
    with open("Land_field.txt", "r") as file:
        for line in file:
            splitted_data = line.rstrip().split(",")
            if kitta_no in splitted_data and splitted_data[-1] == "Available":
                return True
    return False


# Function to check if a land is already rented
def is_land_rented(kitta_no):
        with open("Land_field.txt", "r") as file:
            for line in file:
                splitted_data = line.rstrip().split(",")
                if kitta_no in splitted_data and splitted_data[-1] == "Not-Available":
                    return True
        return False


# Function to calculate the cost of renting a land for a given number of months
def calculate_cost(kitta_no,months):
    with open ("Land_field.txt", "r") as file:
        for line in file:
            splitted_data = line.strip().split(",")
            if kitta_no in splitted_data:
                cost = int(splitted_data[4]) * months
                return cost



# this is for calculatin fine
def calculate_fine(rentedmonth, returnedmonth):
    fine = 0
    months_exceeded = returnedmonth - rentedmonth
    if months_exceeded > 0:
        fine = months_exceeded * 5000 
        return fine
    


            

# Function to generate a rent receipt for a rented land

def generate_receipt(kitta_no, rented_months, customer_name, cost, name_of_city, direction, area):
   
    with open(customer_name + ".txt", "a") as file:
        file.write("=========================================\n")
        file.write("             Land Rent Receipt            \n")
        file.write("=========================================\n")
        file.write(f"Kitta No: {kitta_no}\n")
        file.write(f"Name: {customer_name}\n")
        file.write(f"Rented Months: {rented_months}\n")
        file.write(f"City: {name_of_city}\n")
        file.write(f"Direction: {direction}\n")
        file.write(f"Area: {area} sqft\n")
        file.write(f"Rent Amount: Rs. {cost}\n")
        file.write("=========================================\n")

# Function to check if a kitta number exists in the Land_field.txt file

def kitta_exists(kitta_no):
    with open("Land_field.txt", "r") as file:
        for line in file:
            splitted_data = line.rstrip().split(",")
            if kitta_no in splitted_data:
                return True
    return False

# Function to handle the return of a rented land

def return_land():
    kitta_no=input("Enter kitta number: ")
    if not kitta_exists(kitta_no):
        print("Kitta number does not exist")
        return



    if(int(kitta_no)<0):
        print("Kitta number should be positive")
        return
    
    if not is_land_rented(kitta_no):
        print("Land is not rented yet")
        return
    rented_months=int(input("Enter rented months: "))
    return_months=int(input("Enter returned months: "))
    name = str(input("Enter name: "))
    fine = calculate_fine(rented_months,return_months)
    cost = calculate_cost(kitta_no, rented_months)
    with open ("Land_field.txt", "r") as file:
        for line in file:
            splitted_data = line.strip().split(",")
            if kitta_no in splitted_data:
                
                name_of_city = splitted_data[1]
                direction = splitted_data[2] 
                area = splitted_data[3]
                return_invoice(name,kitta_no,rented_months,return_months,cost,fine,area,direction,name_of_city)
                write.return_land(kitta_no)
                with open(name+".txt", "r") as file:
                    print(file.read())
                return
           
            
# Function to generate an invoice for a returned land

def return_invoice(name, kitta_no, rented_months, return_months, cost, fine, area, direction, name_of_city):
   
    with open(name + ".txt", "a") as file:
        file.write("====================================================\n")
        file.write("                 Returned Land Invoice               \n")
        file.write("====================================================\n")
        file.write(f"Kitta No: {kitta_no}\n")
        file.write(f"Name: {name}\n")
        file.write(f"Rented Months: {rented_months}\n")
        file.write(f"Returned month: {return_months}\n")
        file.write(f"City: {name_of_city}\n")
        file.write(f"Direction: {direction}\n")
        file.write(f"Fine Amount: Rs. {fine}\n")
        file.write(f"Area: {area} sqft\n")
        file.write(f"Rent Amount: Rs. {cost}\n")
        file.write("----------------------------------------------------\n")
        file.write(f"Final Cost: Rs. {cost + fine}\n")
        file.write("====================================================\n\n\n\n")
               




# Function to handle the renting of a land

def rent_land():
    kitta_no=input("Enter kitta number: ")
    if not kitta_exists(kitta_no):
        print("Kitta number does not exist")
        return
    
    if(int(kitta_no)<0):
        print("Kitta number should be positive")
        return
    
    
    
    if is_land_rented(kitta_no):
        print("Land is not available")
        return
    rente_months=int(input("Enter rented months: "))
    name =input("Enter name: ")
  
    cost = calculate_cost(kitta_no, rente_months)
    with open ("Land_field.txt", "r") as file:
        for line in file:
            splitted_data = line.strip().split(",")
            if kitta_no in splitted_data:
                
                name_of_city = splitted_data[1]
                direction = splitted_data[2] 
                area = splitted_data[3]
                generate_receipt(kitta_no,rente_months,name,cost,name_of_city,direction,area)
                write.rent_land(kitta_no)

                with open(name+".txt", "r") as file:
                    print(file.read())
                return
        
