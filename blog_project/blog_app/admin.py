from django.contrib import admin
from .models import Board
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('board_id', 'title', 'use_yn', 'del_yn', 'write_date', 'modif_date', 'viewcount')
    list_display_links = ['title', 'viewcount']
    list_filter = ('use_yn', 'del_yn',('write_date',DateRangeFilter),('modif_date',DateTimeRangeFilter),)
    search_fields = ('title', 'content')
    list_ordering = ("board_id",)
    date_hierarchy = 'write_date'
    actions = ['mark_as_deleted']
    fieldsets =[
        (None, {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']})
   
    ]

    def mark_as_deleted(self, request, queryset):
        queryset.update(del_yn=True)

    mark_as_deleted.short_description = "선택한 게시물을 삭제로 표시"

admin.site.register(Board, BoardAdmin)