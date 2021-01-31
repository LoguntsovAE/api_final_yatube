from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField('Заголовок группы', max_length=200)
    # author = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     default='',
    #     editable=False,
    #     related_name='user_groups')
    slug = models.SlugField(
        'Адрес',
        max_length=20,
        unique=True)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name='Группа',
        help_text='Необязательно',
        related_name='posts')
    # image = models.ImageField(
    #     'Картинка',
    #     upload_to='posts/',
    #     blank=True, null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['user', 'author'],
                name = 'unique_author_user_following',
            ),
        ]