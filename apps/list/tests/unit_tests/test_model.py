
import django
django.setup()
from apps.list.models import Item

#Need to be refactored in order to  be less verbos 
def test_saving_and_retrieving_items():
    first_item = Item()
    first_item.text = 'First Item'
    first_item.save()

    second_item = Item()
    second_item.text = 'Second Item'
    second_item.save()

    saved_items = Item.objects.all()
    
    result = saved_items.count()
    exp = 2

    assert result == exp
    
    first_item.delete()
    second_item.delete()