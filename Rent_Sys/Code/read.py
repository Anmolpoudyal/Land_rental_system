


def read_file(file_name):
    with open('file_name.txt','r') as file:
        anmol = file.readline()
        print(anmol)


#function to display all the rented lands
def rented_lands(file_name):
    with open('file_name.txt', 'r') as file:
        for line in file:
            splitted_data = line.strip().split(",")
            if "Not-available" in splitted_data: 
                print(line)

#function to display all the available lands
def available_land(file_name):
    with open(file_name,'r') as file:
        each_line=file.readlines()
        for line in each_line:
            if "Available" in line:
                print(line)




