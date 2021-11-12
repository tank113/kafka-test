from kafka import KafkaConsumer

topic_name_input  = "topic-input"
topic_name_output = "topic-output"


# consumer to consume the data from the topic topic-output
consumer2 = KafkaConsumer(
     topic_name_output,
     bootstrap_servers=['localhost:9092'],
     group_id='my-group_new',
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: int(x.decode("utf-8"))
    )

def read_topic_data():
	print("received")
	for message in consumer2:
		print(message)
		

if __name__ == "__main__":
	read_topic_data()
