#from __future__ import print_function

import logging
import sys

import grpc
import crypto
import iot_service_pb2
import iot_service_pb2_grpc

from const import *


def run():
    with grpc.insecure_channel(GRPC_SERVER+':'+GRPC_PORT) as channel:
        
        state = crypto.encrypt(str(sys.argv[1]).encode())
        ledname = crypto.encrypt(str(sys.argv[2]).encode())
        login = crypto.encrypt(str(sys.argv[3]).encode())
        password = crypto.encrypt(str(sys.argv[4]).encode())

        stub = iot_service_pb2_grpc.IoTServiceStub (channel)
        response = stub.BlinkLed(iot_service_pb2.LedRequest(state=state,ledname=ledname, login=login, password=password))

    if response.ledstate[ledname] == 1:
        print("Led state is on")
    elif response.ledstate[ledname] == 0:
        print("Led state is off")
    elif response.ledstate[ledname] == 2:
        print("Wrong password")

if __name__ == '__main__':
    logging.basicConfig()
    run()
