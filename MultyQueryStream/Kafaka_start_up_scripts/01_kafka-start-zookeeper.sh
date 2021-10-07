export KAFKA_HOME=/Users/makaranddeshpande/kafka212/kafka_2.12-3.0.A
export KAFKA_HOME=/home/forgcpmak/kafka/kafka_2.12-3.0.0
export PATH=${PATH}:${KAFKA_HOME}/bin
zookeeper-server-start.sh ${KAFKA_HOME}/config/zookeeper.properties
