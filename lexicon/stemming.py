# -*- coding: utf-8 -*-

import os
import re
import ctypes
import threading
from itertools import chain

stripper = re.compile(r'[^\w\-:]', re.U)

def string_to_words(s):
    s = s.lower()
    s = stripper.sub(u' ', s)
    words = s.split()
    return words

class Stemmer(object):
    FI_PROJECT = 'sukija/suomi.pro'
    FI_TRANSFORMS = {
        u'kuu': ([u'kuu', u'kuin'], [u'kuin']),
        u'siitä': ([u'siitä', u'siittää', u'se'], [u'se']),
        u'myödä': ([u'myödä', u'myös'], [u'myös']),
        u'silta': ([u'silta', u'silla', u'silloin'], [u'silloin']),
        u'tähkä': ([u'tähkä', u'tämä'], [u'tämä']),
        u'paljo': ([u'paljo'], [u'paljon']),
    }

        # We support only Finnish for now
    def __init__(self, language):
        assert language == "fi"

        self.libc = ctypes.CDLL(None)
        self.lib = ctypes.CDLL('libmalaga.so.7')
        my_path = os.path.dirname(os.path.abspath(__file__))
        self.lib.init_libmalaga(os.path.join(my_path, self.FI_PROJECT))
        self.lock = threading.Lock()
        self.lib.first_analysis_result.restype = ctypes.c_long

    def __del__(self):
        self.lib.terminate_libmalaga()

    def convert_word(self, word, flat=False):
        if word[-1] == ':':
            word = word[0:-1]
        if not word:
            return list()
        if word[0] == '-':
            word = word[1:]

        self.lock.acquire()
        we = word.encode('utf-8')
        st = ctypes.c_char_p(we)
        self.lib.analyse_item(st, 0)
        result = self.lib.first_analysis_result()
        ret = []
        while result:
            if self.lib.get_value_type(result) != 4:
                raise Exception('Unknown libmalaga result type!')
            s = ctypes.c_char_p(self.lib.get_value_string(result))
            ret.append(unicode(s.value, 'utf-8'))
            self.libc.free(s)
            result = self.lib.next_analysis_result()
        self.lock.release()

	if flat:
            ret = list(set(ret))
            if len(ret) > 0:
                trans = self.FI_TRANSFORMS.get(ret[0])
                if trans and ret == trans[0]:
                    ret = trans[1]
        else:
            if len(ret) == 1:
                ret = ret[0]
        return ret

    def convert_string(self, s, flat=False):
        words = string_to_words(s)
        ret = map(lambda x: self.convert_word(x, flat), words)
        if flat:
            ret = list(chain.from_iterable(ret))
        """for idx, w in enumerate(ret):
            if len(w) == 0:
                print words[idx]"""
        return ret
