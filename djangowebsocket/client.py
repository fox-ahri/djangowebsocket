class Client:
    CLIENTS = []

    def set(self, client):
        """
        保存连接客户端
        """
        self.CLIENTS.append(client)

    def get(self):
        """
        获取所有连接客户端
        """
        return self.CLIENTS
