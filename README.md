MQTT Light Control Simulation
A simple IoT light control system using the MQTT protocol.
Author
KENDY Neilla Gisa – Developer and Creator
Components
index.html: Web interface with ON/OFF buttons and status display.
light_simulation.py: Python script simulating an ESP8266 IoT device.
Setup Instructions
Prerequisites:
Python 3.x
paho-mqtt library (Install with: pip install paho-mqtt)
A modern web browser
Access to the MQTT broker at 157.173.101.159
Running the Simulation:
Start the Python script:python light_simulation.py
Open index.html in a web browser.
Click the "Turn ON" or "Turn OFF" buttons to control the simulated light.
How It Works
The web interface connects via WebSocket (ws://157.173.101.159:9001).
The Python client connects via TCP (157.173.101.159:1883).
The buttons on the web page publish "ON" or "OFF" messages to the light_control topic.
The Python script topic and prints the light status.
Testing
Requires a connection to the specified MQTT broker (157.173.101.159).
The web client communicates via WebSocket (port 9001).
The Python client communicates via standard MQTT over TCP (port 1883).
Ensure the firewall allows connections to these ports.
Notes
Assumes the MQTT broker is running at 157.173.101.159.
The web client uses the WebSocket protocol on port 9001.
The Python client uses standard MQTT over TCP on port 1883.
No authentication is implemented in this example.
Full Python Script (light_simulation.py)
import paho.mqtt.client as mqtt

# Define the MQTT settings
broker = "157.173.101.159"
port = 1883
topic = ""

# Callback when the message is received
def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    if payload == "ON":
        print("💡 Light is TURNED ON")
    elif payload == "OFF":
        print("💡 Light is TURNED OFF")

# Initialize MQTT client
client = mqtt.Client()

# Set up callback for message reception
client.on_message = on_message

# Connect to the broker
client.connect(broker, port)

# Subscribe to the topic
client.subscribe(topic)

# Loop to keep the client connected and receiving messages
client.loop_start()

# Wait for messages (press Ctrl+C to stop)
print("Listening for messages on topic:", topic)
