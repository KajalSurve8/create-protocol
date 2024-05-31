import django_tables2 as tables
from .models import ScheduleOne

class PersonTable(tables.Table):
    class Meta:
        model = ScheduleOne
        template_name = "django_tables2/semantic.html"
        # fields = ("name", )
        exclude = ("sl",)


# import django_tables2 as tables
# from .models import ScheduleOne

# class PersonTable(tables.Table):
#     class Meta:
#         model = ScheduleOne
#         template_name = "django_tables2/semantic.html"
#         # fields = ("name", )
#         exclude = ("sl",)