

from django_filters.rest_framework import DateTimeFromToRangeFilter,FilterSet
# from django_filters import rest_framework as filters
from Patent_manager.models import AmendmentAction

class AmendmentActionDateRangeFilter(FilterSet):
    date_range = DateTimeFromToRangeFilter()

    class Meta:
        model = AmendmentAction
        fields = ['date_range']