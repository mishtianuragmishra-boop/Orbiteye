#  OrbitEye

OrbitEye is an interactive web-based satellite tracking platform built using **Python, Flask, JavaScript, and CesiumJS**.

The goal of OrbitEye is to visualize Earth-orbiting satellites in real time while providing satellite search, orbital analytics, and detailed satellite information through an intuitive interface.

---

#  Features

##  Interactive 3D Earth

- Powered by CesiumJS
- Realistic globe rendering
- Atmospheric effects
- Dynamic lighting
- Smooth camera navigation

---

##  Satellite Search

- Search satellites by name
- Display matching results
- Select satellites for detailed information

*(Currently under development)*

---

##  Analytics

OrbitEye includes analytics tools for exploring satellite datasets.

Current analytics include:

- BSTAR distribution
- Mean Motion analysis
- Inclination distribution
- Epoch analysis
- Eccentricity analysis

---

##  Backend API

Built using Flask.

Current API:

```
GET /api/satellitecount
```

Returns the total number of satellites currently loaded.

Example response:

```json
{
    "count": 10631
}
```

---

#  Data Source

Satellite data is obtained from **CelesTrak**.

Current datasets include:

- TLE data
- Orbital parameters
- Satellite statistics

---

#  Tech Stack

### Frontend

- JavaScript
- HTML
- CSS
- Vite
- CesiumJS

### Backend

- Python
- Flask
- Flask-CORS

### Data Processing

- Python
- CSV
- Matplotlib

---

#  Project Structure

```
Orbiteye/
│
├── backend/
│   ├── api.py
│   ├── readtle.py
│   ├── bstargraph.py
│   ├── meanmotiongraph.py
│   ├── eccgraph.py
│   ├── epochgraph.py
│   └── incgraph.py
│
├── frontend-earth/
│   ├── src/
│   ├── public/
│   └── vite.config.js
│
└── data/
```

---

#  Current Progress

##  Completed

- CesiumJS integration
- OrbitEye interface
- Responsive UI layout
- Flask backend
- Frontend ↔ Backend connection
- Live satellite count API
- Analytics modules

##  In Progress

- Satellite search
- Dynamic search results
- Satellite information panel
- Orbit visualization
- Live tracking

##  Planned

- Analytics dashboard
- Satellite filters
- Orbit prediction
- Saved satellites
- Deployment

---

#  Running OrbitEye

### Backend

```bash
cd backend
python api.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

---

### Frontend

```bash
cd frontend-earth
npm install
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# Project Goal

OrbitEye is designed as a portfolio project demonstrating:

- Interactive geospatial visualization
- Backend API development
- Frontend development
- Data visualization
- Satellite tracking
- Modern web application architecture

---

# Development Status

Current Version:

**v0.3 — Website Foundation Complete**

Next milestone:

- Live satellite search
- Satellite selection
- Orbit rendering
- Analytics dashboard

---

Made with ❤️ using Python, Flask and CesiumJS.
