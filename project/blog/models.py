from django.db import models
from django.conf import settings
import os

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=20) #글자 수 제한 있음
    content=models.TextField() #글자수 제한 없음
    created_at=models.DateTimeField(auto_now_add=True) #auto_now_add 처음 생성할 때만 업데이트한다. add없으면 수정가능
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Blog, self).delete(*args, **kargs)