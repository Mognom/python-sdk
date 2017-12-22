"""Amount module."""
from catalogs.currency import CURRENCIES
import re


class Amount:
    """Amount class."""

    def __init__(self, amount, currency):
        """Initialize Amount."""
        self.amount = amount
        self.currency = currency

    @property
    def currency(self):
        """Getter of currency."""
        return self._currency[0]

    @currency.setter
    def currency(self, currency):
        if not isinstance(currency, str):
            raise TypeError('currency must be a string.')

        if currency not in CURRENCIES:
            raise ValueError('value of currency is incorrect.')

        self._currency = CURRENCIES[currency]

    @property
    def amount(self):
        """Getter of amount."""
        return self._amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, str) and \
           re.match(r'^([0-9]+)|([0-9]+\.[0-9]+)$', amount):
            amount = amount.replace('.', '')
            amount = int(amount)

        elif not isinstance(amount, int):
            raise TypeError('amount must have a correct format.')

        if amount <= 0:
            raise ValueError('value of amount is incorrect.')

        self._amount = amount

    # TODO: hacer sobrecarga de operadores + - < > <= >= == !=
    # def __add__(self, other):
    #     """Operator +."""
    #     if not isinstance(other, Amount):
    #         raise TypeError('Second argument must be a Amount.')
    #
    #     if self.currency != other.currency:
    #         raise TypeError('You can not add two amounts with different currencies.')  # noqa

    def __str__(self):
        """Parse to string."""
        decimal = self.currency[2]
        fmt_amount = str(self.amount).zfill(decimal + 1)
        return fmt_amount[:-decimal] + '.' + fmt_amount[-decimal:]
