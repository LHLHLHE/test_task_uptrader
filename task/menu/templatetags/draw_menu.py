from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    items = MenuItem.objects.filter(menu__name=menu_name)
    root_items = [item for item in items.filter(parent=None).values()]
    selected_item_id = int(context['request'].GET.get(menu_name))

    for root_item in root_items:
        if root_item.get('id') == selected_item_id:
            root_item['child_items'] = [
                item for item in items.filter(parent_id=root_item).values()
            ]

    result_dict = {
        'items': root_items,
        'menu': menu_name,
        'other_querystring': get_querystring(context, menu_name)
    }
    return result_dict


def get_querystring(context, menu):
    querystring_args = []
    for key in context['request'].GET:
        if key != menu:
            querystring_args.append(key + '=' + context['request'].GET[key])
    querystring = ('&').join(querystring_args)
    return querystring
