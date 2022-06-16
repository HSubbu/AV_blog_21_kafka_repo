from kafka import KafkaConsumer
from kafka import TopicPartition

topic_name='pizza_partition'
group_id = "my_pizza_group"


consumer_partition_1 = KafkaConsumer(bootstrap_servers=['localhost:9092'], 
                        group_id=group_id,
                         auto_offset_reset='earliest',
                         max_poll_records = 10)

print("Available Kafka topcs are ..",consumer_partition_1.topics())

consumer_partition_1.assign([TopicPartition(topic_name, 1)])
consumer_partition_1.subscription()                     
for message in consumer_partition_1:    
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))