import json


class Response:
    def __init__(self, data, websocket_type='websocket.send'):
        """
        :param data: 返回数据
        :param websocket_type: 返回类型 默认 'websocket.send'
        """
        if type(data) == str:
            self.__data = data
        else:
            try:
                self.__data = json.dumps(data)
            except Exception as ex:
                self.__data = str(data)
        if type(websocket_type) != str:
            raise Exception('websocket_type must be str')
        self.__websocket_type = websocket_type

    @property
    def data(self):
        """
        :return: response.data 只读 通过 set_data 设置
        """
        return self.__data

    @property
    def websocket_type(self):
        """
        :return: response.websocket_type 只读 通过 set_websocket_type 设置
        """
        return self.__websocket_type

    def set_data(self, data):
        """
        设置返回数据
        :param data: 要覆盖掉 response.data 的数据
        """
        if type(data) == str:
            self.__data = data
        else:
            try:
                self.__data = json.dumps(data)
            except Exception as ex:
                self.__data = str(data)

    def set_websocket_type(self, websocket_type):
        """
        设置返回类型
        :param websocket_type: 覆盖 response.websocket_type
        """
        if type(websocket_type) != str:
            raise Exception('websocket_type must be str')
        self.__websocket_type = websocket_type
