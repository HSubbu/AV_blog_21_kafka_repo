Case 1:
pizza_producer.py  
pizza_consumer.py 
Try auto_offset_reset parameter "earliest" and "latest".
run pizza_producer.py and watch pizza_consumer.py output and see number of messages displayed.

Case 2 : 
after $ docker-compose up -d 
$docker exec -it kafka /bin/sh
#cd opt/kafka/bin
To get list of topics present 
#kafka-topics.sh --list --zookeeper zookeeper:2181
Create a topic with two partitions
#kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 2 --topic pizza_partition
Check the list of partitions again and see if our topic is created
#kafka-topics.sh --list --zookeeper zookeeper:2181
# create two .py consumers called pizza_consumer_part_1.py and pizza_consumer_part_2.py
In pizza_producer_part.py we send two messages initally spcifying producer.send() with parameter 
partitions=0 and partitions=1.
Now when we run producer and two consumers , we see each consumer.py reading individually the messges in the partition 0 and 1
Now send two more messages with same key as above and without mentioning the partitions
in producer . We see that consumers read the messages in the same fashion
