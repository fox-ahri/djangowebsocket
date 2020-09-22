URLS = dict()


def path(url: str, handler):
    """
    :param url: 路由
    :param handler: BaseWebSocketView 的子类
    """
    URLS[url] = handler


def paths(mapping: dict):
    """
    :param mapping: 路由 -> 视图类 的映射
    """
    for k in mapping.keys():
        URLS[k] = mapping[k]


def get_urls() -> dict:
    """
    :return: 所有 Websocket 路由
    """
    return URLS
