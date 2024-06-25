
def rent_land(kitta_no):        #this is for renting land and its changes status
    with open("Land_field.txt", "r+") as file: 
        lines = file.readlines()
        for index, line in enumerate(lines):
            splitted_data = line.strip().split(",")
            if kitta_no in splitted_data:
                if splitted_data[-1]=="Available":
                    splitted_data[-1]="Not-Available"
                    lines[index] = ",".join(splitted_data) + "\n"
                    file.seek(0)
                    file.writelines(lines)
                    file.truncate()
                else:    
                    print("Land is already rented")
          


def return_land(kitta_no):# this function returns rented land and changes status
    with open("Land_field.txt", "r+") as file: 
        lines = file.readlines()
        for index, line in enumerate(lines):
            splitted_data = line.rstrip().split(",")
            if kitta_no in splitted_data:
                if splitted_data[-1]=="Not-Available":
                    splitted_data[-1]="Available"
                    lines[index] = ",".join(splitted_data) + "\n"
                    file.seek(0)
                    file.writelines(lines)
                    file.truncate()
                else:    
                    print("Land is already available")




