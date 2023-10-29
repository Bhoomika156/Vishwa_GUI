import serial

# Replace 'COMx' with the appropriate COM port where your XBee module is connected
serial_port = serial.Serial('COM8', 9600)

try:
    while True:
        # Send data to the XBee module
        message = "Hello, XBee!\n"
        print(message)
        serial_port.write(message.encode())  # Send the message as bytes
        print(message)

        # Read data from the XBee module
        while serial_port.in_waiting >0 :
            received_data = serial_port.readline()  # Read 10 bytes
            if received_data:
                print("Received: " + received_data.decode())
            else:
                print("No data")

        print("Hii\n")

except KeyboardInterrupt:
    # Close the serial port when the script is terminated
    serial_port.close()