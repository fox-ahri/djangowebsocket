from .urls import urls


async def application(scope, receive, send):
    # 根据路由转发
    path = scope.get('path')
    if view := urls.get(path):
        handler = view()
        await handler.receive(receive, send)
    else:
        # 路由不匹配
        await send({'type': 'websocket.accept'})
        await send({'type': 'websocket.send', 'text': f"'{path}' 404 Not Found"})
        await send({'type': 'websocket.close'})


def get_ws_application():
    return application
