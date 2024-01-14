from django.db.models import F

from .models import NewStats


class DemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def stats(os_info):
        if "Windows" in os_info:
            NewStats.objects.all().update(win=F('win') + 1)
        elif "mac" in os_info:
            NewStats.objects.all().update(mac=F('mac') + 1)
        elif "iPhone" in os_info:
            NewStats.objects.all().update(iph=F('iph') + 1)
        elif "Android" in os_info:
            NewStats.objects.all().update(android=F('android') + 1)
        else:
            NewStats.objects.all().update(oth=F('oth') + 1)

    def __call__(self, request, *args, **kwargs):
        if "admin" not in request.path:
            self.stats(request.META['HTTP_USER_AGENT'])
        response = self.get_response(request)

        # print(request.path)
        # print(request.headers['Host'])
        # print(request.headers['Accept-Language'])
        # print(request.META['REQUEST_METHOD'])
        # print(request.META['HTTP_USER_AGENT'])
        return response
