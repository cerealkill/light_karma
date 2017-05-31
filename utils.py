# -*- coding: utf-8 -*-
import re
from itertools import cycle


MANTRA = cycle(["om vajrasattva samaya", "manupalaya", "vajrasattva denopa titha", "dido me bhava",
                "suto kayo me bhava", "supo kayo me bhava", "anurakto me bhava", "sarva siddhi me prayatsa",
                "sarva karma su tsame", "tsittam shriyam kuru hum", "ha ha ha ha ho", "bhagavan", "sarva tathagata",
                "vajra mame muntsa", "vajra bhava maha samaya sattva ah hum phet"])


def find_text(text, reg):
    """
    Regex finder of first occurrence
    :param text: text to find the match
    :param reg: regex
    :return:
    """
    finder = re.compile(reg, re.MULTILINE)
    return finder.findall(text)[0]


def process_tabular_data(headers_text, lines_list, wanted_list, replacement, cls=None):
    """
    Bring it on and then just Class(*this) to profit!
    :param headers_text: ["D", "C", "B"]
    :param lines_list: [["VD", "VC", "VB"], ...]
    :param wanted_list: ["A", "B", "C", "D"]
    :param replacement: None or ''
    :param cls: If a class is to be instanced with result
    :return: [[None, "VB", "VC", "VD"], ...]
    """
    columns = process_columns(headers_text, wanted_list)
    table = [[line[columns[w]] if w in columns.keys() else replacement for w in wanted_list] for line in lines_list]

    return [cls(*line) for line in table] if cls else table


def process_columns(headers_text, wanted_list):
    """
    Find desired sublists in a huge list
    :param headers_text: str
    :param wanted_list: list
    :return: dict
    """
    columns = {word: headers_text.index(word) for word in wanted_list if word in headers_text}
    if len(columns) < 1:
        raise ValueError
    return columns