import websocket
import threading
import time

def on_message(ws, message):
    print(f"Received message: {message}")
    assert message == "Test message", "Message received is not as expected"
    ws.close()

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def on_open(ws):
    print("WebSocket opened, sending test message...")
    ws.send("Test message")

def test_websocket():
    ws = websocket.WebSocketApp("ws://localhost:3000", 
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    test_websocket()
