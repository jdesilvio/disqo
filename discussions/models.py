from django.db import models
from django.utils.encoding import python_2_unicode_compatible


MAX_TITLE_LENGTH = 200
MAX_DESCRIPTION_LENGTH = 2000
MAX_COMMENT_LENGTH = 500


@python_2_unicode_compatible
class Topic(models.Model):
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title + ' ({})'.format(self.pub_date)


@python_2_unicode_compatible
class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=MAX_COMMENT_LENGTH)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return ('[Topic {}] '.format(self.topic_id) +
                self.comment_text +
                ' ({})'.format(self.pub_date))
