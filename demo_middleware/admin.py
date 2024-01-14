import json

from django.contrib import admin

from django.core.serializers.json import DjangoJSONEncoder

from .models import NewStats


@admin.register(NewStats)
class NewStatsAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        stat_data = (
            NewStats.objects.annotate().values("win", "mac", "iph", "android", "oth")
        )

        # data = NewStats.objects.all()
        # NewStats = serializers.serialize('json', list(data), fields=("win","mac","iph","android","oth"))
        # print(NewStats)

        as_json = json.dumps(list(stat_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"stat_data": as_json}

        return super().changelist_view(request, extra_context=extra_context)
