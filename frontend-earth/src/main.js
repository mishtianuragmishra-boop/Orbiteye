import "./style.css";
import * as Cesium from "cesium";

import "cesium/Build/Cesium/Widgets/widgets.css";

document.body.innerHTML = `
<div id="app">

    <div id="navbar">
        <h1>OrbitEye</h1>

        <div id="menu">
            <button id="homebtn"    >Home</button>
            <button id="searchMenu">Search</button>
            <button id="analyticsbtn">Analytics</button>
            <button id="livetrackerbtn">LiveTracker</button>
            <button>Exit</button>
        </div>

    </div>

<!--lift sidebar-->

    <div id="leftsidebar">
        <h2>Search</h2>
        <input
             type="text"
             id="searchInput"
             placeholder="Search Satellites . . "
        />

        <button id="searchbtn">
            search
        </button>

        <hr>

        <h3>Results</h3>
        <div id="resultlist">
            <p>ISS</p>
            <p>STARLINK</p>
            <p>NOAA-20</p>
        </div>
        <hr>
        <h3>Filters</h3>
        <label><input type="checkbox">Starlink</label>
        <label><input type="checkbox">GPS</label>
        <label><input type="checkbox">Weather</label>
        <label><input type="checkbox">Debris</label>
    </div>
    
<!--EARTH-->
    <div id="cesiumContainer"></div>

<!--Rightsidebar-->

    <div id="rightsidebar">
        <h2>Satellite information</h2>
        <div class="inforow">
            <strong>Name</strong>
            <p>None selected</p>
        </div>

        <div class="inforow">
            <strong>Satellites counted</strong>
            <p id="Satcount">loading.....</p>
        </div>

        <div class="inforow">
            <strong>Norad</strong>
            <p>-------</p>
        </div>

        <div class="inforow">
            <strong>Altitude</strong>
            <p>-------</p>
        </div>

        <div class="inforow">
            <strong>Velocity</strong>
            <p>-------</p>
        </div>

        <div class="inforow">
            <strong>Country</strong>
            <p>-------</p>
        </div>

        <div class="inforow">
            <strong>Launch</strong>
            <p>-------</p>
        </div>

    </div>

    <!--floating buttons-->
    <div id="floatingbuttons">
        <button>+</button>
        <button>-</button>
        <button>home</button>
        <button>galaxyemoji</button>
    </div> 

<!--status bar-->

    <div id="statusbar">
        <span>live</span>
        <span>Satellites loaded</span>
        <span>backend:connected</span>
        <span>UTC--|--</span>
    </div>
</div>

`;

const viewer = new Cesium.Viewer("cesiumContainer", {
    animation: false,
    timeline: false,
    baseLayerPicker:false,
    geocoder:false,
    homeButton:false,
    sceneModePicker:false,
    navigationHelpButton:false,
    fullscreenButton:false, 
    infoBox:false,
    selectionIndicator:false,
});

viewer.scene.globe.enableLighting = true;
viewer.scene.skyAtmosphere.show=true;
viewer.scene.fog.enabled=true;
viewer.camera.flyTo(
    {
        destination:Cesium.Cartesian3.fromDegrees(
            -75,
            20,
            22000000
        ),
        duration:5
    }
);
viewer.cesiumWidget.creditContainer.style.display="none";
fetch("http://127.0.0.1:5000/api/satellitecount")
    .then(response => response.json())
    .then(data => {
        document.getElementById("Satcount").textContent = data.count;
    });
