from skyfield.api import EarthSatellite,load

satname=input("Enter the satellite name")
with open("data/starlink.tle.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
    found=False
    for i in range(len(lines)):
        name=lines[i].strip()
        if name == satname:
            line1=lines[i+1].strip()
            line2=lines[i+2].strip()
            satname=EarthSatellite(line1,line2,name)
            ts=load.timescale()
            t=ts.now()
            geocenteric=satname.at(t)
            subpoint=geocenteric.subpoint()
            print()
            print("Satellite Name: ",satname.name)
            print("Satellite longitude : ",subpoint.longitude.degrees)
            print("Satellite latitude : ",subpoint.latitude.degrees)
            print("Altitude (in km) : ",subpoint.elevation.km)
            found=True
            break
    if found==False:
        print("satellite not found")