import datetime

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from stockapp.models import Notification, Stock
from webapp.sql.db_sql import Sql


def emailing():
    notifications = Notification.objects.filter(notification_is_send=0)
    for notification in notifications:
        stock = Stock.objects.get(stock_notification=notification)
        if stock.stock_notification.notification_date == datetime.datetime.now().date():
            user = stock.stock_compartment.compartment_colddevice.colddevice_user
            product = stock.stock_product.product_name

            subject = "MyColdManager - Rappel"
            html_message = render_to_string(
                "webapp/mail.html",
                {
                    "user": user,
                    "product": product,
                }
            )
            plain_message = strip_tags(html_message)
            from_email = 'From <mycoldmanager@gmail.com>'
            to = user.email

            mail.send_mail(
                subject,
                plain_message,
                from_email,
                [to],
                html_message=html_message
            )
            Sql.notification_is_send(notification)
