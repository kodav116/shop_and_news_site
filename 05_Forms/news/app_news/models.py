from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)


class Commentary(models.Model):
    news_at = models.ForeignKey(News, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    comment = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user_name, self.created_at)





