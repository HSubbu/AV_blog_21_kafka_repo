from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                    value_serializer=lambda v: json.dumps(v).encode('ascii'),
                    key_serializer=lambda v: json.dumps(v).encode('ascii')
                    )
topic_name='pizza-demo'
#send an event(message)
print(f"Sending event to {topic_name}")
producer.send(
 topic_name,
 key={"id":1},
 value={"name":"John", "pizza":"Margherita"}
)
producer.flush()
#next messages
producer.send(
 topic_name,
 key={"id":2},
 value={"name":"Adele", "pizza":"Hawaii"}
)

producer.send(
 topic_name,
 key={"id":3},
 value={"name":"Mark", "pizza":"Chicken"}
)
producer.flush()
#produce another event <-- New Consumer Group
producer.send(
 topic_name,
 key={"id":4},
 value={"name":"Dan", "pizza":"Fries"}
)
producer.flush()