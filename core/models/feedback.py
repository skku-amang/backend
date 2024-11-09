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


# 피드백 템플릿
# exmaple
# 1. 정기공연 전용 질문지 // 개인, 팀, 선호도, 기타
# 2. 방학공연 전용 질문지 // 팀, 선호도, 기타
class FeedbackTemplate(models.Model):
    feedback = models.ForeignKey(
        Feedback, on_delete=models.CASCADE, related_name="templates"
    )
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)


# 질문 문항
# exmaple
# 1. "이번 세션에 대한 전반적인 만족도를 평가해주세요."
# 2. "이번 세션에서 가장 만족스러웠던 점은 무엇인가요?"
# 3. "이번 세션에서 가장 아쉬웠던 점은 무엇인가요?"
class FeedbackQuestion(models.Model):
    STRING = 'string'
    INTEGER = 'int'
    QUESTION_TYPE_CHOICES = [
        (STRING, 'String'),
        (INTEGER, 'Integer'),
    ]

    template = models.ForeignKey(
        FeedbackTemplate, on_delete=models.CASCADE, related_name="questions"
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