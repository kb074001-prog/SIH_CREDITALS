async function updateDashboard() {
    try {
        const response = await fetch('/api/live');
        const data = await response.json();

        document.getElementById('temperature').textContent = `${Number(data.temperature).toFixed(2)} °C`;
        document.getElementById('smoke').textContent = data.smoke;
        document.getElementById('pm25').textContent = `${Number(data.pm25).toFixed(2)} µg/m³`;
        document.getElementById('gas').textContent = data.gas;
        document.getElementById('battery').textContent = `${data.battery} %`;
        document.getElementById('deviceValue').textContent = data.sensor_node;
        document.getElementById('deviceChip').textContent = data.sensor_node;
        document.getElementById('latitude').textContent = data.latitude;
        document.getElementById('longitude').textContent = data.longitude;

        setStatus('fireStatus', data.fire_detected, '🔥 FIRE ALERT', 'NORMAL');
        setStatus('airStatus', data.air_alert, '⚠ AIR ALERT', 'NORMAL');
        setStatus('gasStatus', data.gas_alert, '⚠ GAS ALERT', 'NORMAL');

        const ai = document.getElementById('aiStatus');
        ai.textContent = data.ai_status;
        ai.className = 'status ' + (data.ai_status === 'Active' ? 'active' : 'danger');
    } catch (error) {
        console.error('Dashboard error:', error);
    }
}

function setStatus(id, alert, alertText, normalText) {
    const element = document.getElementById(id);
    element.textContent = alert ? alertText : normalText;
    element.className = 'status ' + (alert ? 'danger' : 'normal');
}

async function generateCAP() {
    const payload = {
        event: document.getElementById('event').value,
        headline: document.getElementById('headline').value,
        description: document.getElementById('description').value.trim(),
        instruction: document.getElementById('instruction').value.trim(),
        urgency: document.getElementById('urgency').value,
        severity: document.getElementById('severity').value,
        certainty: document.getElementById('certainty').value,
        latitude: parseFloat(document.getElementById('capLatitude').value),
        longitude: parseFloat(document.getElementById('capLongitude').value),
        radius: parseFloat(document.getElementById('radius').value)
    };

    const box = document.getElementById('capResult');
    box.textContent = 'Generating CAP 1.2 alert...';

    try {
        const response = await fetch('/api/cap/generate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
        const result = await response.json();

        if (result.status === 'success') {
            box.innerHTML = `<strong>✓ CAP 1.2 Alert Generated</strong><br><br>Identifier: <code>${result.identifier}</code><br><br><a href="${result.download}" target="_blank">📄 Download CAP XML</a>`;
        } else {
            box.textContent = 'CAP generation failed.';
        }
    } catch (error) {
        console.error(error);
        box.textContent = 'Unable to generate CAP alert.';
    }
}

updateDashboard();
setInterval(updateDashboard, 5000);
