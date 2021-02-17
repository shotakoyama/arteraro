from arteraro.erarigilo.util.noiser import Noiser
from .token import EnToken
from .sent import EnSent

class EnNoiser(Noiser):
    def sent_decode(self, sent):
        sent = EnSent.decode(sent, token_class = EnToken)
        return sent

