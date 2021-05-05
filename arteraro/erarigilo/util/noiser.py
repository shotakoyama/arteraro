from .sampler import *
import sys
import json
import logging
from logging import getLogger, Formatter, StreamHandler
logger = getLogger(__name__)
logging.basicConfig(format='[%(asctime)s] (%(levelname)s) %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.DEBUG, stream=sys.stderr)

class Noiser:
    def __init__(self, generator_list, ratio=0.0, lang_list=None):
        self.generator_list = generator_list
        self.ratio = ratio
        self.lang_list = lang_list
        if lang_list is not None:
            self.uniform_sampler = UniformSampler()
            self.choice_sampler = ChoiceSampler(lang_list)

    def batch_decode(self, batch):
        for line in batch:
            line = line.strip()
            dct = json.loads(line)
            sent = self.sent_decode(dct)
            yield sent

    def batch_encode(self, batch):
        for sent in batch:
            sent = sent.encode()
            sent = json.dumps(sent, ensure_ascii = False)
            yield sent

    def __call__(self, batch):
        batch = self.batch_decode(batch)

        logger.info('start error generation')
        for index, (generator, dct) in enumerate(self.generator_list, start=1):
            manager = generator(dct)
            logger.info('rule {}: {}'.format(index, manager.mistaker.name))
            batch = [manager(sent) for sent in batch]
        batch = self.batch_encode(batch)
        return batch

