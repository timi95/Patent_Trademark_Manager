

from django_filters.rest_framework import DateTimeFromToRangeFilter,FilterSet
# from django_filters import rest_framework as filters
from Patent_manager.models import AmendmentAction

def AmendmentActionDateRangeFilter_class_gen(Object):
    class AmendmentActionDateRangeFilter(FilterSet):
        date = DateTimeFromToRangeFilter()

        class Meta:
            model = Object
            fields = ['date']
    return AmendmentActionDateRangeFilter