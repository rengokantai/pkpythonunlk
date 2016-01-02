__author__ = 'Hernan Y.Ke'
TAX_PER = 0.15
class TaxCN(object):
    def __init__(self):
        self.country_code = "CN"

    def __call__(self, billamount):
        return billamount * TAX_PER


class TaxUS(object):
    def __init__(self):
        self.country_code = "US"

    def __call__(self, billamount):
        if billamount < 500:
            return billamount * (TAX_PER//2)
        else:
            return billamount * TAX_PER

class TaxCalculator(object):
    def __init__(self):
        self._impl = [TaxCN(), TaxUS()] # Strategy

    def __call__(self, country, billamount):
        for impl in self._impl:
            if impl.country_code == country:
                return impl(billamount)
        else:
            return None

taxcal = TaxCalculator()
print(taxcal("CN", 400))
print(taxcal("US", 400))
