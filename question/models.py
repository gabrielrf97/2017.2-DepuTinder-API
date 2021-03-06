from django.db import models

# Create your models here.

TITLE_LENGTH = 100
SUBTITLE_LENGTH = 150
DESCRIPTION_LENGTH = 200
AUTHOR_LENGTH = 50
LINK_LENGTH = 5000

class Question(models.Model):
    proposition = models.ForeignKey(
        'propositions.Propositions',
        on_delete=models.CASCADE,
        related_name='proposition',
        default=0
    )
    questionnaire = models.ForeignKey(
        'questionnaire.Questionnaire',
        on_delete=models.CASCADE,
        related_name='%(class)s_questionnaire',
        default=0
    )
    questionTitle = models.CharField(max_length=TITLE_LENGTH, blank=True)
    questionSubtitle = models.CharField(max_length=SUBTITLE_LENGTH, blank=True)
    questionDescription = models.CharField(max_length=DESCRIPTION_LENGTH, blank=True)
    questionAuthor = models.CharField(max_length=AUTHOR_LENGTH, blank=True)
    questionLink = models.CharField(max_length=AUTHOR_LENGTH, blank=True)
