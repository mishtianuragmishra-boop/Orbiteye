import csv
from datetime import datetime

def bstar():

    BSTARavg=0

    highest_BSTAR=float("-inf")
    lowest_BSTAR=float("inf")

    highestBSTAR=""
    lowestBSTAR=""

    sum_BSTAR=0
    tsat=0

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

    return {
        "Average BSTAR": BSTARavg,
        "Total satellites": tsat,
        "Highest BSTAR": highest_BSTAR,
        "Satellite with highest BSTAR": highestBSTAR,
        "Lowest BSTAR": lowest_BSTAR,
        "Satellite with lowest BSTAR": lowestBSTAR,
    }
    
def eccentricity():

    eccavg=0

    highest_ecc=float("-inf")
    lowest_ecc=float("inf")

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
        return{
            "Average Eccentricity": eccavg,
            "Total satellites": tsat,
            "Highest Eccentricity": highest_ecc,
            "Satellite with highest Eccentricity": highest_e,
            "Lowest Eccentricity": lowest_ecc,
            "Satellite with lowest Eccentricity": lowest_e,
        }    
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
    return{
        "Average Epoch": avgepoch,
        "Total satellites": tsat,
        "Highest Epoch": highest_epoch,
        "Satellite with highest Epoch": highestepoch,
        "Lowest Epoch": lowest_epoch,
        "Satellite with lowest Epoch": lowestepoch,
    }

def inclination():

    highest_inc=float("-inf")
    lowest_inc=float("inf")

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
    return{
        "Average Inclination": incavg,
        "Total satellites": tsat,
        "Highest Inclination": highest_inc,
        "Satellite with highest Inclination": highinc,
        "Lowest Inclination": lowest_inc,
        "Satellite with lowest Inclination": lowinc,
    }
def meanmotion():
    highest_meanmotion=float("-inf")
    lowest_meanmotion=float("inf")
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

    meanmotion_avg=sum_meanmotion/tsat

    return {
        "Average Mean Motion": meanmotion_avg,
        "Total satellites": tsat,
        "Highest Mean Motion": highest_meanmotion,
        "Satellite with highest Mean Motion": highest_mmsat,
        "Lowest Mean Motion": lowest_meanmotion,
        "Satellite with lowest Mean Motion": lowest_mmsat,
    }
