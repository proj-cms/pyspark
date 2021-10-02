export KAFKA_HOME=/Users/makaranddeshpande/kafka212/kafka_2.12-3.0.0
export PATH=${PATH}:${KAFKA_HOME}/bin
kafka-server-start.sh $KAFKA_HOME/config/server.properties
