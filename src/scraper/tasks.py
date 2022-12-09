from .utils import get_link_book_data

from .models import Price, Link

from celery import shared_task

@shared_task()
def update_data_price(link_id):
    link = Link.objects.get(id=link_id)
    data = get_link_book_data(link.link)
    if data:
        Price.objects.create(link=link, price=data.get('price'))
        return "Updated"
    return "Failed"