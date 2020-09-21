import json


class Response:
    def __init__(self, data, websocket_type='websocket.send'):
        if type(data) == str:
            self.data = data
        else:
            try:
                self.data = json.dumps(data)
            except Exception as ex:
                self.data = str(data)
        if type(websocket_type) != str:
            raise Exception('websocket_type must be str')
        self.websocket_type = websocket_type
