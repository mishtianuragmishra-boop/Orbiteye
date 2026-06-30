import csv

def searchbyname():
    sname=input("Enter the satellite name you're searching for:")
    found = False
    with open("data/starlink.csv","r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        match = 0
        for row in reader:
            if  sname.lower() in row["OBJECT_NAME"].lower():
                match += 1
                print("Satellite found")
                print(". . . . .. more info upcoming")
                print("Name",row["OBJECT_NAME"])
                print("ID",row["OBJECT_ID"])
                print("EPOCH",row["EPOCH"])
                print("MEAN MOTION",row["MEAN_MOTION"])
                print("ECCENTRICITY",row["ECCENTRICITY"])
                print("INCLINATION",row["INCLINATION"])
                print("RA OF ASC NODE",row["RA_OF_ASC_NODE"])
                print("ARG OF PERICENTER",row["ARG_OF_PERICENTER"])
                print("MEAN ANOMALY",row["MEAN_ANOMALY"])
                print("EPHEMERIS TYPE",row["EPHEMERIS_TYPE"])
                print("CLASSIFICATION TYPE",row["CLASSIFICATION_TYPE"])
                print("NORAD CAT ID",row["NORAD_CAT_ID"])
                print("ELEMENT SET NO",row["ELEMENT_SET_NO"])
                print("REV_AT_EPOCH",row["REV_AT_EPOCH"])
                print("BSTAR",row["BSTAR"])
                print("MEAN MOTION DOT",row["MEAN_MOTION_DOT"])
                print("MEAN MOTION DDOT",row["MEAN_MOTION_DDOT"])
                found = True
                break
    print("=====Total matches=====",match)

def searchbynoradid():
    found = False
    with open("data/starlink.csv","r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        norad=None
        match = 0
        norad = input("Enter a NORAD ID:")
        for row in reader:
            if  norad == row["NORAD_CAT_ID"]:
                match += 1
                print("Satellite found")
                print(". . . . .. more info upcoming")
                print("Name",row["OBJECT_NAME"])
                print("ID",row["OBJECT_ID"])
                print("EPOCH",row["EPOCH"])
                print("MEAN MOTION",row["MEAN_MOTION"])
                print("ECCENTRICITY",row["ECCENTRICITY"])
                print("INCLINATION",row["INCLINATION"])
                print("RA OF ASC NODE",row["RA_OF_ASC_NODE"])
                print("ARG OF PERICENTER",row["ARG_OF_PERICENTER"])
                print("MEAN ANOMALY",row["MEAN_ANOMALY"])
                print("EPHEMERIS TYPE",row["EPHEMERIS_TYPE"])
                print("CLASSIFICATION TYPE",row["CLASSIFICATION_TYPE"])
                print("NORAD CAT ID",row["NORAD_CAT_ID"])
                print("ELEMENT SET NO",row["ELEMENT_SET_NO"])
                print("REV_AT_EPOCH",row["REV_AT_EPOCH"])
                print("BSTAR",row["BSTAR"])
                print("MEAN MOTION DOT",row["MEAN_MOTION_DOT"])
                print("MEAN MOTION DDOT",row["MEAN_MOTION_DDOT"])
                found = True
                break
    print("=====Total matches=====",match)

