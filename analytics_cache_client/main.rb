require 'net/http'
require 'uri'
require 'json'
require 'securerandom'

$stdout.sync = true

SERVER_URL = "http://#{ENV['ANALYTICS_SERVER_HOST']}:#{ENV['ANALYTICS_SERVER_PORT']}/i"

# Infinite loop
while true
  begin
    # Generate a random device_id
    random_device_id = SecureRandom.hex(8)

    # Get current timestamp in milliseconds
    timestamp = (Time.now.to_f * 1000).to_i

    # Define the fake data payload
    data = {
      "app_key" => "aee33f197f73bc5f7ca99261a6f253caa2d4f614",
      "timestamp" => timestamp.to_s,
      "hour" => "14",
      "dow" => "1",
      "tz" => "-420",
      "sdk_version" => "20.04",
      "sdk_name" => "java-native-android",
      "user_details" => "{\"custom\":{\"device_id\":\"QPY2\",\"ota\":\"1\"}}",
      "device_id" => random_device_id,
      "checksum" => "36cf731444de656fb03794cf1856dce1fe0b4a23"
    }

    # Set up the URI and HTTP request
    uri = URI.parse(SERVER_URL)
    http = Net::HTTP.new(uri.host, uri.port)
    request = Net::HTTP::Post.new(uri.request_uri)

    # Add the data to the request
    request.body = "events=" + data.to_json

    # Perform the request
    http.request(request)
    sleep(1)
  rescue => e
    puts "Error: #{e}"
  end
end
