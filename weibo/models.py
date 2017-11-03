from django.db import models
from django.contrib.auth.admin import User
import json
# Create your models here.


class WBUser(User):
    """
    继承 django 默认 User 类，扩充字段及方法
    """
    GENDER_OPTIONS = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
        (3, '其他')
    )
    nickname = models.CharField(verbose_name='昵称', max_length=60, unique=True, null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_OPTIONS, default=0)
    _info = models.TextField(verbose_name='其他信息', blank=True, null=True)
    followers = models.ManyToManyField('WBUser')

    @property
    def name(self):
        """
        返回用户名字，优先显示昵称
        """
        return self.nickname or self.username

    @property
    def info(self):
        """
        读取字段 _info，将 json 格式字符串转换为字典
        """
        return json.loads(self._info)

    def save_user_info(self, info: dict):
        """
        保存字段 _info，将字典转换为 json 格式的字符串
        """
        self._info = json.dumps(info)
        self.save()

    def follow(self, user: 'WBUser'):
        """
        关注
        """
        self.followers.add(user)
        self.save()

    def forward(self, weibo: 'WeiBo'):
        """
        转发微博
        """
        return WeiBo.objects.create(user=self, weibo_text=weibo.weibo_text)

    def __str__(self):
        return self.name


class WBText(models.Model):
    """
    文字微博
    """
    author = models.ForeignKey(WBUser, verbose_name='作者', related_name='ori_wbs')
    msg = models.TextField(verbose_name='微博', max_length=500)

    def __str__(self):
        return '{msg}...'.format(msg=self.msg[:20])


class WeiBo(models.Model):
    """
    微博信息
    """
    user = models.ForeignKey(WBUser, verbose_name='用户', related_name='wbs')
    time_create = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_del = models.BooleanField(verbose_name='是否删除', default=False)
    text = models.ForeignKey(WBText, verbose_name='文本', related_name='wbs')

    def del_this(self):
        self.is_del = True
        self.save()

    def __str__(self):
        return self.text


class Comment(models.Model):
    """
    评论
    """
    target = models.ForeignKey(WBText, verbose_name='被评信息', related_name='comments')
    user = models.ForeignKey(WBUser, verbose_name='用户', related_name='comments')
    text = models.OneToOneField(WBText, verbose_name='评论')
    time_create = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_del = models.BooleanField(verbose_name='是否删除', default=False)

    def del_this(self):
        self.is_del = True
        self.save()
