import datetime

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from stockapp.models import Notification, Stock
from webapp.sql.db_sql import Sql


def emailing():
    """Send email if notification date is reached"""
    # Get all non-send notifications
    notifications = Notification.objects.filter(notification_is_send=0)
    # For each notification
    for notification in notifications:
        # Get the notification stock
        stock = Stock.objects.get(stock_notification=notification)
        # If notification date in now
        if stock.stock_notification.notification_date == (
            datetime.datetime.now().date()
        ):
            # Get the stock user
            user = (
                stock.stock_compartment.compartment_colddevice.colddevice_user
            )
            # Get the product name
            product = stock.stock_product.product_name

            # Create the mail
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

            # Send the mail
            mail.send_mail(
                subject,
                plain_message,
                from_email,
                [to],
                html_message=html_message
            )
            # Set notification_is_send to 1
            Sql.notification_is_send(notification)
