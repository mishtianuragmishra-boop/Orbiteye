import requests
import csv
from io import StringIO
url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=csv"
response = requests.get(url)
print(response.status_code)
#print(response.text[:1000])
if response.status_code == 200:
    csv_text=StringIO(response.text)
    reader=csv.DictReader(csv_text)
    count=0
    for row in reader:
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
        count+=1
        if count==5:
            break
            
    with open("data/starlink.csv","w",encoding="utf-8") as f:
        f.write(response.text)
    
    print("Download successful")
    print("Saved as data")
else:
    print("Download failed")
    