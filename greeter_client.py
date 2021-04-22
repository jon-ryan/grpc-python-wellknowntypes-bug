from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc
from google.protobuf import empty_pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(empty_pb2)
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
