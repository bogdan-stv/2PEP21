import logging
from concurrent import futures
import grpc
import area_pb2
import area_pb2_grpc

class Area(area_pb2_grpc.AreaCalculatorServicer):

    def CalculateArea(self, request, context):
        return area_pb2.AreaResult(result=float(request.length * request.width))

    def CalculateSquare(self, request, context):
        return area_pb2.AreaResult(result=float(request.side * request.side))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    area_pb2_grpc.add_AreaCalculatorServicer_to_server(Area(), server)
    server.add_insecure_port('[::]:30100')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()
