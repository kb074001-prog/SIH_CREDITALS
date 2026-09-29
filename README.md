# SafeForest - Final Landing Page + CAP 1.2

This version keeps the content and API architecture of the original SafeForest project while changing the webpage presentation to match the supplied landing-page reference:

ESP32 -> NVIDIA Jetson -> FastAPI -> CAP 1.2

Included:
- Home hero section
- Features / multi-hazard detection
- How It Works architecture
- Live dashboard
- ESP32 sensor data
- Monitoring location
- CAP 1.2 alert generator
- CAP XML download
- Existing ESP32 and Jetson POST endpoints

Run in PowerShell from this folder:

.\\venv\\Scripts\\python.exe -m pip install -r requirements.txt
.\\venv\\Scripts\\python.exe -m uvicorn main:app --reload

Open http://127.0.0.1:8000
