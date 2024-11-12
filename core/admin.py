from django.contrib import admin

from core.models.performance import Performance
from core.models.session import Session
from core.models.team import Team, MemberSession, MemberSessionMembership
from core.models.generation import Generation
from core.models.feedback import Feedback, FeedbackQuestion, FeedbackAnswer


models = [
    Performance,
    Session,
    Team,
    MemberSession,
    MemberSessionMembership,
    Generation,
    Feedback,
    FeedbackQuestion,
    FeedbackAnswer,
]

for model in models:
    admin.site.register(model)
