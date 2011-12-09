"""Plugin prototype"""


class Plugin(object):
    runlevel = 0
    remote = True

    def __init__(self, scanner):
        self.scanner = scanner

    def start(self):
        print "- Start prototype plugin"
