from behave import *
from parsing_functions import *
from caspailleur import base_functions as bfunc


@given("I have an iterable with elements")
def step_given_iterable(context):
    context.elements = tuple(int(row['elements']) for row in context.table)


@when("I calculate the powerset")
def step_when_calculate_powerset(context):
    context.result = bfunc.powerset(context.elements)


@then("I should get the expected powerset")
def step_then_expected_powerset(context):
    expected_powerset = parse_table_column_to_list(context.table, 'powerset')
    assert list(context.result) == expected_powerset


@given(u'the following true rows per column')
def given_true_rows(context):
    context.crosses_per_columns = parse_table_column_to_list_of_sets(context.table, 'True Rows')


@when(u'I calculate the closure for description')
def when_calculate_closure(context):
    context.description = parse_table_column_to_list(context.table, 'description')


@then(u'I should get the expected closure')
def then_get_closure(context):
    closure_true = parse_table_column_to_list(context.table, 'closure')
    assert list(bfunc.closure(context.description, context.crosses_per_columns)) == closure_true


@given(u'the set')
def given_set(context):
    set_str = context.table[0]['set'].strip('{}')
    if set_str:
        context.set = frozenset(map(int, set_str.split(',')))
    else:
        context.set = frozenset()


@when(u'I check if it\'s a subset of')
def when_check_subset(context):
    set_str = context.table[0]['set'].strip('{}')
    if set_str:
        set2 = frozenset(map(int, set_str.split(',')))
    else:
        set2 = frozenset()
    context.answer = bfunc.is_subset_of(context.set, set2)


@when(u'I check if it\'s a psubset of')
def when_check_psubset(context):
    set_str = context.table[0]['set'].strip('{}')
    if set_str:
        set2 = frozenset(map(int, set_str.split(',')))
    else:
        set2 = frozenset()
    context.answer = bfunc.is_psubset_of(context.set, set2)
    print(context.answer)


@then('I want the answer "{outcome}"')
def then_get_answer(context, outcome):
    if outcome.strip().lower() == "true":
        answer = True
    elif outcome.strip().lower() == "false":
        answer = False
    else:
        assert False, "The expected result is not written in a Boolean type"

    assert answer == context.answer

