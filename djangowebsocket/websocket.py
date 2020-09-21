from .response import Response


class BaseWebSocketView:
    """
    WebSocket 基础视图类
    """
    # 连接客户端
    clients = {}

    def websocket(self, request) -> Response:
        """
        视图方法，需要在子类重写，不重写将返回 默认 空字符串
        """
        return Response('', 'websocket.send')

    async def receive(self, receive, send):
        """
        处理请求类型的方法，接受客户端的消息时将调用 websocket 方法
        :param receive: 请求 receive
        :param send: 请求 send
        """
        while True:
            event = await receive()
            event_type = event.get('type')
            if event_type == 'websocket.connect':
                await send({'type': 'websocket.accept'})
            elif event_type == 'websocket.disconnect':
                await send({'type': 'websocket.close'})
            else:
                response = self.websocket(event.get('text'))
                await send({'type': response.websocket_type, 'text': response.data})
