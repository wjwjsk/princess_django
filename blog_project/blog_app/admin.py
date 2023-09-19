from django.contrib import admin
from .models import Board, Topic
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = (
        "board_id",
        "title",
        "use_yn",
        "del_yn",
        "write_date",
        "modif_date",
        "viewcount",
        "topic_id",
    )
    list_display_links = ["title", "viewcount"]
    list_filter = (
        "use_yn",
        "del_yn",
        ("write_date", DateRangeFilter),
        ("modif_date", DateTimeRangeFilter),
    )
    search_fields = ("title", "content")
    list_ordering = ("board_id",)
    date_hierarchy = "write_date"
    actions = ["mark_as_deleted"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
        ("Topic information", {"fields": ["topic_id"]}),  # topic_id 필드 추가
    ]

    def mark_as_deleted(self, request, queryset):
        queryset.update(del_yn=True)

    mark_as_deleted.short_description = "선택한 게시물을 삭제로 표시"


class TopicAdmin(admin.ModelAdmin):
    list_display = ("topic_id", "name", "use_yn")
    actions = ["add_topic", "delete_topic"]

    def delete_topic(self, request, queryset):
        for obj in queryset:
            # 해당 토픽이 사용되고 있는 모든 게시물 가져오기
            related_boards = Board.objects.filter(topic=obj)

            # 토픽 삭제
            obj.delete()

            # 관련 게시물 삭제
            related_boards.delete()

    delete_topic.short_description = "토픽 삭제"


admin.site.register(Topic, TopicAdmin)
admin.site.register(Board, BoardAdmin)
