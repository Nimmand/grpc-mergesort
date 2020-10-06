# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rng_pb2 as rng__pb2


class RngesusStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateNumbers = channel.unary_unary(
                '/rng.Rngesus/GenerateNumbers',
                request_serializer=rng__pb2.RngRequest.SerializeToString,
                response_deserializer=rng__pb2.RngReply.FromString,
                )


class RngesusServicer(object):
    """The greeting service definition.
    """

    def GenerateNumbers(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RngesusServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateNumbers': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateNumbers,
                    request_deserializer=rng__pb2.RngRequest.FromString,
                    response_serializer=rng__pb2.RngReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rng.Rngesus', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Rngesus(object):
    """The greeting service definition.
    """

    @staticmethod
    def GenerateNumbers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rng.Rngesus/GenerateNumbers',
            rng__pb2.RngRequest.SerializeToString,
            rng__pb2.RngReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)