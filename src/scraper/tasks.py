from .utils import get_link_book_data

from .models import Price, Link

from celery import shared_task

# its better scheduling bit tasks, but in this case that's enough
@shared_task()
def update_book_data_price():
    links = Link.objects.all()
    for link in links:
        link = Link.objects.get(id=link.id)
        data = get_link_book_data(link.link)
        if data:
            Price.objects.create(link=link, price=data.get('price'))