from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                    value_serializer=lambda v: json.dumps(v).encode('ascii'),
                    key_serializer=lambda v: json.dumps(v).encode('ascii')
                    )
topic_name='pizza_partition'
print("producing to partitions....")
#send an event(message)
producer.send(topic_name,
              key={"id":0},
              value={"name":"Frank", "pizza":"Margherita "},
              partition=0
             )
producer.send(topic_name,
              key={"id":1},
              value={"name":"Adele", "pizza":"Hawaii "},
              partition=1
             )
producer.flush()

# sending more messages
producer.send(topic_name,
              key={"id":0},
              value={"name":"Mark", "pizza":"Chicken"},
              #partition=0
             )
producer.send(topic_name,
              key={"id":1},
              value={"name":"Jan", "pizza":"Mushrooms"},
              #partition=1
             )
producer.flush()