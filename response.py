import thin.response

class Response(dict):
    
    def __init__(self, pathfile, message):
        self.rp = None
        self.pathfile = pathfile
        self.message = message
        self.__decrypt()
    
    def __getitem__(self, i):
        if hasattr(self.rp, i):
            return getattr(self.rp, i)
        else:
            raise KeyError, i
    
    def __decrypt(self):
        self.rp = thin.response.remote_response(self.pathfile, self.message)
