import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reservation


class Calendar(APIView):
    def get(self, request, residence_id):
        num_days = 31
        base = datetime.datetime.today()
        date_list = [base.date() + datetime.timedelta(days=x) for x in range(num_days)]
        print(len(date_list))
        return Response({'dates': date_list})


class Reserve(APIView):
    def post(self, request):
        pass



