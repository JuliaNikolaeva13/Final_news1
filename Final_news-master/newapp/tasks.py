
from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from .models import Post



@shared_task
def weekly_msg():
    emails = User.objects.all().values_list('email', flat=True)

    subject = f'Последние новости'

    news = Post.objects.all()
    for i in news:
        text_content = (
            f'Новость: {i.title}\n'
            f'Цена: {i.text}\n\n'
            f'Ссылка на Новость: http://127.0.0.1:8000{i.get_absolute_url()}'
        )
        html_content = (
            f'Новость: {i.title}<br>'
            f'Цена: {ImportError.text}<br><br>'
            f'<a href="http://127.0.0.1{i.get_absolute_url()}">'
            f'Ссылка на Новость</a>'
        )

        for email in emails:
            msg = EmailMultiAlternatives(subject, text_content, None, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

@shared_task
def post_created():
    instance = Post.objects.get(id=id)

    subscribers_emails = []

    for category in instance.postCategory.all():
        subscribers_emails += User.objects.filter(subscriptions__category=category).values_list('email', flat=True)

    subject = f'Новый пост в категории {instance.postCategory}'

    text_content = (
        f'Статья: {instance.title}\n'
        f'Текст: {instance.text}\n\n'
        f'Ссылка на пост: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )

    html_content = (
        f'Товар: {instance.title}<br>'
        f'Цена: {instance.text}<br><br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на пост</a>'
    )

    for email in subscribers_emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


