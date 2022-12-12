from .utils import get_link_book_data

from .models import Price, Link
from .api.serializers import LinkSerializer

from celery import shared_task

headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    }

@shared_task()
def update_book_data_price(link_pk):
    link = Link.objects.get(pk=link_pk)
    data = get_link_book_data(link.link)
    if data:
        price = Price(link=link, price=data.get('price'))
        price.save()
        return data

# its better scheduling bit tasks, but in this case that's enough
@shared_task()
def update_books():
    links = Link.objects.all()
    for link in links:
        update_book_data_price.delay(link.id)