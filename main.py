from datetime import datetime, timezone
from random import uniform, randint, choice
from pathlib import Path
import uuid
import xml.etree.ElementTree as ET

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
CAP_DIR = BASE_DIR / "cap_alerts"
CAP_DIR.mkdir(exist_ok=True)

app = FastAPI(
    title="SafeForest",
    description="Multi-Hazard Disaster Detection Prototype",
    version="1.1"
)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/health")
def health():
    return {
        "status": "online",
        "system": "SafeForest",
        "architecture": "ESP32 -> NVIDIA Jetson -> FastAPI -> CAP 1.2",
        "cap_version": "CAP 1.2"
    }


@app.get("/api/live")
def live_data():
    # DEMO DATA — replace with actual ESP32/Jetson readings later.
    temperature = round(uniform(28, 38), 2)
    pm25 = round(uniform(20, 90), 2)

    smoke = choice(["Normal", "Normal", "Low", "Elevated"])
    gas = choice(["Normal", "Normal", "Normal", "Warning"])

    fire_detected = temperature >= 36 and smoke == "Elevated"
    air_alert = pm25 >= 75
    gas_alert = gas == "Warning"

    if fire_detected:
        ai_status = "Fire Detected"
    elif gas_alert:
        ai_status = "Gas Alert"
    elif air_alert:
        ai_status = "Air Alert"
    else:
        ai_status = "Active"

    return {
        "device_id": "SF-001",
        "sensor_node": "ESP32-SF-001",
        "edge_device": "NVIDIA Jetson",
        "temperature": temperature,
        "smoke": smoke,
        "pm25": pm25,
        "gas": gas,
        "battery": randint(75, 98),
        "latitude": 29.36,
        "longitude": 79.52,
        "fire_detected": fire_detected,
        "air_alert": air_alert,
        "gas_alert": gas_alert,
        "ai_status": ai_status,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.post("/api/sensor")
def receive_sensor_data(data: dict):
    return {
        "received": True,
        "source": "ESP32",
        "forwarded_to": "NVIDIA Jetson",
        "data": data,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.post("/api/jetson/inference")
def jetson_inference(data: dict):
    return {
        "received": True,
        "source": "NVIDIA Jetson",
        "ai_processed": True,
        "result": data,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.post("/api/alert")
def alert(data: dict):
    return {
        "alert_received": True,
        "alert": data,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


def create_cap_xml(data: dict):
    now = datetime.now(timezone.utc)
    sent = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    identifier = f"safeforest-{now.strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:8]}"

    root = ET.Element("alert")
    ET.SubElement(root, "identifier").text = identifier
    ET.SubElement(root, "sender").text = "SafeForest"
    ET.SubElement(root, "sent").text = sent
    ET.SubElement(root, "status").text = "Test"
    ET.SubElement(root, "msgType").text = "Alert"
    ET.SubElement(root, "scope").text = "Public"

    info = ET.SubElement(root, "info")
    ET.SubElement(info, "language").text = "en-US"
    ET.SubElement(info, "category").text = "Safety"
    ET.SubElement(info, "event").text = data.get("event", "Wildfire")
    ET.SubElement(info, "urgency").text = data.get("urgency", "Immediate")
    ET.SubElement(info, "severity").text = data.get("severity", "Severe")
    ET.SubElement(info, "certainty").text = data.get("certainty", "Likely")
    ET.SubElement(info, "headline").text = data.get("headline", "SafeForest Emergency Alert")
    ET.SubElement(info, "description").text = data.get("description", "Potential hazard detected by SafeForest.")
    ET.SubElement(info, "instruction").text = data.get("instruction", "Follow instructions from authorized emergency authorities.")

    area = ET.SubElement(info, "area")
    ET.SubElement(area, "areaDesc").text = "SafeForest monitored forest area"
    lat = float(data.get("latitude", 29.36))
    lon = float(data.get("longitude", 79.52))
    radius = float(data.get("radius", 1))
    ET.SubElement(area, "circle").text = f"{lat},{lon} {radius}"

    xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    return identifier, xml


@app.post("/api/cap/generate")
def generate_cap(data: dict):
    identifier, xml = create_cap_xml(data)
    filename = f"{identifier}.xml"
    (CAP_DIR / filename).write_bytes(xml)
    return {
        "status": "success",
        "cap_version": "CAP 1.2",
        "identifier": identifier,
        "filename": filename,
        "download": f"/api/cap/download/{filename}"
    }


@app.get("/api/cap/download/{filename}")
def download_cap(filename: str):
    # Only allow files created inside cap_alerts.
    safe_name = Path(filename).name
    filepath = CAP_DIR / safe_name
    if not filepath.exists():
        return {"error": "CAP alert not found"}
    return FileResponse(filepath, media_type="application/xml", filename=safe_name)


@app.get("/api/cap/demo.xml")
def demo_cap():
    _, xml = create_cap_xml({
        "event": "Wildfire",
        "headline": "SafeForest Wildfire Detection Alert",
        "description": "Potential wildfire detected by ESP32 sensors and NVIDIA Jetson edge AI.",
        "instruction": "Avoid the affected monitoring area and follow instructions from authorized emergency authorities.",
        "urgency": "Immediate",
        "severity": "Severe",
        "certainty": "Likely",
        "latitude": 29.36,
        "longitude": 79.52,
        "radius": 1
    })
    return Response(content=xml, media_type="application/xml")
