import csv

def searchbyname(sname):
    found = False
    with open("data/starlink.csv","r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        match = 0
        for row in reader:
            if  sname.lower() in row["OBJECT_NAME"].lower():
                match += 1
                print("Satellite found")
                print(". . . . .. more info upcoming")
                return{
                    "Name": row["OBJECT_NAME"],
                    "ID": row["OBJECT_ID"],
                    "EPOCH": row["EPOCH"],
                    "MEAN MOTION": row["MEAN_MOTION"],
                    "ECCENTRICITY": row["ECCENTRICITY"],
                    "INCLINATION": row["INCLINATION"],
                    "RA OF ASC NODE": row["RA_OF_ASC_NODE"],
                    "ARG OF PERICENTER": row["ARG_OF_PERICENTER"],
                    "MEAN ANOMALY": row["MEAN_ANOMALY"],
                    "EPHEMERIS TYPE": row["EPHEMERIS_TYPE"],
                    "CLASSIFICATION TYPE": row["CLASSIFICATION_TYPE"],
                    "NORAD CAT ID": row["NORAD_CAT_ID"],
                    "ELEMENT SET NO": row["ELEMENT_SET_NO"],
                    "REV_AT_EPOCH": row["REV_AT_EPOCH"],
                    "BSTAR": row["BSTAR"],
                    "MEAN MOTION DOT": row["MEAN_MOTION_DOT"],
                    "MEAN MOTION DDOT": row["MEAN_MOTION_DDOT"]
                }
                found = True
                break
    print("=====Total matches=====",match)

def searchbynoradid(norad):
    with open("data/starlink.csv","r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        match = 0
        for row in reader:
            if  norad == row["NORAD_CAT_ID"]:
                match += 1
                print("Satellite found")
                print(". . . . .. more info upcoming")
                return{
                    "Name": row["OBJECT_NAME"],
                    "ID": row["OBJECT_ID"],
                    "EPOCH": row["EPOCH"],
                    "MEAN MOTION": row["MEAN_MOTION"],
                    "ECCENTRICITY": row["ECCENTRICITY"],
                    "INCLINATION": row["INCLINATION"],
                    "RA OF ASC NODE": row["RA_OF_ASC_NODE"],
                    "ARG OF PERICENTER": row["ARG_OF_PERICENTER"],
                    "MEAN ANOMALY": row["MEAN_ANOMALY"],
                    "EPHEMERIS TYPE": row["EPHEMERIS_TYPE"],
                    "CLASSIFICATION TYPE": row["CLASSIFICATION_TYPE"],
                    "NORAD CAT ID": row["NORAD_CAT_ID"],
                    "ELEMENT SET NO": row["ELEMENT_SET_NO"],
                    "REV_AT_EPOCH": row["REV_AT_EPOCH"],
                    "BSTAR": row["BSTAR"],
                    "MEAN MOTION DOT": row["MEAN_MOTION_DOT"],
                    "MEAN MOTION DDOT": row["MEAN_MOTION_DDOT"]
                }
    

