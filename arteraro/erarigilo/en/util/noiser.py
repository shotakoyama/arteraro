from arteraro.erarigilo.util.noiser import Noiser
from .token import EnToken
from .sent import EnSent
from arteraro.erarigilo.en.form import form_trg

class EnNoiser(Noiser):
    def is_sampled(self, dct):
        if self.ratio == 0.0:
            return False

        if self.lang_list is None:
            return False

        if all(dct[lang] is None for lang in self.lang_list):
            return False

        p = self.uniform_sampler()
        return p < self.ratio

    def sample_language(self, dct):
        assert self.lang_list is not None
        assert any(dct[lang] is not None for lang in self.lang_list)

        lang = self.choice_sampler()
        while dct[lang] is None:
            lang = self.choice_sampler()
        return lang

    def sent_decode(self, dct):
        if self.is_sampled(dct):
            lang = self.sample_language(dct)
            sent = dct[lang]
            sent['trg'] = {'bridge': lang, 'text': form_trg(EnSent.decode(dct['trg'], token_class = EnToken))}
        else:
            sent = dct['trg']

        sent = EnSent.decode(sent, token_class = EnToken)
        return sent

