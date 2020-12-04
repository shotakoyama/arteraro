from erarigilo.util.noiser import Noiser
from erarigilo.en.util.token import EnToken
from erarigilo.en.util.sent import EnSent

class EnNoiser(Noiser):
    def sent_decode(self, sent):
        sent = EnSent.decode(sent, token_class = EnToken)
        return sent

