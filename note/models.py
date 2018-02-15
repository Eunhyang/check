from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField('이름', max_length=100)
    parent = models.ForeignKey('self', models.SET_NULL, null=True, blank=True, verbose_name='상위 분류')

    def __str__(self):
        return f'{self.parent.name}/{self.name}' if self.parent else self.name

    class Meta:
        verbose_name = '분류'
        verbose_name_plural = verbose_name


class Issue(TimeStampedModel):
    parent = models.ForeignKey('self', models.SET_NULL, null=True, blank=True, verbose_name='상위 이슈')
    status = models.PositiveSmallIntegerField('상태', choices=[
        (1, '보류'),
        (2, '완료')
    ], null=True, blank=True)
    content = models.TextField('내용')
    code_place = models.TextField('코드 위치', null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name='분류')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '이슈'
        verbose_name_plural = verbose_name


class Memo(TimeStampedModel):
    content = models.TextField('내용')
    issue = models.ForeignKey(
        Issue, models.SET_NULL, null=True, blank=True,
        verbose_name='분류')
    is_base = models.BooleanField('기준 카테고리', default=False)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '메모'
