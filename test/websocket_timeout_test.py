import websocket
import time

def on_open(ws):
    print("WebSocket opened, sending test message...")
    ws.send("Test message")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def test_websocket_timeout():
    try:
        # Start the WebSocket connection with a timeout of 5 seconds
        ws = websocket.WebSocketApp("ws://localhost:3000", 
                                    on_open=on_open,
                                    on_error=on_error,
                                    on_close=on_close)
        
        # Set the ping_interval to 1 second, ping_timeout to 5 seconds
        ws.run_forever(ping_interval=1, ping_timeout=5)

    except Exception as e:
        print(f"Error during WebSocket connection: {e}")

if __name__ == "__main__":
    test_websocket_timeout()
