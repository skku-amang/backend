from django.db import models


class Feedback(models.Model):
    performance = models.ForeignKey(
        "core.Performance", on_delete=models.CASCADE, related_name="feedbacks"
    )
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)
    startDatetime = models.DateTimeField()
    endDatetime = models.DateTimeField()


class FeedbackQuestion(models.Model):
    STRING = 'string'
    INTEGER = 'int'
    QUESTION_TYPE_CHOICES = [
        (STRING, 'String'),
        (INTEGER, 'Integer'),
    ]

    feedback = models.ForeignKey(
        Feedback, on_delete=models.CASCADE, related_name="questions"
    )
    question = models.TextField()
    questionType = models.CharField(
        max_length=50,
        choices=QUESTION_TYPE_CHOICES,
        default=STRING,
    )
    order = models.IntegerField()
    isRequired = models.BooleanField(default=True)


class FeedbackAnswer(models.Model):
    question = models.ForeignKey(
        FeedbackQuestion, on_delete=models.CASCADE, related_name="answers"
    )
    answer = models.TextField()
    user = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)
