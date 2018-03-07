#-*- coding: utf-8 -*-

class Pai(object):

    def sobrescrever(self):
        print "Pai"

class Filho(Pai):

    def __init__(self, *args, **kwargs):
        super(Filho, self).__init__(*args, **kwargs)

    def sobrescrever(self):
        super(Filho, self).sobrescrever()
        print "Filho"

class Filha(Pai):

    def __init__(self, *args, **kwargs):
        super(Filha, self).__init__(*args, **kwargs)

    def sobrescrever(self):
        super(Filha, self).sobrescrever()
        print "Filha"

filha = Filha()
filha.sobrescrever()

filho = Filho()
filho.sobrescrever()
