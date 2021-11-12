from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

topic_name = "topic-input"

num_partitions = 10

num_list = random.sample(range(0, 10), 10)
num_list_sorted = sorted(num_list)


def send_data_to_topics():
	print("sending...")
	for i in range(num_partitions):
		for j in range(len(num_list_sorted)):
			print(num_list_sorted[j])
			producer.send(topic_name, value=str(num_list_sorted[j]).encode("utf-8"), partition=i)
	producer.flush()
    

if __name__ == "__main__":
	send_data_to_topics()