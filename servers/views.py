from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.conf import settings
from .models import Server
from .serializers import ServerSerializer
from .utils import send_mail_fn
ADMIN_EMAIL = settings.ADMIN_EMAIL


class ServerList(ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs['pk'])

    def get_object(self):
        return self.get_queryset().get()


class ServerCreate(ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def perform_create(self, serializer):
        subject = 'Server Created'
        message = 'You have successfully created a server'
        email = self.request.user.email
        sender = ADMIN_EMAIL
        to_email = email
        send_mail_fn(request=self.request, sender=sender, subject=subject, message=message, to_email=to_email,
                     user='Member')
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ServerUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def perform_update(self, serializer):
        subject = 'Server Updated'
        message = 'You have successfully updated a server'
        email = self.request.user.email
        sender = ADMIN_EMAIL
        to_email = email
        send_mail_fn(request=self.request, sender=sender, subject=subject, message=message, to_email=to_email,
                     user='Member')
        serializer.save()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        subject = 'Server Deleted'
        message = 'You have successfully deleted a server'
        email = self.request.user.email
        sender = ADMIN_EMAIL
        to_email = email
        send_mail_fn(request=self.request, sender=sender, subject=subject, message=message, to_email=to_email,
                     user='Member')
        return self.destroy(request, *args, **kwargs)


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

