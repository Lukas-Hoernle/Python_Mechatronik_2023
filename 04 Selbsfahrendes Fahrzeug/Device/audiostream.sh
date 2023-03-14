#! /bin/sh

REMOTE_IP="$1"

if [ "$REMOTE_IP" == "" ]; then
    # Default: IPv4 Multicast
    REMOTE_IP="239.0.0.1"
    MULTICAST="(multicast)"
fi

echo "==============================================================="
echo "Starte Audiostream von und zu IP-Adresse $REMOTE_IP $MULTICAST"
echo ""
echo "IP-Adressen des Raspberry Pi:"
echo ""
ip -brief addr show
echo ""
echo "Auf dem Zielcomputer bitte folgende Befehle ausführen, um sich"
echo "mit den Audiostreams zu verbinden:"
echo ""
echo "Senden: trx-tx -h <rasbperrypi_ip>"
if [ "$MULTICAST" == "" ]; then
    echo "Empfang: trx-rx"
else
    echo "Empfang: trx-rx -h 239.0.0.1"
fi
echo "==============================================================="

trx-tx -h "$REMOTE_IP" -d plughw:1 &
PID_TX=$!

trx-rx -m 100 &
PID_RC=$!

echo "ENTER drücken zum Beenden"
read

kill -9 $PID_TX
kill -9 $PID_RX
