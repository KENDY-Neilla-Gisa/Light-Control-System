import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()

BROKER = os.getenv("BROKER_URL")
PORT = int(os.getenv("PORT"))
TOPIC = "/student_group/light_control"
USERNAME = os.getenv("HIVEMQ_USERNAME")
PASSWORD = os.getenv("PASSWORD")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker with result code " + str(rc))
        client.subscribe(TOPIC)
        print(f"Subscribed to topic {TOPIC}")
    else:
        print("Failed to connect, return code " + str(rc))

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    if message == "ON":
        print("💡 Light is TURNED ON")
    elif message == "OFF":
        print("💡 Light is TURNED OFF")
    else:
        print("⚠️ Unknown command received")

client = mqtt.Client()
client.tls_set()  # Securing connection with TLS
client.username_pw_set(USERNAME, PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

print(f"Connecting to broker {BROKER} on port {PORT} ...")
client.connect(BROKER, PORT, 60)
client.loop_forever()
