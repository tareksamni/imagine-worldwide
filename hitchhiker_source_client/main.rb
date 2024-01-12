this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'lib')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'hitchhiker_services_pb'

$stdout.sync = true

HITCHHIKER_HOST = ENV['HITCHHIKER_HOST'] || '127.0.0.1'
HITCHHIKER_PORT = ENV['HITCHHIKER_PORT'] || '50051'

def main
  hostname = "#{HITCHHIKER_HOST}:#{HITCHHIKER_PORT}"
  stub = Hitchhiker::HitchhikerSource::Stub.new(hostname, :this_channel_is_insecure)

  # Example call to GetDownloads
  get_downloads_request = Hitchhiker::GetDownloadsRequest.new(client_id: 'client123', destination_id: 'dest456')
  response = stub.get_downloads(get_downloads_request)
  file_list = response.file_list.to_a
  puts "Downloadable files: #{response.file_list.join(', ')}"

  # Example call to DownloadFile
  download_file_request = Hitchhiker::DownloadFileRequest.new(client_id: 'client123', file_list: file_list)
  response = stub.download_file(download_file_request)
  puts "Downloaded files:"
  response.file.each do |file|
    puts "File ID: #{file.file_id}, File Name: #{file.file_name}, Type: #{file.type}, Blob Size: #{file.blob.size}"
  end

  # Example call to MarkDelivered
  mark_delivered_request = Hitchhiker::MarkDeliveredRequest.new(client_id: 'client123', destination_id: 'dest456', file_list: file_list)
  stub.mark_delivered(mark_delivered_request)
  puts "Marked delivered."
  sleep 5
end

while true
  begin
    main
  rescue GRPC::Unavailable => e
    puts "Hitchhiker server unavailable. Retrying in 5 seconds..."
    sleep 5
  end
end
