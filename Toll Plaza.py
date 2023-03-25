# Program to be used by worker at Toll Plaza.
from datetime import datetime

dict_veh = {"C": "Car", "J": "Jeep", "B": "Bus", "T": "Truck", "M": "Mini Bus",
            "H": "Heavy vehicle"}
prices_single = {"C": 90, "J": 90, "B": 105, "T": 100, "M": 95, "H": 120}
prices_double = {"C": 150, "J": 150, "B": 180, "T": 170, "M": 170, "H": 200}
database_single = {}
database_double = {}
database_vip = {}
ID_list = list(range(22000, 22100))


def balance(total, paid):
    return paid - total


def detail_ss_entry(vehicle):
    global database_single, ID_list
    number = input("Enter vehicle number:")
    print("Total amount to be paid is:", prices_single[vehicle])
    while True:
        paid = int(input("Enter amount paid:"))
        if paid < prices_single[vehicle]:
            print("Amount paid is not enough.")
            continue
        else:
            break
    bal = balance(prices_single[vehicle], paid)
    print("Amount to be returned is", bal)
    entry_date = str(datetime.now().date())
    entry_time = str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute)
    print("       --- Entry Provided --- ")
    id_par = ID_list.pop(0)
    database_single[id_par] = [number, dict_veh[vehicle], entry_date, entry_time]
    ps_entry(id_par, vehicle, number, "Single", prices_single[vehicle], paid, bal, entry_date, entry_time)


def detail_sd_entry(vehicle):
    global database_double, ID_list
    number = input("Enter vehicle number:")
    print("Total amount to be paid is:", prices_double[vehicle])
    while True:
        paid = int(input("Enter amount paid:"))
        if paid < prices_double[vehicle]:
            print("Amount paid is not enough.")
            continue
        else:
            break
    bal = balance(prices_double[vehicle], paid)
    print("Amount to be returned is", bal)
    entry_date = str(datetime.now().date())
    entry_time = str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute)
    print(" --- Entry Provided --- ")
    id_par = ID_list.pop(0)
    database_double[id_par] = [number, dict_veh[vehicle], entry_date, entry_time, "False"]
    ps_entry(id_par, vehicle, number, "Double", prices_single[vehicle], paid, bal, entry_date, entry_time)


def ps_entry(id_entry, vehicle, number, ttype, price, paid, bal, entry_date, entry_time):
    print("_"*50)
    print("National Highway Authority".center(50), sep="")
    print("INDIA".center(50), sep="")
    print()
    print("Entry ID:".rjust(20, " "), id_entry, sep="")
    print("Vehicle Type:".rjust(20, " "), dict_veh[vehicle], sep="")
    print("Vehicle number :".rjust(20, " "), number, sep="")
    print("Entry type :".rjust(20, " "), ttype,  sep="")
    print("Amount:".rjust(20, " "), "Rs.", price, sep="")
    print("Paid:".rjust(20, " "), "Rs.", paid,  sep="")
    print("Balance:".rjust(20, " "), "Rs.", bal, sep="")
    print("                               Date:{:<18}".format(entry_date), sep="")
    print("                               Time:{:<18}".format(entry_time), sep="")
    print("_"*50)


def simple_entry():
    print("C for Car, J for Jeep, B for Bus, T for Truck, A for Ambulance,\n M for\
 Mini Bus, H for other heavy vehicle.")
    while True:
        vehicle = input("Enter the vehicle Type:")
        if vehicle not in {"C", "J", "B", "T", "A", "M", "H"}:
            print("Not a valid response for vehicle type.")
            continue
        else:
            break
    if vehicle == "A":
        amb = input("Enter vehicle number :")
        print(" -- Entry Provided to ambulance number -{}. -- ".format(amb))
        return None
    while True:
        s_or_d = input("Single(S) or double(D) :")
        if s_or_d not in {"S", "D"}:
            print("Error! Only enter \"S\" or \"D\"")
            continue
        else:
            break
    if s_or_d == "S":
        detail_ss_entry(vehicle)
    elif s_or_d == "D":
        detail_sd_entry(vehicle)


def re_entry():
    while True:
        id_re = int(input("Enter the ID:"))
        if id_re in database_double.keys():
            database_double[id_re][4] = "True"
            print(" -- Entry provided --")
            print("_" * 50)
            print("National Highway Authority".center(50), sep="")
            print("INDIA".center(50), sep="")
            print()
            print("Entry ID:".rjust(20, " "), id_re, sep="")
            print("Vehicle Type:".rjust(20, " "), database_double[id_re][1], sep="")
            print("Vehicle number :".rjust(20, " "), database_double[id_re][0], sep="")
            print("Previous entry date :".rjust(20, " "), database_double[id_re][2], sep="")
            print("Previous entry time :".rjust(20, " "), database_double[id_re][3], sep="")
            print("Date:".rjust(30, " "), str(datetime.now().date()), sep="")
            print("Time:".rjust(30, " "), str(datetime.now().hour), ":", str(datetime.now().minute), sep="")
            print("_" * 50)
            break
        else:
            print("NO such entry found in the database.")
            break


def vip_entry():
    print("C for Car, J for Jeep, B for Bus, T for Truck,\n M for\
Mini Bus, H for other heavy vehicle.")
    while True:
        veh_type = input("Enter vehicle type:")
        if veh_type not in {"C", "J", "B", "T", "M", "H"}:
            print("Not a valid response!")
            continue
        else:
            break
    number = input("Enter vehicle number:")
    desig = input("Enter designation of person:")
    entry_date = str(datetime.now().date())
    entry_time = str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute)
    while True:
        print("Do you confirm that this person hold authority to bypass without paying?")
        print("Type C to Confirm and D to Decline :", end="")
        confirm = input()
        match confirm:
            case "C":
                id_entry = ID_list.pop(0)
                print("_" * 50)
                print("National Highway Authority".center(50), sep="")
                print("INDIA".center(50), sep="")
                print()
                print("Entry ID:".rjust(20, " "), id_entry, sep="")
                print("Vehicle Type:".rjust(20, " "), dict_veh[veh_type], sep="")
                print("Vehicle number:".rjust(20, " "), number, sep="")
                print("\n      --This entry is provided as VIP entry -- ", sep="")
                print("Authority of person:".rjust(20, " "), desig, sep="")
                print("Authority of person:".rjust(20, " "), desig, sep="")
                print()
                print("                         Date:{:<18}".format(entry_date), sep="")
                print("                         Time:{:<18}".format(entry_time), sep="")
                print("_" * 50)
                list1 = [number,  dict_veh[veh_type], desig, entry_date, entry_time]
                database_vip[id_entry] = list1
                break
            case "D":
                print(" -- Entry declined -- ")
                break
            case _:
                print("Not a valid response.")


def print_det():
    print("Single Entry : ")
    print("|{:<10}|{:^15}|{:^15}|{:^14}|{:^14}|".format("ID", "Vehicle number", "Vehicle Type", "Entry date", "Entry time"))
    for i in database_single.keys():
        print("|{:<10}|{:^15}|{:^15}|{:^14}|{:^14}|".format(i, database_single[i][0],
                                                            database_single[i][1], database_single[i][2], database_single[i][3]))
    print("\nDouble Entry : ")
    print("|{:<10}|{:^15}|{:^15}|{:^14}|{:^14}|{:8}|".format("ID", "Vehicle number", "Vehicle Type", "Entry date", "Entry time", "RE-enter"))
    for i in database_double.keys():
        print("|{:<10}|{:^15}|{:^15}|{:^14}|{:^14}|{:8}|".format(i, database_double[i][0], database_double[i][1],
                                                                 database_double[i][2], database_double[i][3], database_double[i][4]))
    print("\nVIP Entry : ")
    print("|{:<10}|{:^15}|{:^15}|{:^15}|{:^14}|{:^14}|".format("ID", "Vehicle number",
                                                               "Vehicle Type", "Designation", "Entry date", "Entry time"))
    for i in database_vip.keys():
        print("|{:<10}|{:^15}|{:^15}|{:^15}|{:^14}|{:^14}|".format(i, database_vip[i][0], database_vip[i][1],
                                                                   database_vip[i][2], database_vip[i][3], database_vip[i][4]))


while True:
    print()
    print("E to do entry, R for re-entry, V for VIP entry , Q to quit and P to print entry details.")
    process = input("Select process :")
    match process:
        case "E":
            simple_entry()
        case "R":
            re_entry()
        case "V":
            vip_entry()
        case "P":
            print_det()
        case "Q":
            break
        case _:
            print("Not a valid response!")
            continue
