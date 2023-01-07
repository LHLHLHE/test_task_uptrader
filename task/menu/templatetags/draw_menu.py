from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        items = MenuItem.objects.filter(menu__name=menu_name)
        root_items = [item for item in items.filter(parent=None).values()]
        selected_item_id = int(context['request'].GET.get(menu_name))
        selected_item_ids = get_selected_item_ids(
            items.get(id=selected_item_id),
            root_items,
            selected_item_id
        )

        for root_item in root_items:
            if root_item.get('id') in selected_item_ids:
                root_item['child_items'] = [
                    item for item in
                    items.filter(parent_id=root_item.get('id')).values()
                ]
        result = {'items': root_items}

    except Exception:
        result = {
            'items': [
                item for item in MenuItem.objects.filter(
                    menu__name=menu_name,
                    parent=None
                ).values()
            ]
        }

    finally:
        result['menu'] = menu_name

    return result


def get_selected_item_ids(parent, root_items, selected_item_id):
    selected_item_ids = []

    while parent:
        selected_item_ids.append(parent.id)
        parent = parent.parent
    if not selected_item_ids:
        for root_item in root_items:
            if root_item['id'] == selected_item_id:
                selected_item_ids.append(selected_item_id)
    return selected_item_ids
