from batou import Component
from batou.lib.file import File

class Test(Component):

    def configure(self):

        self += File('/tmp/test',
                     content='foo')
