import sys
sys.path.insert(0, './lib')

from concurrent.futures import ThreadPoolExecutor
import os
import signal
import multiprocessing
import grpc
import time
from lib.analytics_manager import AnalyticsManager
from lib.hitchhiker_pb2 import *
from lib.hitchhiker_pb2_grpc import HitchhikerSourceServicer, add_HitchhikerSourceServicer_to_server

# Set environment variables
SOURCE_ID = os.getenv('SOURCE_ID', 'pilot04')
HITCHHIKER_HOST = os.getenv('HITCHHIKER_HOST', '127.0.0.1')
HITCHHIKER_PORT = os.getenv('HITCHHIKER_PORT', '50051')
ANALYTICS_DATA_DIR = os.getenv('ANALYTICS_DATA_DIR', '../data/countly/received')
MAX_STORAGE_MB = os.getenv('MAX_STORAGE_MB', '100')

class HitchhikerServer(HitchhikerSourceServicer):
    def __init__(self):
        self.analytics_manager = AnalyticsManager(ANALYTICS_DATA_DIR)

    def GetSourceId(self, request, context):
        print("Received GetSourceId request")
        return GetSourceIdResponse(source_id=SOURCE_ID)

    def GetDownloads(self, request, context):
        print(f"Received GetDownloads request: {request}")
        file_list = self.analytics_manager.list_of_files()
        return GetDownloadsResponse(file_list=file_list)

    def DownloadFile(self, request, context):
        print(f"Received DownloadFile request: {request}")
        file_details = [self.analytics_manager.details(filename) for filename in request.file_list]
        result = [File(**details) for details in file_details if details is not None]
        return DownloadFileResponse(file=result)

    def MarkDelivered(self, request, context):
        for file in request.file_list:
            self.analytics_manager.remove_file(file)
        return MarkDeliveredResponse()

def grpc_server():
    print("Starting GRPC server")
    server = grpc.server(ThreadPoolExecutor())
    add_HitchhikerSourceServicer_to_server(HitchhikerServer(), server)
    server.add_insecure_port(f"{HITCHHIKER_HOST}:{HITCHHIKER_PORT}")
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)
        print("GRPC Server: Received shutdown signal")

def garbage_collector():
    print("Starting garbage collector")
    analytics_manager = AnalyticsManager(ANALYTICS_DATA_DIR, max_storage_mb=int(MAX_STORAGE_MB))
    try:
        while True:
            print("Garbage Collector: cleaning up")
            analytics_manager.remove_old_files()
            time.sleep(15)
    except KeyboardInterrupt:
        print("Garbage Collector: Received shutdown signal")

def signal_handler(sig, frame):
    print('Received shutdown signal. Exiting gracefully...')
    sys.exit(0)

if __name__ == '__main__':
    from functools import partial
    print = partial(print, flush=True)

    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Start your processes
    gc_process = multiprocessing.Process(target=garbage_collector)
    grpc_process = multiprocessing.Process(target=grpc_server)

    gc_process.start()
    grpc_process.start()

    # Wait for the processes to finish
    gc_process.join()
    grpc_process.join()
