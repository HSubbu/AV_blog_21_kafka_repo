from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], 
                         auto_offset_reset='earliest')
topic_name='kafka-demo'
print(consumer.topics())
consumer.subscribe(topics=[topic_name])
consumer.subscription()                         
for message in consumer:    
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))