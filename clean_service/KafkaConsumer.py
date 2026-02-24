import json
from confluent_kafka import Consumer
from CleanConfig import CleanConfig






class KafkaConsumer:
    def __init__(self,bootstrap_servers,topic_name, group_id, logger):
        self.bootstrap_servers = bootstrap_servers
        self.topic_name =  topic_name
        self.group_id = group_id
        self.logger = logger

    def start(self):
        consumer_config = {
            "bootstrap.servers": self.bootstrap_servers,
            "group.id": self.group_id,
            "auto.offset.reset": "earliest"
        }
        consumer = Consumer(consumer_config)
        consumer.subscribe([self.topic_name])

        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print("❌ Error:", msg.error())
                    continue

                value = msg.value().decode('utf-8')
                order = json.loads(value)
                print(order)
        except KeyboardInterrupt:
            print("\n🔴 Stopping consumer")

        finally:
            consumer.close()




c = CleanConfig().get_bootstrap_servers()
k = KafkaConsumer(c,'RAW','abc','abc')
k.start()