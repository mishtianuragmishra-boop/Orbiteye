from tracker import livetracker
from analytics import bstar,eccentricity,epoch,inclination,meanmotion
from tsearch import searchbyname,searchbynoradid
while True:
    print("\n==========ORBIT EYE==========")
    print("1 SEARCH")
    print("2 ANALYTICS")
    print("3 TRACKER")
    print("4 EXIT")
    choice=input("Enter your choice:")
    if choice=="1":
        print("\n SEARCH MENU")
        print("1 SEARCH BY NAME")
        print("2 SEARCH BY NORAD ID")
        option=input("Choose an option")
        if option=="1":
            searchbyname()
        elif option=="2":
            searchbynoradid()
    elif choice == "2":
        print("\n ANALYSIS MENU")
        print("======1 MEANMOTION=====")
        print("=====2 EPOCH=====")
        print("=====3 INCLINATION=====")
        print("=====4 ECCENTRICITY=====")
        print("=====5 BSTAR=====")
        option=input("=====Enter an option=====")
        if option=="1":
            meanmotion()
        elif option=="2":
            epoch()
        elif option=="3":
            inclination()
        elif option=="4":
            eccentricity()
        elif option=="5":
            bstar()
    elif choice=="3":
        livetracker()
    elif choice=="4":
        print("Hope you had a GREAT experience")
        break
    else:
        print("Invalid Choice")
