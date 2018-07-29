from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator

class RangeIntegerField(IntegerField):

    def __init__(self, min=None, max=None, *args, **kwargs):
        kwargs['validators'] = kwargs.get('validators', [])
        if min is not None:
            kwargs['validators'].append(MinValueValidator(min))
        if max is not None:
            kwargs['validators'].append(MaxValueValidator(max))
        super(RangeIntegerField, self).__init__(*args, **kwargs)


class PercentageField(RangeIntegerField):

    def __init__(self, *args, **kwargs):
        kwargs['min'] = kwargs.get('min', None) or 0
        kwargs['max'] = kwargs.get('max', None) or 100
        super(PercentageField, self).__init__(*args, **kwargs)
