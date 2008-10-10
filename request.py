from __future__ import absolute_import

from BeautifulSoup import BeautifulSoup

from .thin import request

class Request(dict):
    def __init__(self, pathfile):
        self.cp = request.init()
        self.soup = ''
        self.bsoup = ''
        self.elements = {}
        self.pathfile = pathfile
    
    def __setitem__(self, i, y):
        if hasattr(self.cp, i):
            setattr(self.cp, i, y)
    
    def __getitem__(self, i):
        if hasattr(self.cp, i):
            return getattr(self.cp, i)
    
    def encrypt(self):
        self.soup = request.remote_call(self.cp, self.pathfile)
        self.bsoup = BeautifulSoup(self.soup)
        self.elements['action'] = self.bsoup.find('form')['action']
        self.elements['encrypted'] = self.bsoup.find('input', 
                                        {'name': 'DATA'})['value']
        self.elements['means'] = [ item['name'] for item in 
                                    self.bsoup.find('input', {'type': 'image'})
        return self.elements
