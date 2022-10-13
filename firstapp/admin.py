from django.contrib import admin
from firstapp.models import usermember, course_details, student_details

# Register your models here.
admin.site.register(usermember)
admin.site.register(course_details)
admin.site.register(student_details)
