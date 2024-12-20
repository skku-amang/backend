from django.db import models


class Feedback(models.Model):
    performance = models.OneToOneField(
        "core.Performance", on_delete=models.CASCADE, related_name="feedback", verbose_name="공연"
    )
    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)
    startDatetime = models.DateTimeField()
    endDatetime = models.DateTimeField()

    def __str__(self):
        return f"{self.performance} 피드백"

    class Meta:
        ordering = ["-createdDatetime"]
        verbose_name = "피드백"
        verbose_name_plural = "피드백"


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
    answerType = models.CharField(
        max_length=50,
        choices=QUESTION_TYPE_CHOICES,
        default=STRING,
    )
    order = models.IntegerField()
    isRequired = models.BooleanField(default=True)

    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.feedback} 질문{self.order}: {self.question}"

    class Meta:
        ordering = ["-createdDatetime"]
        verbose_name = "피드백 질문"
        verbose_name_plural = "피드백 질문"


class FeedbackAnswer(models.Model):
    question = models.ForeignKey(
        FeedbackQuestion, on_delete=models.CASCADE, related_name="answers"
    )
    answer = models.TextField()
    respondent = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE, verbose_name="답변자")
    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.question} - {self.respondent}: {self.answer}"

    class Meta:
        ordering = ["-createdDatetime"]
        verbose_name = "피드백 답변"
        verbose_name_plural = "피드백 답변"
