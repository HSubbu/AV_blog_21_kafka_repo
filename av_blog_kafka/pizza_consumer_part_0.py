from kafka import KafkaConsumer
from kafka import TopicPartition

topic_name='pizza_partition'
group_id = "my_pizza_group"


consumer_partition_0 = KafkaConsumer(bootstrap_servers=['localhost:9092'], 
                         auto_offset_reset='earliest',
                         max_poll_records = 10)

print("Available Kafka topcs are ..",consumer_partition_0.topics())

consumer_partition_0.assign([TopicPartition(topic_name, 0)])
consumer_partition_0.subscription()                           
for message in consumer_partition_0:    
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))