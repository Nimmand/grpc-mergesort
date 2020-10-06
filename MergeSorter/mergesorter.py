import grpc
import merge_pb2
import merge_pb2_grpc

from concurrent import futures

def merge_sort(x):
        if len(x) < 2:return x

        result,mid = [],int(len(x)/2)

        y = merge_sort(x[:mid])
        z = merge_sort(x[mid:])

        while (len(y) > 0) and (len(z) > 0):
                if y[0] > z[0]:result.append(z.pop(0))   
                else:result.append(y.pop(0))

        result.extend(y+z)
        return result

class MergeSorter(merge_pb2_grpc.MergesorterServicer):
    def Merge(self, request, context):
        return merge_pb2.MergeReply(numbers = merge_sort(request.numbers))



server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
merge_pb2_grpc.add_MergesorterServicer_to_server(MergeSorter(), server)
server.add_insecure_port('[::]:5002')
server.start()
print("Started Server")
server.wait_for_termination()