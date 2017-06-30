# -*- coding: utf-8 -*-
#引用模块
def search4prepositions_zhs(phrase: str) -> set:#定义函数
    """Return any prepositions found in a supplied phrase."""
    # Source 
    # Source 
    PREPOSITION_zhs = set('')
    return PREPOSITION_zhs.intersection(set(phrase))

def search4letters(phrase: str, letters: str='') -> set:#定义函数
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
