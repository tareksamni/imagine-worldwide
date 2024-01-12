# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hitchhiker_pb2 as hitchhiker__pb2


class HitchhikerSourceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSourceId = channel.unary_unary(
                '/hitchhiker.HitchhikerSource/GetSourceId',
                request_serializer=hitchhiker__pb2.GetSourceIdRequest.SerializeToString,
                response_deserializer=hitchhiker__pb2.GetSourceIdResponse.FromString,
                )
        self.GetDownloads = channel.unary_unary(
                '/hitchhiker.HitchhikerSource/GetDownloads',
                request_serializer=hitchhiker__pb2.GetDownloadsRequest.SerializeToString,
                response_deserializer=hitchhiker__pb2.GetDownloadsResponse.FromString,
                )
        self.DownloadFile = channel.unary_unary(
                '/hitchhiker.HitchhikerSource/DownloadFile',
                request_serializer=hitchhiker__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=hitchhiker__pb2.DownloadFileResponse.FromString,
                )
        self.MarkDelivered = channel.unary_unary(
                '/hitchhiker.HitchhikerSource/MarkDelivered',
                request_serializer=hitchhiker__pb2.MarkDeliveredRequest.SerializeToString,
                response_deserializer=hitchhiker__pb2.MarkDeliveredResponse.FromString,
                )


class HitchhikerSourceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSourceId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDownloads(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarkDelivered(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HitchhikerSourceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSourceId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSourceId,
                    request_deserializer=hitchhiker__pb2.GetSourceIdRequest.FromString,
                    response_serializer=hitchhiker__pb2.GetSourceIdResponse.SerializeToString,
            ),
            'GetDownloads': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDownloads,
                    request_deserializer=hitchhiker__pb2.GetDownloadsRequest.FromString,
                    response_serializer=hitchhiker__pb2.GetDownloadsResponse.SerializeToString,
            ),
            'DownloadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=hitchhiker__pb2.DownloadFileRequest.FromString,
                    response_serializer=hitchhiker__pb2.DownloadFileResponse.SerializeToString,
            ),
            'MarkDelivered': grpc.unary_unary_rpc_method_handler(
                    servicer.MarkDelivered,
                    request_deserializer=hitchhiker__pb2.MarkDeliveredRequest.FromString,
                    response_serializer=hitchhiker__pb2.MarkDeliveredResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hitchhiker.HitchhikerSource', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HitchhikerSource(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSourceId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hitchhiker.HitchhikerSource/GetSourceId',
            hitchhiker__pb2.GetSourceIdRequest.SerializeToString,
            hitchhiker__pb2.GetSourceIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDownloads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hitchhiker.HitchhikerSource/GetDownloads',
            hitchhiker__pb2.GetDownloadsRequest.SerializeToString,
            hitchhiker__pb2.GetDownloadsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hitchhiker.HitchhikerSource/DownloadFile',
            hitchhiker__pb2.DownloadFileRequest.SerializeToString,
            hitchhiker__pb2.DownloadFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarkDelivered(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hitchhiker.HitchhikerSource/MarkDelivered',
            hitchhiker__pb2.MarkDeliveredRequest.SerializeToString,
            hitchhiker__pb2.MarkDeliveredResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)