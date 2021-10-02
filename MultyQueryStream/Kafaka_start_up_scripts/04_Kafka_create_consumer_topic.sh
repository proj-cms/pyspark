export KAFKA_HOME=/Users/makaranddeshpande/kafka212/kafka_2.12-3.0.0
export PATH=${PATH}:${KAFKA_HOME}/bin

kafka-topics.sh \
--create \
--topic notifications \
--bootstrap-server localhost:9092 \
--partitions 2 \
--replication-factor 1