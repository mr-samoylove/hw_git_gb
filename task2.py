# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

import typing


def make_values_as_keys(**kwargs) -> dict:
    for key, value in kwargs.items():
        if not isinstance(value, typing.Hashable):
            kwargs[key] = str(value)

    return {value: key for key, value in kwargs.items()}


result = make_values_as_keys(key1='str1', key2=2, key3=[1, 2, 3])
print(result)
