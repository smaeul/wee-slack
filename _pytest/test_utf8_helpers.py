# -*- coding: utf-8 -*-

from collections import OrderedDict
from wee_slack import decode_from_utf8, encode_to_utf8, utf8_decode


def test_decode_preserves_string_without_utf8():
    assert u'test' == decode_from_utf8(b'test')

def test_decode_preserves_unicode_strings():
    assert u'æøå' == decode_from_utf8(u'æøå')

def test_decode_preserves_mapping_type():
    value_dict = {'a': 'x', 'b': 'y', 'c': 'z'}
    value_ord_dict = OrderedDict(value_dict)
    assert type(value_dict) == type(decode_from_utf8(value_dict))
    assert type(value_ord_dict) == type(decode_from_utf8(value_ord_dict))

def test_decode_preserves_iterable_type():
    value_set = {'a', 'b', 'c'}
    value_tuple = ('a', 'b', 'c')
    assert type(value_set) == type(decode_from_utf8(value_set))
    assert type(value_tuple) == type(decode_from_utf8(value_tuple))

def test_decodes_utf8_string_to_unicode():
    assert u'æøå' == decode_from_utf8(u'æøå'.encode())

def test_decodes_utf8_dict_to_unicode():
    unicode_dict = {u'æ': u'å', u'ø': u'å'}
    utf8_dict = {k.encode(): v.encode() for k, v in unicode_dict.items()}
    assert unicode_dict == decode_from_utf8(utf8_dict)

def test_decodes_utf8_list_to_unicode():
    unicode_list = [u'æ', u'ø', u'å']
    utf8_list = [s.encode() for s in unicode_list]
    assert unicode_list == decode_from_utf8(utf8_list)

def test_encode_preserves_string_without_utf8():
    assert b'test' == encode_to_utf8(u'test')

def test_encode_preserves_byte_strings():
    byte_string = u'æøå'.encode()
    assert byte_string == encode_to_utf8(byte_string)

def test_encode_preserves_mapping_type():
    value_dict = {'a': 'x', 'b': 'y', 'c': 'z'}
    value_ord_dict = OrderedDict(value_dict)
    assert type(value_dict) == type(encode_to_utf8(value_dict))
    assert type(value_ord_dict) == type(encode_to_utf8(value_ord_dict))

def test_encode_preserves_iterable_type():
    value_set = {'a', 'b', 'c'}
    value_tuple = ('a', 'b', 'c')
    assert type(value_set) == type(encode_to_utf8(value_set))
    assert type(value_tuple) == type(encode_to_utf8(value_tuple))

def test_encodes_utf8_string_to_unicode():
    assert u'æøå'.encode() == encode_to_utf8(u'æøå')

def test_encodes_utf8_dict_to_unicode():
    unicode_dict = {u'æ': u'å', u'ø': u'å'}
    utf8_dict = {k.encode(): v.encode() for k, v in unicode_dict.items()}
    assert utf8_dict == encode_to_utf8(unicode_dict)

def test_encodes_utf8_list_to_unicode():
    unicode_list = [u'æ', u'ø', u'å']
    utf8_list = [s.encode() for s in unicode_list]
    assert utf8_list == encode_to_utf8(unicode_list)

@utf8_decode
def method_with_utf8_decode(*args, **kwargs):
    return (list(args), kwargs)

def test_utf8_decode():
    args = [s.encode() for s in (u'æ', u'ø', u'å')]
    # In Python 3, kwargs keys must be unicode.
    kwargs = {k: v.encode() for k, v in {u'a': u'å', u'b': u'å'}.items()}

    result_args, result_kwargs = method_with_utf8_decode(*args, **kwargs)

    assert result_args == decode_from_utf8(args)
    assert result_kwargs == decode_from_utf8(kwargs)
