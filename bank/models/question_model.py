# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):

    update_user = models.CharField(max_length=45)
    create_user = models.CharField(max_length=45)
    update_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Questions(BaseModel):

    """
    recording the base information of question
    """

    status_map = (
        (0, "DELETE"),
        (10, "OFFLINE"),
        (20, "ONLINE")
     )

    question_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, unique=True)
    type = models.IntegerField(unique=True)
    status = models.IntegerField(choices=status_map)
    version = models.IntegerField()

    def __str__(self):
        return self.__name__

    class Meta:
        db_table = "question_bank"
        unique_together = ("title", "type")


class DetailInfo(BaseModel):

    """
    recording the detail information of question
    """

    detail_id = models.AutoField(primary_key=True)
    content = models.TextField()
    code = models.TextField()
    style = models.IntegerField()
    status = models.IntegerField()
    notes = models.TextField()

    def __str__(self):
        return self.__name__

    class Meta:
        db_table = "question_detail"


class QuestionDetailRel(models.Model):

    """
    maintain the relationship between question and detail
    """

    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='b_question_id')
    detail = models.ForeignKey(DetailInfo, on_delete=models.CASCADE, related_name='b_detail_id')
    status = models.IntegerField()

    def __str__(self):
        return self.__name__

    class Meta:
        db_table = "question_detail_rel"
