from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Server
from .serializers import ServerSerializer


class ServerList(ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


# class DnsRecordList(ListCreateAPIView):
#     queryset = DnsRecord.objects.all()
#     serializer_class = DnsRecordSerializer
#
#
# class DnsRecordDetail(RetrieveUpdateDestroyAPIView):
#     queryset = DnsRecord.objects.all()
#     serializer_class = DnsRecordSerializer
#
#
# class DnsDetailsList(ListCreateAPIView):
#     queryset = DnsDetails.objects.all()
#     serializer_class = DnsDetailsSerializer
#
#
# class DnsDetailsDetail(RetrieveUpdateDestroyAPIView):
#     queryset = DnsDetails.objects.all()
#     serializer_class = DnsDetailsSerializer

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l2 = [1, 2, 3, 4]
# find the same elements in both lists
# and return a list of those elements

# def find_same_elements(l1, l2):
#     return [x for x in l1 if x in l2]


# count repeated letters in a string

# def count_repeated_letters(string):
#     count = 0
#     for i in range(len(string)):
#         if string[i] == string[i - 1]:
#             count += 1
#     return count
#
# print(count_repeated_letters('aaabbbcc'))

