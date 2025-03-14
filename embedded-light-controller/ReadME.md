# MQTT Light Toggler

This project demonstrates how to control a light using MQTT protocol. It includes a Python script to listen for MQTT messages and a web interface to send MQTT messages to control the light.

## Project Structure

- `light_simulation.py`: Python script to connect to the MQTT broker and listen for messages.
- `index.html`: Web interface to send MQTT messages to control the light.
- `.env`: Environment file to store sensitive data like broker URL, username, and password.

## Prerequisites

- Python 3.x
- `paho-mqtt` library
- `python-dotenv` library
- A web browser

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/MugishaProper/mqtt-light-toggler.git
   cd mqtt-light-toggler
   ```

2. Setting up environment:

   1. Set up an account on HiveMQ:
      - Go to [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud-broker/) and sign up for a free account.
      - Create a new cluster and note down the cluster URL, username, and password.

   2. Create a `.env` file in the project directory and add your MQTT broker details:

      ```properties
      BROKER_URL=your-cluster-url
      PORT=8883
      HIVEMQ_USERNAME=your-username
      PASSWORD=your-password
      ```

## Usage

### Running the Python Script

1. Open a terminal and navigate to the project directory.
2. Run the Python script:

   ```sh
   python light_simulation.py
   ```

   The script will connect to the MQTT broker and listen for messages on the specified topic.

### Using the Web Interface

1. Open `index.html` in a web browser.
2. Use the buttons to send "ON" and "OFF" messages to the MQTT broker.
3. The Python script will receive these messages and print the corresponding actions to the console.

## Environment Variables

The `.env` file is used to store sensitive data. The following variables are required:

- `BROKER_URL`: The URL of the MQTT broker.
- `PORT`: The port to connect to the MQTT broker.
- `HIVEMQ_USERNAME`: The username for the MQTT broker.
- `PASSWORD`: The password for the MQTT broker.