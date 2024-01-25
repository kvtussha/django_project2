from django.core.mail import send_mail
from django.conf import settings
from main_app.models import MailingMessage, MailingLog
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Send notifications'

    def handle(self, *args, **options):
        notifications = MailingMessage.objects.filter(sent=False)

        for notification in notifications:
            # Отправка уведомления на почту
            send_mail(
                notification.subject,
                notification.body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=settings.DEFAULT_FROM_EMAIL,
            )

            # Добавление в общий журнал уведомлений
            MailingLog.objects.create(mailing=notification, attempt_datetime=timezone.now(),
                                      attempt_status='Sent', server_response=settings.SERVER_RESPONSE)

            # Устанавливаем флаг "отправлено" в модели MailingMessage
            notification.sent = True
            notification.sent_at = timezone.now()
            notification.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully sent notification: {notification.subject}'))
