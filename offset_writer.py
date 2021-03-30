from threading import Thread
from os import remove

class Writer(Thread):

    def __init__(self, in_filename, out_filename, offset):

        Thread.__init__(self)
        self.offset = offset
        self.in_filename = in_filename
        self.out_filename = out_filename

    def run(self):

        with open(self.in_filename, 'r+b') as i_f, open(self.out_filename, 'r+b') as o_f:

            bytes = i_f.read()
            o_f.seek(self.offset)
            o_f.write(bytes)

        remove(self.in_filename)
