from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from core.models.performance import Performance
from core.models.session import Session
from core.models.team import Team, MemberSession, MemberSessionMembership
from core.models.generation import Generation
from core.models.feedback import Feedback, FeedbackQuestion, FeedbackAnswer


class PerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_with_image",
        "description",
        "location",
        "feedback_link",
        "startDatetime",
        "endDatetime",
    )
    list_display_links = ("id", "name_with_image")
    list_select_related = ("feedback",)
    search_fields = ("name",)
    ordering = ("startDatetime",)

    def name_with_image(self, obj):
        if obj.representativeImage:
            return format_html(
                f"""
                <div style="display:flex; align-items:center;">
                <img src="{obj.representativeImage.url}" style="width: 50px; height: auto;" />
                {obj.name}
                </div>"""
            )
        return "-"

    name_with_image.short_description = "대표 이미지"

    def feedback_link(self, obj):
        if obj.feedback:
            url = reverse("admin:core_feedback_change", args=[obj.feedback.id])
            return format_html('<a href="{}">{}</a>', url, obj.feedback)
        return "-"

    feedback_link.short_description = "피드백"


class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "songName", "performance_link", "leader")
    list_display_links = ("id", "name")
    list_filter = ("performance",)
    list_select_related = ("performance",)
    search_fields = ("name",)
    ordering = ("performance", "createdDatetime")

    def performance_link(self, obj):
        if obj.performance:
            url = reverse("admin:core_performance_change", args=[obj.performance.id])
            return format_html('<a href="{}">{}</a>', url, obj.performance)
        return "-"

    performance_link.short_description = "Performance"


admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Team, TeamAdmin)

models = [
    Session,
    MemberSession,
    MemberSessionMembership,
    Generation,
    Feedback,
    FeedbackQuestion,
    FeedbackAnswer,
]

for model in models:
    admin.site.register(model)
