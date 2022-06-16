from kafka import KafkaProducer
from datetime import datetime
import time
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
for i in range(1000):
    msg = 'Sending Message ' + str(i) +' '+ str(datetime.now().time())
    topic_name = 'kafka-demo'
    producer.send(topic_name, key=b'Message', value=msg.encode())
    print(f"Producing to {topic_name}")
    producer.flush()
    time.sleep(2)