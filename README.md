# OrbitEye 🚀

OrbitEye is a Python-based satellite tracking and analysis application developed as an Electronics and Communication Engineering (ECE) project. It allows users to search for satellites, analyze orbital parameters, and track satellite positions using real-world orbital data from CelesTrak.

---

## Features

### 🔍 Satellite Search

* Search satellites by **Name**
* Search satellites by **NORAD Catalog ID**
* Display complete satellite information including:

  * Object Name
  * Object ID
  * Epoch
  * Mean Motion
  * Eccentricity
  * Inclination
  * Right Ascension of Ascending Node
  * Argument of Pericenter
  * Mean Anomaly
  * Ephemeris Type
  * Classification Type
  * NORAD Catalog ID
  * Element Set Number
  * Revolution at Epoch
  * BSTAR Drag Term
  * Mean Motion Dot
  * Mean Motion DDot

---

## Orbital Analytics

OrbitEye computes the following statistics for the satellite dataset:

* Mean Motion
* Inclination
* Eccentricity
* BSTAR Drag Term
* Epoch

For each parameter, the program calculates:

* Average value
* Maximum value and corresponding satellite
* Minimum value and corresponding satellite

---

## Live Satellite Tracking

Using the Skyfield library and TLE (Two-Line Element) data, OrbitEye provides the current:

* Latitude
* Longitude
* Altitude

of a selected satellite.

---

## Technologies Used

* Python 3
* CSV
* Skyfield
* Datetime

---

## Dataset

Satellite data is obtained from **CelesTrak** in the following formats:

* CSV
* TLE (Two-Line Element)

---

## Project Structure

```
OrbitEye/
│
├── backend/
│   ├── main.py
│   ├── analytics.py
│   ├── tsearch.py
│   ├── tracker.py
│   └── data/
│       ├── starlink.csv
│       └── starlink.tle
│
├── README.md
└── requirements.txt
```

---

## Installation

Install the required library:

```
pip install skyfield
```

---

## Running the Project

Run the main program:

```
python main.py
```

---

## Menu

```
========== ORBIT EYE ==========
1. Search
2. Analytics
3. Tracker
4. Exit
```

---

## Future Enhancements

* Graphical User Interface (GUI)
* MATLAB-based orbital visualization
* Interactive ground-track maps
* Data visualization and statistical plots
* API integration
* Database support

---

## Author
MISHTI ANURAG MISHRA
Developed as an Electronics and Communication Engineering (ECE) academic project using real satellite orbital data.
