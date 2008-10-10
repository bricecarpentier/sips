from BeautifulSoup import BeautifulSoup
import thin.request

class Request(dict):
    def __init__(self, pathfile):
        self.cp = thin.request.init()
        self.soup = ''
        self.bsoup = ''
        self.encrypted = ''
        self.pathfile = pathfile
    
    def __setitem__(self, i, y):
        if hasattr(self.cp, i):
            setattr(self.cp, i, y)
    
    def __getitem__(self, i):
        if hasattr(self.cp, i):
            return getattr(self.cp, i)
    
    def encrypt(self):
        self.soup = thin.request.remote_call(self.cp, self.pathfile)
        self.bsoup = BeautifulSoup(soup)
        self.encrypted = bsoup.find('input', {'name': 'DATA'})['value']
        return encrypted