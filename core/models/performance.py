from django.db import models


class Performance(models.Model):
    name = models.CharField(max_length=255, verbose_name="이름")
    description = models.TextField(blank=True, null=True, verbose_name="설명")
    representativeImage = models.ImageField(upload_to="performance/", null=True, verbose_name="대표 이미지")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="장소")
    startDatetime = models.DateTimeField(blank=True, null=True, verbose_name="시작 일시")
    endDatetime = models.DateTimeField(blank=True, null=True, verbose_name="종료 일시")

    createdDatetime = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updatedDatetime = models.DateTimeField(auto_now=True, verbose_name="수정 일시")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["-createdDatetime"]
        verbose_name = "공연"
        verbose_name_plural = "공연"
