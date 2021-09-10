from __future__ import print_function
import grpc
import area_pb2_grpc
import area_pb2
import logging

def run(length, width):
    with grpc.insecure_channel("localhost:30100") as channel:
        stub = area_pb2_grpc.AreaCalculatorStub(channel)
        response = stub.CalculateArea(area_pb2.AreaParams(length=length,width=width))
        print('Server responded with ', response.result)
        response = stub.CalculateSquare(area_pb2.SquareParams(side=length))
        print('Server responded with', response.result)

if __name__ == "__main__":
    logging.basicConfig()
    run(2, 4)
