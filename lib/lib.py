#classe para manipular o socket
class Send:
    def __init__(self):
        self.__msg=''
        self.new=True
        self.con=None
    def put(self,msg):
        self.__msg=msg
        if self.con != None:
        #envia um mensagem atravez de uma conexão socket
            self.con.send(str.encode(self.__msg))
    def get(self):
        return self.__msg
        def loop(self):
            return self.new
