import csv
from datetime import datetime



def bstar():

    BSTARavg=0

    highest_BSTAR=0
    lowest_BSTAR=999

    highestBSTAR=""
    lowestBSTAR=""

    sum_BSTAR=0
    tsat=0

    found=False

    with open("data/starlink.csv","r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:#taking total number of satellites
            BSTAR=float(row["BSTAR"])

            sum_BSTAR+= BSTAR
            tsat += 1

            if BSTAR > highest_BSTAR:
                highest_BSTAR=BSTAR
                highestBSTAR=row["OBJECT_NAME"]

            if BSTAR < lowest_BSTAR:
                lowest_BSTAR=BSTAR
                lowestBSTAR=row["OBJECT_NAME"]

    BSTARavg=sum_BSTAR/tsat

    print("The average BSTAR is:",BSTARavg)
    print("Total number of satellites",tsat)

    print(
        "=====Highest BSTAR=====" ,highest_BSTAR,
        "=====Satellite=====",highestBSTAR
        )

    print(
        "=====Lowest BSTAR=====",lowest_BSTAR,
        "=====Satellite=====",lowestBSTAR
        )
    
def eccentricity():

    eccavg=0

    highest_ecc=0
    lowest_ecc=999

    highest_e=""
    lowest_e=""

    sum_ecc=0
    tsat=0

    with open("data/starlink.csv","r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:#taking total number of satellites
            ecc=float(row["ECCENTRICITY"])

            sum_ecc += ecc
            tsat += 1

            if ecc > highest_ecc:
                highest_ecc= ecc
                highest_e=row["OBJECT_NAME"]

            if ecc < lowest_ecc:
                lowest_ecc=ecc
                lowest_e=row["OBJECT_NAME"]

        eccavg=sum_ecc/tsat

        print("The average Eccentricity is:",eccavg)
        print("Total number of satellites",tsat)

        print(
            "=====Highest Eccentricity=====" ,highest_ecc,
            "=====Satellite=====",highest_e
            )

        print(
            "=====Lowest Eccentricity=====",lowest_ecc,
            "=====Satellite=====",lowest_e
             )
    
def epoch():

    highest_epoch=None
    lowest_epoch=None

    highestepoch=""
    lowestepoch=""

    sumepoch=0

    tsat=0

    with open("data/starlink.csv","r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:#taking total number of satellites
            epoch=datetime.fromisoformat(row["EPOCH"].replace("Z","+00:00"))

            sumepoch+=epoch.timestamp()
            tsat+=1

            if  highest_epoch is None or epoch > highest_epoch:
                highest_epoch=epoch
                highestepoch=row["OBJECT_NAME"]

            if lowest_epoch is None  or epoch < lowest_epoch:
                lowest_epoch=epoch
                lowestepoch=row["OBJECT_NAME"]

    avg_timestamp=sumepoch/tsat
    avgepoch=datetime.fromtimestamp(avg_timestamp)
    print("=====Average EPOCH=====",avgepoch)

    print(
        "=====Newest epoch=====" ,highest_epoch,
        "=====Satellite=====",highestepoch
            )

    print(
        "=====Oldest epoch=====",lowest_epoch,
        "=====Satellite=====",lowestepoch
            )
            
def inclination():

    highest_inc=0
    lowest_inc=999

    highinc=""
    lowinc=""

    sum_inc=0
    tsat=0

    with open("data/starlink.csv","r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:#taking total number of satellites
            inclination=float(row["INCLINATION"])
            sum_inc+= inclination
            tsat+=1
            if inclination>highest_inc:
                highest_inc=inclination
                highinc=row["OBJECT_NAME"]

            if inclination<lowest_inc:
                lowest_inc=inclination
                lowinc=row["OBJECT_NAME"]

    incavg=sum_inc/tsat

    print("=====The average inclination is=====",incavg)
    print("=====Total number of satellites=====",tsat)

    print(
        "=====Highest incllination=====" ,highest_inc,
        "=====Satellite=====",highinc
        )

    print(
        "=====Lowest Inclination=====",lowest_inc,
        "=====Satellite=====",lowinc
        )
        
def meanmotion():
    highest_meanmotion=0
    lowest_meanmotion=999
    highest_mmsat=""
    lowest_mmsat=""

    sum_meanmotion=0
    tsat=0
    with open("data/starlink.csv","r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:#taking total number of satellites
            meanmotion=float(row["MEAN_MOTION"])

            sum_meanmotion += meanmotion
            tsat += 1

            if meanmotion > highest_meanmotion:
                highest_meanmotion=meanmotion
                highest_mmsat=row["OBJECT_NAME"]

            if meanmotion < lowest_meanmotion:
                lowest_meanmotion=meanmotion
                lowest_mmsat=row["OBJECT_NAME"]

    meanmotion=sum_meanmotion/tsat
    print(f"The average Mean Motion is: {meanmotion:4f}")
    print("=====Total number of satellites=====",tsat)
    print("=====Highest Mean Motion=====" ,highest_meanmotion,
          "=====Satellite=====",highest_mmsat)
    print("=====Lowest Mean Motion=====",lowest_meanmotion,
          "=====Satellite=====",lowest_mmsat)