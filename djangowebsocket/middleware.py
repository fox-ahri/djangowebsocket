class BaseMiddleware:
    def process_request(self, request):
        """
        请求前
        :param request: request
        """
        return request

    def process_response(self, request, response):
        """
        请求后
        :param request: request
        :param response: response
        """
        return response


MIDDLEWARE = []


def middleware(mw):
    """
    注册中间件
    :param mw: 中间件类
    """
    MIDDLEWARE.append(mw)


def middlewares(mws):
    """
    注册中间件
    :param mws: 中间件类列表
    """
    for i in mws:
        MIDDLEWARE.append(i)
