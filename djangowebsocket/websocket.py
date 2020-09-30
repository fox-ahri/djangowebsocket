from .middleware import MIDDLEWARE
from .request import Request
from .response import Response


class BaseWebSocketView:
    """
    WebSocket 基础视图类
    """
    def __init__(self, scope, send, clients):
        self.request = Request(scope)
        self.send = send
        clients.set([self.request, send])
        self.clients = clients

    def websocket(self, request) -> Response:
        """
        视图方法，需要在子类重写，不重写将返回 默认 空字符串
        """
        return Response('', 'websocket.send')

    async def receive(self, receive):
        """
        处理请求类型的方法，接受客户端的消息时将调用 websocket 方法
        :param receive: 请求 receive
        """
        while True:
            event = await receive()
            event_type = event.get('type')
            if event_type == 'websocket.connect':
                await self.send({'type': 'websocket.accept'})
            elif event_type == 'websocket.disconnect':
                break
            else:
                self.request.data = event.get('text')
                before = []
                after = []
                for i in MIDDLEWARE:
                    before.append(i().process_request)
                    after.append(i().process_response)
                for i in before:
                    self.request = i(self.request)
                response = self.websocket(self.request)
                for i in after[::-1]:
                    response = i(self.request, response)
                await self.send({'type': response.websocket_type, 'text': response.data})
