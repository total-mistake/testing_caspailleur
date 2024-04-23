from behave import *
from parsing_functions import *
from caspailleur import order, base_functions as bfunc


@given(u'I have a sorted list of elements')
def given_sorted_list(context):
    context.elements = parse_table_column_to_list(context.table, 'elements')
    context.elements = [frozenset(ar) for ar in context.elements]


@when(u'I perform a topological sort of a list using an order pattern')
def when_topological_sort(context):
    context.idxs_unordered = parse_table_column_to_list(context.table, 'map')
    context.elements_ba = list(bfunc.isets2bas(context.elements, len(context.elements)))
    context.elements_unordered = [context.elements_ba[i] for i in context.idxs_unordered]


@then(u'I should get the sorted elements and their indices mapping')
def get_sorted_elements(context):
    print(order.topological_sorting(context.elements_unordered))
    assert order.topological_sorting(context.elements_unordered) == (context.elements_ba,
                                                                     context.idxs_unordered)
    assert order.topological_sorting(context.elements_ba) == (context.elements_ba,
                                                              list(range(len(context.elements_ba))))
