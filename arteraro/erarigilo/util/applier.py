class TokenWiseApplier:
    def apply(self, sent, lottery):
        for index in range(len(sent)):
            if self.mistaker.cond(sent[index]) and lottery():
                sent[index] = self.mistaker(sent[index])
        return sent


class IndexWiseApplier:
    def apply(self, sent, lottery):
        for index in range(len(sent)):
            if self.mistaker.cond(sent, index) and lottery():
                sent = self.mistaker(sent, index)
        return sent


class SpanWiseApplier:
    def apply(self, sent, lottery):
        span_list = self.mistaker.extract_span(sent)
        for span in span_list:
            if lottery():
                sent = self.mistaker(sent, span)
        return sent

