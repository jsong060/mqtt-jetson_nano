import paho.mqtt.client as mqtt

#Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    # client.subscribe('testtopic/#')

# Message receiving callback
def on_message(client, userdata, msg):
    print("Received on topic \"",msg.topic+"\" "+str(msg.payload.decode('utf-8')))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected disconnection.')

broker = 'broker.emqx.io'
port = 1883

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "test_client01")

# Specify callback function
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Establish a connection
client.connect(broker, port)
# Publish a message
client.publish('test_t01',payload='Hello World 1234',qos=0)

client.loop_forever()