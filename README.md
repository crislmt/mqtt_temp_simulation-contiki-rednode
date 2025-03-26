# Environmental Monitoring using IoT Devices - Contiki NG/Node-RED

## Introduction
This project utilizes IoT devices to monitor temperature and humidity. Readings are taken every 10 seconds, and a sliding window computes the average of the last six readings. If the average surpasses a specified threshold (K), raw readings are sent instead. The backend maintains logs of temperature and humidity extremes for each month and sends reports via email. Data persistency ensures that a system reboot does not result in data loss.

## Approach and Assumptions
### Contiki NG
- The simulation employs Contiki NG with a network of COOJA Motes using the RPL Tree Protocol.
- An IPv6 border router acts as the gateway for IoT devices to communicate over the internet.
- Temperature and humidity data are transmitted via MQTT with QoS level 0 to minimize overhead.
- The simulation follows the Constant Loss Unit-Disk Graph Model (CL-UDGM) for communication between nodes.

### Node-RED
- The backend uses Node-RED for data processing, email reporting, and persistent storage.
- Data is logged in JSON files (`temp.json` for daily updates and `log.json` for monthly summaries).

## Design
### Contiki NG
#### RPL Border Router Mote
- Acts as the root of the RPL tree and bridges MQTT messages from IoT devices to a Mosquitto broker.
- Messages are forwarded from a local Mosquitto broker to an external broker.

#### MQTT Mote
- Operates as a finite state machine, sending MQTT messages with temperature and humidity readings.
- Stores the last six readings locally to compute averages.
- If the average exceeds a threshold (K), raw readings are sent instead of averages.

### Node-RED
#### Setup Flow
- Initializes the system by creating `temp.json` with default values.
- Only runs once during the first setup.

#### Main Flow
- Processes incoming readings and updates `temp.json` with cumulative daily statistics.
- Maintains daily, monthly, and extreme temperature/humidity records.
- Generates and stores monthly summaries in `log.json`.
- Sends reports via email at the end of each month.

## Installation
### Node-RED
1. Start Node-RED.
2. Run the setup flow to generate the `temp.json` file.
3. Ensure `temp.json` remains intact for system recovery after crashes.

### Contiki NG
1. Open a terminal and navigate to the COOJA simulator directory.
2. Run `ant run` to launch the simulator.
3. Load the `simulation.csc` file from the project directory.
4. Compile and run `MQTT_Mote` and `RPL_Border_Router`.
5. Launch the RPL border router client with:
   ```bash
   make TARGET=cooja connect-router-cooja
   ```
6. Stop any running Mosquitto instance in the VM.
7. Start a new Mosquitto instance with:
   ```bash
   mosquitto -c mosquitto.conf
   ```

## Simulation
The system simulates real-world IoT device behavior by collecting and analyzing temperature and humidity data. The processing workflow ensures efficient data handling, persistent storage, and robust failure recovery mechanisms.

## References
- [Contiki NG Documentation](https://github.com/contiki-ng/contiki-ng/wiki)
- [Node-RED Documentation](https://nodered.org/docs/)

