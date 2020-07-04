import random
import time


from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=IoTBootCamp2.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=YCsbkLxra/WHyK3YL0/b9Zkvx4WgXdRyckbKa+x5Q/s="


MSG_TXT = '{{"dice1": {dice1},"dice2": {dice2}}}'


def iothub_client_init():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client


def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print("IoT Hub device sending periodic messages, press Ctrl-C to exit")

        while True:

            dice1 = (random.randint(1,6))
            dice2 = (random.randint(1,6))
            msg_txt_formatted = MSG_TXT.format(dice1=dice1, dice2=dice2)
            message = Message(msg_txt_formatted)

            if dice1 == dice2 == 6:
                message.custom_properties["doublingAlert"] = "the player has four sixes to use"
            else:
                message.custom_properties["doublingAlert"] = "the player sticks into normal rules"

            # Send the message.
            print("Sending message: {}".format(message))
            client.send_message(message)
            client.send_message(message.custom_properties["doublingAlert"])
            print("Message successfully sent")
            time.sleep(random.randint(20, 60))

    except KeyboardInterrupt:
        print("IoTHubClient sample stopped")


if __name__ == '__main__':
    print("IoT Hub Quickstart #1 - Simulated device")
    print("Press Ctrl-C to exit")
    iothub_client_telemetry_sample_run()
