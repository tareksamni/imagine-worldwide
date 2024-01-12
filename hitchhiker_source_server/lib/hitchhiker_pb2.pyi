from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSourceIdRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSourceIdResponse(_message.Message):
    __slots__ = ("source_id",)
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    source_id: str
    def __init__(self, source_id: _Optional[str] = ...) -> None: ...

class GetDownloadsRequest(_message.Message):
    __slots__ = ("client_id", "destination_id")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    destination_id: str
    def __init__(self, client_id: _Optional[str] = ..., destination_id: _Optional[str] = ...) -> None: ...

class GetDownloadsResponse(_message.Message):
    __slots__ = ("file_list",)
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    file_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file_list: _Optional[_Iterable[str]] = ...) -> None: ...

class DownloadFileRequest(_message.Message):
    __slots__ = ("client_id", "file_list")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    file_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, client_id: _Optional[str] = ..., file_list: _Optional[_Iterable[str]] = ...) -> None: ...

class File(_message.Message):
    __slots__ = ("file_id", "file_name", "type", "blob")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    file_name: str
    type: str
    blob: bytes
    def __init__(self, file_id: _Optional[str] = ..., file_name: _Optional[str] = ..., type: _Optional[str] = ..., blob: _Optional[bytes] = ...) -> None: ...

class DownloadFileResponse(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _containers.RepeatedCompositeFieldContainer[File]
    def __init__(self, file: _Optional[_Iterable[_Union[File, _Mapping]]] = ...) -> None: ...

class MarkDeliveredRequest(_message.Message):
    __slots__ = ("client_id", "destination_id", "file_list")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    destination_id: str
    file_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, client_id: _Optional[str] = ..., destination_id: _Optional[str] = ..., file_list: _Optional[_Iterable[str]] = ...) -> None: ...

class MarkDeliveredResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
