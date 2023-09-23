# Vishwa_GUI
## ➕GROUND CONTROL SYSTEM:

For the ground control system, we have wireless communication between the payload XBEE and the Yagi Antenna (whatever antenna we are using) and the wired communication between the Ground station computer <-> XBEE Breakout Board <-> Ground station XBEE <-> Yagi Antenna (ex)

## GCS Communication Pathway:

### Telemetry Transmission via USB Connectors: 
Telemetry data, which includes information such as sensor readings, mission status, and other relevant data from the CanSat, is communicated to the Ground Control Station via USB connectors. Two USB connectors are used for this purpose. These connectors establish a physical connection between the CanSat's onboard computer and the laptop.

### Ground XBee Module: 
The USB-connected telemetry data is then transmitted from our laptop to a Ground XBee module. XBee modules are a type of wireless communication device commonly used in Internet of Things (IoT) and remote monitoring applications. The Ground XBee module acts as a wireless data transmitter and receiver.

### SMA Male to N Female Connector:
The Ground XBee module is connected to a specialized connector known as SMA Male to N Female connector. SMA (SubMiniature version A) and N connectors are commonly used in RF (Radio Frequency) and antenna applications. This connector ensures a secure and reliable connection between the ground XBee module and the antenna.

## For the simulation mode 👍
● When the SIM_ENABLE and SIM_ACTIVATE commands are sent, information read from CSV file is sent to CanSat 
● CanSat uses given information to run through flight protocol, returning sensor values 


