#! /bin/bash
#
# Usage:  ./start.sh [port]
#  
# Start the service as a background process
#
# Used and edited: Project 4 start.sh

PORTNUM=$1
if [[ "${PORTNUM}" == "" ]]; then
    PORTNUM="5000"
fi;

echo "***Will listen on port ${PORTNUM}***"

this=${BASH_SOURCE[0]}
here=`dirname ${this}`
activate="${here}/env/bin/activate"
echo "Activating ${activate}"
source ${activate}
echo "Activated"

pushd mapping
python3 map_server.py -P ${PORTNUM} &
pid=$! 
popd
echo "***"
echo "Flask server started"
echo "PID ${pid} listening on port ${PORTNUM}"
echo "***"
