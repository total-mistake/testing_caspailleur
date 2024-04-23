def parse_table_column_to_list(table, column_name):
    """
    Parse the content of the table to extract a specific column.

    Parameters:
        table (list of dict): The table containing the data.
        column_name (str): The name of the column to extract.

    Returns:
        list of lists: The values extracted from the specified column.
    """
    extracted_column = []
    for row in table:
        value = row[column_name]
        if value.strip():  # Check if the value is not empty
            if '{' in value and '}' in value:  # Check if the value contains curly braces
                value = set(map(int, filter(None, value.strip('{}').split(','))))
            else:
                try:
                    value = int(value)  # Convert to integer if it's a single element
                except ValueError:
                    value = []
        else:
            value = []  # Empty list if the value is empty string
        extracted_column.append(value)

    # Flatten the extracted_column if all elements are lists (representing sets)
    if all(isinstance(item, list) for item in extracted_column):
        extracted_column = [item for sublist in extracted_column for item in sublist]

    return extracted_column


def parse_table_column_to_list_of_sets(table, column_name):
    """
    Parse the content of the table to extract a specific column.

    Parameters:
        table (list of dict): The table containing the data.
        column_name (str): The name of the column to extract.

    Returns:
        list of sets: The values extracted from the specified column.
    """
    extracted_column = []
    for row in table:
        true_rows = row[column_name].strip('{}')
        if true_rows:
            powerset = {int(item) for item in true_rows.split(',')}
        else:
            powerset = set()
        extracted_column.append(powerset)
    return extracted_column

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
