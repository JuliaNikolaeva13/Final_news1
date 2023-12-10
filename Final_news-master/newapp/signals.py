from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from .models import Post


@receiver(post_save, sender=Post)
def post_created(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'New article in category {instance.category}'

    text_content = (
        f'Title: {instance.title}\n'
        f'Author: {instance.author}\n\n'
        f'Link to the news: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Title: {instance.title}<br>'
        f'Author: {instance.author}<br><br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Link to the news</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
