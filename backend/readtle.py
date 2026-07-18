def satellitecount():
    with open("data/starlink.tle","r") as f:
        lines=f.readlines()
    return len(lines)//3
