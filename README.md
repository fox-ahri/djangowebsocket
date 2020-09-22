# Django - WebSocket

## [MyGitAddressChina](https://git.ahriknow.com/ahri/djangowebsocket)
## [Github](https://github.com/fox-ahri/djangowebsocket)

### Contact me ahriknow@gmail.com


### How to use
- install
    ```sh
    pip install djangowebsocket
    ```

- Change the contents of `asgi.py`, if your project name is `Project`
    ```python
    import os

    from django.core.asgi import get_asgi_application

    from djangowebsocket import get_ws_application
    from djangowebsocket import path, paths, middleware

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

    http_application = get_asgi_application()
    websocket_application = get_ws_application()

    # register your routers, About to support regular matching
    path('/path1/', ViewClass1)  # what is ViewClass, see below
    # or
    paths({
        '/path2/': ViewClass2,
        '/path3/': ViewClass3,
    })


    # register your middleware, it's sequential
    middleware(MiddlewareClass1)  # what is MiddlewareClass1, see below
    # or
    middlewares([MiddlewareClass2, MiddlewareClass3])


    async def branch(scope, receive, send):
        if scope.get('type') == 'websocket':
            await websocket_application(scope, receive, send)
        else:
            await http_application(scope, receive, send)


    application = branch
    ```

- Write ViewClass
    ```python
    from djangowebsocket import BaseWebSocketView, Response


    class WebSocketView(BaseWebSocketView):

        def websocket(self, request):
            # Response's data can be str, dict, list, tuple, etc.
            return Response({'test': '123'})
    ```

- Write MiddlewareClass
    ```python
    from djangowebsocket import BaseMiddleware


    class MD(BaseMiddleware):
        def process_request(self, request):
            print(request.data)  # Preprocess request
            return request

        def process_response(self, request, response):
            response.set_data({'111': 222})  # Set data by set_data
            return response

    ```

- The request hasattr:
    ```python
    QUERY  # params in path
    HEADER
    TYPE
    ASGI
    SCHEM
    SERVER
    CLIENT
    ROOT_PATH
    PATH
    RAW_PATH
    SUB_PROTOCOLS
    ```

#### 2020.09.22
