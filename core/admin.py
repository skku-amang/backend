from django.contrib import admin

from core.models.generation import Generation
from core.models.feedback import Feedback, FeedbackQuestion, FeedbackAnswer


models = [Generation, Feedback, FeedbackQuestion, FeedbackAnswer]

(admin.site.register(model) for model in models)
