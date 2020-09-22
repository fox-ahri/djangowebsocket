class Request:
    QUERY = {}
    HEADER = {}

    def to_string(self, byte):
        return str(byte, encoding="utf-8")

    def __init__(self, scope):
        """
        封装 request
        :param scope: 请求 scope
        """
        try:
            for i in self.to_string(scope.get('query_string', b'')).split('&'):
                tmp = i.split('=')
                self.QUERY[tmp[0]] = tmp[1]
        except Exception as ex:
            raise Exception('Analysis query_string error: ' + str(ex))
        try:
            for i in scope.get('headers', []):
                self.HEADER[self.to_string(i[0])] = self.to_string(i[1])
        except Exception as ex:
            raise Exception('Analysis headers error: ' + str(ex))
        self.TYPE = scope.get('type')
        self.ASGI = scope.get('asgi')
        self.SCHEME = scope.get('scheme')
        self.SERVER = scope.get('server')
        self.CLIENT = scope.get('client')
        self.ROOT_PATH = scope.get('root_path')
        self.PATH = scope.get('path')
        self.RAW_PATH = scope.get('raw_path')
        self.SUB_PROTOCOLS = scope.get('subprotocols')
