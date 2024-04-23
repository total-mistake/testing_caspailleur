from fcapy.context import FormalContext
from fcapy.lattice import ConceptLattice
import matplotlib.pyplot as plt
from fcapy.visualizer import LineVizNx
import re

# Загрузка данных
import pandas as pd
# Исследование данных
import caspailleur as csp

# Пример простого набора данных от автора
df = pd.read_csv('https://raw.githubusercontent.com/total-mistake/testing_caspailleur/main/test_data_tables/pizza.csv',
                 index_col=0)

# Другой набор данных от автора мат.пакета
# df = pd.read_csv('https://raw.githubusercontent.com/EgorDudyrev/FCApy/main/data/animal_movement.csv',index_col=0)


# Вывод примера
# print(df.to_markdown().replace('1', 'X').replace('0', ' '))

# Формальный контекст
data_dict = csp.explore_data(df.values)
K = FormalContext.from_pandas(df)
print("\nБулева таблица:")
print(K)

# Решетка понятий
L = ConceptLattice.from_context(K)
fig, ax = plt.subplots(figsize=(10, 5))
vsl = LineVizNx()
vsl.draw_concept_lattice(L, ax=ax, flg_node_indices=True)
ax.set_title('"Pizza" concept lattice', fontsize=18)
plt.tight_layout()
plt.show()

# print(data_dict.keys())

# Оптимизация вывода
to_print = '\n'.join([f"{k}: {v}" for k, v in data_dict.items()])
to_print = to_print.replace('frozenset()', 'set()')
for _ in re.findall(r"frozenset\(.+?\)", to_print):
    to_print = re.sub(r"frozenset\((.+?)\)", r"\g<1>", to_print)

print("\n" + "Визуализация результата:" + "\n" + to_print)


def verbose(indices, names, empty_symbol='∅'):
    """Функция для сопоставления индексов столбцов с именами столбцов.

    Parameters:
    indices: list
        Индексы столбцов.
    names: list
        Имена столбцов.
    empty_symbol: str, optional
        Символ, используемый для пустого множества.

    Returns:
    str
        Строка, представляющая имена столбцов.
    """
    return ', '.join([names[i] for i in sorted(indices)]) if indices else empty_symbol


def unpack_gens_dict(gens_dict, intents, show_difference: bool = True):
    """Функция для распаковки словаря намерений.

    Parameters:
    gens_dict: dict
        Словарь с намерениями и их индексами.
    intents: list
        Список намерений.
    show_difference: bool, optional
        Флаг, указывающий на необходимость показать разницу между намерениями и их индексами.

    Returns:
    dict
        Распакованный словарь намерений.
    """
    dct = {k: intents[intent_i] for k, intent_i in gens_dict.items()}
    if show_difference:
        return {k: v - k for k, v in dct.items()}
    return dct


# Вывод объема
print('\nОбъем:')
print('\n'.join([verbose(intent, df.columns) for intent in data_dict['intents']]))


def construct_mermaid_diagram(ordering, intents):
    # Создаем строку, содержащую буквы для имен узлов диаграммы
    node_names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Определяем узлы диаграммы, связываемые с соответствующими намерениями (intents)
    # Каждый узел представляет собой набор атрибутов, заданных в намерении
    # Подробнее см. функцию verbose
    defining_nodes = '\n'.join([
        f'{node_name}[{verbose(intent, df.columns, empty_symbol="fa:fa-empty-set")}];'
        for node_name, intent in zip(node_names, intents)]
    )

    # Определяем связи между узлами диаграммы
    # Каждый ребенок связан с каждым родителем в соответствии с ordering
    defining_edges = '\n'.join([
        f'{node_names[parent_i]} --> {node_names[intent_i]};'
        for intent_i, parents in enumerate(ordering) for parent_i in parents]
    )

    # Собираем строку, представляющую графическую диаграмму с использованием языка Mermaid
    diagram = f"graph TD; " + defining_nodes + defining_edges
    return diagram


print("\nMermaid код:\n" + construct_mermaid_diagram(data_dict['intents_ordering'], data_dict['intents']))
# Чтобы получить визуализацию диаграммы необходимо ввести полученный код по ссылке: https://mermaid.live/

# Разница ключей и объема
print("\nДемонстрация разницы между ключами и объемом (слева ключи, справа объем):")
print('\n'.join([
    verbose(k, df.columns) + ' ~ ' + verbose(v, df.columns)
    for k, v in unpack_gens_dict(data_dict['keys'], data_dict['intents'], show_difference=False).items()
    if k != v
]))

# Proper premises
print('\n\nProper premises\n'.join([
    verbose(k, df.columns)+' -> '+verbose(v, df.columns)
    for k, v in unpack_gens_dict(data_dict['proper_premises'], data_dict['intents'], show_difference=True).items()
]))

# Pseudo-intents
print('\n\nPseudo-intents\n'.join([
    verbose(k, df.columns)+' -> '+verbose(v, df.columns)
    for k, v in unpack_gens_dict(data_dict['pseudo_intents'], data_dict['intents'], show_difference=True).items()
]))


# Индексы сложности (линейность и дистрибуивность)
print("\nИндексы сложности:")
for k in ['linearity', 'distributivity']:
    print(k, data_dict[k])

