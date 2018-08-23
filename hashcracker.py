import hashlib

class Menu(object):
    def hash(string,type="md5"):
        func = eval("hashlib.%s" % type)
        return func(string.encode()).hexdigest()
    def md5(targetfile,wordlistfile):
        #CONT
