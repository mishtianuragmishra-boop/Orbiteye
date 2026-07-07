from skyfield.api import EarthSatellite, load
def livetracker(query):
    query=query.strip().upper()

    with open("data/starlink.tle.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
    for i in range(0,len(lines)-2):
        name=lines[i].strip()
        line1=lines[i+1].strip()
        line2=lines[i+2].strip()
        parts=line1.split()
        if len(parts)<2:
            continue
        norad=parts[1][:-1]
        if name.upper()==query or norad==query:
            satellite = EarthSatellite(line1,line2,name)
            ts=load.timescale()
            t=ts.now()
            geocentric=satellite.at(t)
            subpoint=geocentric.subpoint()
            velocity=geocentric.velocity.km_per_s
            speed=(velocity[0]**2+velocity[1]**2+velocity[2]**2)**0.5
            return {
                "Name": satellite.name,
                "Latitude" : round(subpoint.latitude.degrees,4),
                "Longitude" : round(subpoint.longitude.degrees,4),
                "Altitude" : round(subpoint.elevation.km,2),
                "Velocity" : round(speed,2)
            }
    