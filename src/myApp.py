import faust
import logging
from asyncio import sleep
from kafka import KafkaConsumer
from kafka import KafkaProducer


log = logging.getLogger(__name__)

data = []


app = faust.App('myApp', broker='kafka://localhost:9092')

source_topic = app.topic('topic-input', value_type=bytes)
destination_topic = app.topic('topic-output', value_type=bytes)


@app.agent(source_topic, sink=[destination_topic])
async def collect_msg(messages):
	# Create a batch of streams of 150 events until 10 seconds
    async for message in messages.take(150, within=10):
        for d in sorted(message):
        	yield(d)


if __name__ == '__main__':
    app.main()
