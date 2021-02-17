from .sampler import *
import sys
import json

class Noiser:
    def __init__(self, *args):
        self.args = args

    def batch_decode(self, batch):
        for sent in batch:
            sent = sent.strip()
            sent = json.loads(sent)
            sent = self.sent_decode(sent)
            yield sent

    def batch_encode(self, batch):
        for sent in batch:
            sent = sent.encode()
            sent = json.dumps(sent, ensure_ascii = False)
            yield sent

    def __call__(self, batch):
        batch = self.batch_decode(batch)
        for generator, dct in self.args:
            manager = generator(dct)
            print(manager.mistaker.name, file = sys.stderr)
            batch = [manager(sent) for sent in batch]
        batch = self.batch_encode(batch)
        return batch

