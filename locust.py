import time
import execution_pb2_grpc
import execution_pb2

class LocustServiceServicer(execution_pb2_grpc.LocustServiceServicer):
    def __init__(self):
        self.task_updates = {}

    def RunTest(self, request_iterator, context):
        entry_info = dict()
        for request in request_iterator:
            print(request)
            time.sleep(2)

            # Print task information
            print(f"Executing test {request.test_id}: {request.name}")

            status = {
                "test_id": request.test_id,
                "status": "Done"
            }
            yield execution_pb2.TestResponse(**status)
