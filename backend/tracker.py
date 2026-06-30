from skyfield.api import EarthSatellite, load
def livetracker():
    with open("data/iss.tle") as f:
        name=f.readline().strip()
        line1=f.readline().strip()
        line2=f.readline().strip()
        satellite = EarthSatellite(line1,line2,name)
        ts=load.timescale()
        t=ts.now()
        geocentric=satellite.at(t)
        subpoint=geocentric.subpoint()
        print("Satellite", satellite.name)
        print("Latitude", subpoint.latitude.degrees)
        print("Longitude", subpoint.longitude.degrees)
        print("Altitude", subpoint.elevation.km)