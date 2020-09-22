from .urls import URLS
from .client import Client


async def application(scope, receive, send):
    """
    接收 websocket 请求的 application
    """
    clients = Client()
    # 根据路由转发
    path = scope.get('path')
    if view := URLS.get(path):
        handler = view(scope, send, clients)
        await handler.receive(receive)
    else:
        # 路由不匹配 404
        await send({'type': 'websocket.accept'})
        await send({'type': 'websocket.send', 'text': f"'{path}' 404 Not Found"})
        await send({'type': 'websocket.close'})


def get_ws_application():
    return application
