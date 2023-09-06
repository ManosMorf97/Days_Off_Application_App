import paho.mqtt.client as mqtt
import time

client=mqtt.Client("Server")




def process_request(client,userdata,message):
    message_decoded=str(message.payload.decode("utf-8"))
    pub="Publisher: "
    if message_decoded.startswith("Publisher: "):
        print(message_decoded)
        client.publish("Random","Subscriber: You sent me "+message_decoded[len(pub):])
        


client.on_message=process_request
client.connect("mqtt.eclipseprojects.io")

client.subscribe("Random")


client.loop_forever()

client.disconnect()