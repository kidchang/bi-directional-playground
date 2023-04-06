import time
import grpc
import execution_pb2
import execution_pb2_grpc

def get_tests():
    test_cases = [{"test_id": x, "name": "Test {}".format(x)} for x in range(1, 6)];
    return test_cases

# initialize channel to gRPC server
channel = grpc.insecure_channel(target="localhost:50051")

# create service stub
stub = execution_pb2_grpc.LocustServiceStub(channel=channel)

def test_request_iterator():
    test_cases = [{"test_id": x, "name": "Test {}".format(x)} for x in range(1, 6)];
    for test in test_cases:
        test_request = execution_pb2.TestRequest(test_id=test['test_id'], name=test['name'])
        yield test_request

# iterate through response stream and print to console
for test_response in stub.RunTest(test_request_iterator()):
    print(test_response)
