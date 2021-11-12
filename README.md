# PART 1

In this program the application is sending the integer data from the input topic called "topic-input" with 10 partitions to output topic called "topic-output" with a single partition. The data is accumulated from multiple partitions and is sorted before producing in the output topic.

## How to run and test locally?

* Create a python venv
* Install dependencies

```sh
# py3:
python -m venv test_venv
source test_venv/bin/activate
pip install -r requirements.txt

```
* Install Zookeeper. Run the below command to start Zookeeper

```sh
bin/zookeeper-server-start.sh config/zookeeper.properties

```

* Install Kafka. Run the below command to start Kafka server.

```sh
bin/kafka-server-start.sh config/server.properties

```

* Create an input topic called "topic-input" with partition = 10

```sh
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 10 --topic topic-input

```

* Create an output topic called "topic-output" with partition = 1

```sh
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic topic-output

```

* Run the Faust app inside the python venv using the below command, where myApp is the name of the application

```sh
faust -A myApp worker -l info

```

* Run the Kafka Producer using the below command to produce the integer data to topic "topic-input"

```sh
python src/kafkaProducer.py

```

* Run the Kafka Consumer to see the data in the topic "topic-output"

```sh
python src/kafkaConsumer2.py

```

* Check the data in the topics using below commands

```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic-input --from-beginning

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic-output --from-beginning

```

* Also run the python tests locally to check the faust application

```sh
pytest src/test.py 

```
