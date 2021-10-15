from django.contrib import admin
from.models import coursesData

        
class coursesDataAdmin(admin.ModelAdmin):
    list_display=['course_name',
                  'course_fee',
                  'start_date',
                  'duration',
                  'trainer_name',
                  'trainer_exp']

admin.site.register(coursesData,coursesDataAdmin)

