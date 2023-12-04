import datetime

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reservation, Residence


class Calendar(APIView):
    def get(self, request, residence_id):
        num_days = 31
        base = datetime.datetime.today()
        date_list = []
        for x in range(num_days):
            dd = base + datetime.timedelta(days=x)
            residence = Residence.objects.exclude(Q(reserve__reservation_start_date__date__gte=dd) & Q(reserve__reservation_end_date__date__lte=dd))\
                                         .values_list('id', flat=True)
            # residence = Residence.objects.all()
            date_list.append({str(dd.date()): residence})
        # date_list = [base.date() + datetime.timedelta(days=x) for x in range(num_days)]

        print(len(date_list))
        return Response({'dates': date_list})


class Reserve(APIView):
    def post(self, request):
        pass



