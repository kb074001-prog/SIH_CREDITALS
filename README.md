🌲 SafeForest — Multi-Hazard Forest Monitoring & CAP Alert System
📌 Overview
1. Open the project folder
cd C:\Users\<username>\Desktop\SIH
2. Create a virtual environment
py -m venv venv
3. Install dependencies
.\venv\Scripts\python.exe -m pip install -r requirements.txt
▶️ Run the Project

Start the FastAPI server:

.\venv\Scripts\python.exe -m uvicorn main:app --reload

SafeForest is a multi-hazard forest monitoring and early-warning prototype designed to monitor environmental conditions and identify potential hazards such as forest fire, air pollution, and gas leakage.

The system combines ESP32 sensor nodes, NVIDIA Jetson edge computing, AI/ML processing, and a FastAPI backend with a web-based monitoring dashboard.

The overall system architecture is:

ESP32 Sensor Nodes
        ↓
NVIDIA Jetson
        ↓
AI / ML Processing
        ↓
FastAPI Backend
        ↓
SafeForest Web Dashboard
        ↓
CAP 1.2 Alert Generator

The project provides a single platform for monitoring sensor information, device status, hazard conditions, location, and structured alerts.

🎯 Objectives

The main objectives of SafeForest are:

Monitor forest and environmental conditions.
Detect potential wildfire-related conditions.
Monitor air pollution using PM2.5 data.
Monitor possible gas leakage conditions.
Collect environmental data using ESP32 sensor nodes.
Provide an edge-AI processing layer using NVIDIA Jetson.
Display monitoring information through a web dashboard.
Provide API endpoints for ESP32 and Jetson integration.
Generate CAP 1.2-compatible alert information.
Provide a foundation that can later be connected to real sensors and trained AI models.
🚨 Hazards Monitored
🔥 Forest Fire

The system uses environmental parameters such as temperature and smoke information to represent potential fire-related conditions.

The architecture also provides an NVIDIA Jetson AI layer for future integration of AI-based fire detection.

🌫️ Air Pollution

PM2.5 data is monitored and displayed on the dashboard to represent air-quality conditions.

☁️ Gas Leakage

Gas sensor information is used to represent normal or warning conditions.

🤖 AI-Based Analysis

NVIDIA Jetson is included as the edge-computing platform for AI/ML inference.

🏗️ System Architecture
┌──────────────────────┐
│   ESP32 Sensor Nodes │
│                      │
│ Temperature          │
│ Smoke                │
│ PM2.5                │
│ Gas                  │
│ Battery              │
│ Location             │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    NVIDIA Jetson     │
│                      │
│    Edge AI / ML      │
│     Processing       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       FastAPI        │
│       Backend        │
│                      │
│ REST API             │
│ Data Processing      │
│ Alert Interface      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Web Dashboard      │
│                      │
│ Live Sensor Data     │
│ Hazard Status        │
│ Device Status        │
│ Location             │
│ CAP Alerts           │
└──────────────────────┘
🔌 ESP32 Sensor Layer

ESP32 is used as the sensor-node platform.

The sensor layer is designed to provide information such as:

Parameter	Purpose
Temperature	Environmental/fire monitoring
Smoke	Fire-related monitoring
PM2.5	Air-pollution monitoring
Gas	Gas-leakage monitoring
Battery	Sensor-node status
Latitude	Monitoring location
Longitude	Monitoring location

Example sensor data:

{
    "device_id": "SF-001",
    "temperature": 34.5,
    "smoke": 0.32,
    "pm25": 42,
    "gas": 0.15
}

The current software prototype provides an API endpoint for receiving this type of data.

🤖 NVIDIA Jetson Edge AI

NVIDIA Jetson acts as the edge-computing component of SafeForest.

The architecture allows the Jetson to process sensor or other input data locally and return AI/ML inference results to the backend.

Example inference data:

{
    "event": "forest_fire",
    "confidence": 0.94,
    "status": "critical"
}

The current project provides the backend interface for Jetson inference. An actual trained AI model can be integrated into this layer during future development.

⚙️ FastAPI Backend

SafeForest uses FastAPI as its backend framework.

The backend connects the frontend dashboard with the sensor and edge-AI layers.

Backend responsibilities
Serve the SafeForest website.
Provide live monitoring data.
Receive ESP32 sensor data.
Receive NVIDIA Jetson inference results.
Receive alert information.
Provide the API layer for future hardware integration.
🔗 API Endpoints
GET /

Loads the SafeForest web dashboard.

GET /api/health

Checks the backend status.

Example:

{
    "status": "online",
    "system": "SafeForest",
    "architecture": "ESP32 -> NVIDIA Jetson -> FastAPI"
}
GET /api/live

Returns live/demo monitoring information.

The response includes information such as:

Device ID
ESP32 sensor node
NVIDIA Jetson
Temperature
Smoke
PM2.5
Gas
Battery
Latitude
Longitude
AI status
Timestamp

The current prototype generates demo values for live dashboard demonstration.

POST /api/sensor

Receives sensor information from an ESP32 node.

Example:

{
    "device_id": "SF-001",
    "temperature": 34.5,
    "smoke": 0.32,
    "pm25": 42,
    "gas": 0.15
}
POST /api/jetson/inference

Provides an interface for NVIDIA Jetson AI inference results.

Example:

{
    "event": "forest_fire",
    "confidence": 0.94,
    "status": "critical"
}
POST /api/alert

Receives alert information through the backend.

🚨 CAP 1.2 Alert System

SafeForest includes a CAP 1.2-compatible alert prototype.

CAP stands for Common Alerting Protocol.

The alert interface allows the user to provide information such as:

Event
Urgency
Severity
Certainty
Headline
Description
Instructions
Latitude
Longitude
Alert radius

The system can generate a structured CAP XML alert containing this information.

Supported event examples
Wildfire
Air Pollution
Gas Leakage
Multi-Hazard
CAP workflow
Hazard Information
       ↓
CAP Alert Form
       ↓
FastAPI Backend
       ↓
CAP XML Generation
       ↓
Downloadable Alert File

Important: The CAP module is a prototype demonstrating structured CAP-compatible alert generation. It is not an official connection to a government emergency-alert distribution network.

🖥️ Web Dashboard

The SafeForest website provides a centralized interface for the monitoring system.

Dashboard features
🌲 SafeForest system overview
🔥 Fire-risk status
🌫️ Air-quality status
☁️ Gas-detection status
🤖 Jetson AI status
🌡️ Temperature
💨 Smoke
🌫️ PM2.5
🔋 Battery status
📍 Latitude and longitude
📡 ESP32 device information
🚨 CAP 1.2 alert generator

The dashboard automatically requests live data from:

/api/live

and updates the displayed monitoring values.

📁 Project Folder Structure

Use the following structure for the current project:

SIH/
│
├── main.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── cap_alerts/
│   └── generated CAP XML files
│
└── venv/
    └── Python virtual environment
File Description
File/Folder	Description
main.py	FastAPI backend and API endpoints
requirements.txt	Required Python packages
README.md	Project documentation
static/index.html	SafeForest web interface
static/style.css	Website styling
static/app.js	Dashboard and API JavaScript
cap_alerts/	Generated CAP alert files
venv/	Python virtual environment
🛠️ Technologies Used
Hardware
ESP32
Environmental sensors
NVIDIA Jetson
Backend
Python
FastAPI
Uvicorn
Pydantic
Frontend
HTML5
CSS3
JavaScript
AI/Edge Computing
NVIDIA Jetson
AI/ML inference layer
Alerting
CAP 1.2-compatible XML
📦 Requirements

The project dependencies are defined in:

requirements.txt

Current dependencies:

fastapi
uvicorn
pydantic
🚀 Installation
1. Open the project folder
cd C:\Users\<username>\Desktop\SIH
2. Create a virtual environment
py -m venv venv
3. Install dependencies
.\venv\Scripts\python.exe -m pip install -r requirements.txt
▶️ Run the Project

Start the FastAPI server:

.\venv\Scripts\python.exe -m uvicorn main:app --reload

The terminal will display the local server address.

Open that address in a web browser to access the SafeForest dashboard.

🔄 Complete Workflow
1. Environmental sensors collect data
                    ↓
2. ESP32 receives sensor readings
                    ↓
3. Data is sent toward the edge-processing layer
                    ↓
4. NVIDIA Jetson performs/hosts AI processing
                    ↓
5. FastAPI provides the backend API
                    ↓
6. Web dashboard displays monitoring information
                    ↓
7. Hazard information can be represented
   through the CAP alert interface
                    ↓
8. CAP XML can be generated for the prototype
📊 Prototype Data

The current /api/live endpoint uses generated demonstration values.

This allows the website and dashboard to be tested without continuously connected physical sensors.

The prototype therefore demonstrates the complete software workflow, while actual field deployment would require connecting real sensors and deploying the intended AI/ML models.

📍 Monitoring Location

The prototype includes latitude and longitude values in its monitoring data.

These values can be used to represent the geographical location of the sensor node and can also be included in the CAP alert information.

🔮 Future Scope

The SafeForest system can be extended with:

Real ESP32 sensor integration
Physical smoke, temperature, gas and PM2.5 sensors
Actual NVIDIA Jetson deployment
Trained fire-detection AI models
Camera-based fire detection
Thermal-camera integration
Multiple distributed sensor nodes
LoRa/LoRaWAN communication
Wireless sensor networks
Historical sensor-data storage
Real-time graphs and analytics
Map-based monitoring
Automated alert generation
User authentication
Cloud synchronization
Field testing and model validation
⚠️ Current Limitations
The current live dashboard uses demo/simulated sensor values.
Physical ESP32 sensors are not continuously connected to the current software prototype.
The Jetson endpoint is an integration interface; a trained production AI model must be connected for actual AI inference.
The CAP module demonstrates structured alert generation and is not an official emergency-alert distribution service.
Real-world deployment would require hardware testing, communication infrastructure, validation, security, and appropriate operational integration.
🎯 Project Outcome

SafeForest demonstrates an integrated architecture for environmental monitoring in which:

ESP32
  ↓
Sensor Data
  ↓
NVIDIA Jetson
  ↓
Edge AI / ML
  ↓
FastAPI
  ↓
Web Dashboard
  ↓
CAP 1.2 Alert

The prototype provides a foundation for combining multi-hazard sensing, edge computing, AI/ML processing, real-time monitoring, and structured alert generation into a single system.

👨‍💻 Project Status

Current Status: Prototype / Demonstration

The current implementation successfully demonstrates the software-side architecture, web dashboard, API interfaces, live demonstration data, and CAP alert-generation workflow.

Further hardware and AI/ML integration can be added as the project progresses.
