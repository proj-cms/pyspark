export KAFKA_HOME=/Users/makaranddeshpande/kafka212/kafka_2.12-3.0.0
export KAFKA_HOME=/home/forgcpmak/kafka/kafka_2.12-3.0.0
export PATH=${PATH}:${KAFKA_HOME}/bin
kafka-console-consumer.sh --topic invoices --from-beginning --bootstrap-server localhost:9092
