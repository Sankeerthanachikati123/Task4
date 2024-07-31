from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
from fastapi.responses import HTMLResponse

app = FastAPI()
html="""
<!DOCTYPE html>
<html>
<head>
    <title>Client2 Chat</title>
</head>
<body>
    <h1>Client2 Chat</h1>
    <textarea id="chat" cols="30" rows="10" readonly></textarea><br>
    <input type="text" id="message" autocomplete="off">
    <button onclick="sendMessage()">Send</button>

    <script>
        var ws = new WebSocket("ws://127.0.0.1:8000/ws/client2");

        ws.onmessage = function(event) {
            var chat = document.getElementById('chat');
            chat.value += event.data + "\n";
        };

        function sendMessage() {
            var input = document.getElementById("message");
            ws.send(input.value);
            input.value = '';
        }
    </script>
</body>
</html>
"""
@app.get("/")
def get():
    return HTMLResponse(html)
class ConnectionManager:
    def __init__(self):
        self.client1_connections: List[WebSocket] = []
        self.client2_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket, client_type: str):
        await websocket.accept()
        if client_type == "client1":
            self.client1_connections.append(websocket)
        elif client_type == "client2":
            self.client2_connections.append(websocket)

    def disconnect(self, websocket: WebSocket, client_type: str):
        if client_type == "client1":
            self.client1_connections.remove(websocket)
        elif client_type == "client2":
            self.client2_connections.remove(websocket)

    async def send_message(self, message: str, client_type: str):
        if client_type == "client1":
            for connection in self.client1_connections:
                await connection.send_text(message)
        elif client_type == "client2":
            for connection in self.client2_connections:
                await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/client1")
async def websocket_endpoint_client1(websocket: WebSocket):
    await manager.connect(websocket, client_type="client1")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"Client1 says: {data}", client_type="client2")
    except WebSocketDisconnect:
        manager.disconnect(websocket, client_type="client1")
        await manager.send_message("Client1 disconnected", client_type="client2")

@app.websocket("/ws/client2")
async def websocket_endpoint_client2(websocket: WebSocket):
    await manager.connect(websocket, client_type="client2")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"Client2 says: {data}", client_type="client1")
    except WebSocketDisconnect:
        manager.disconnect(websocket, client_type="client2")
        await manager.send_message("Client2 disconnected", client_type="client1")

