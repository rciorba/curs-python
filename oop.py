# coding=utf-8

import json
import os
import os.path


class Persoană:
    # Responsabilitatea de stocare și logica de busyness sunt în aceeași clasă
    # Vedem vre-o problemă?

    # logică de stocare
    @classmethod
    def încarcă_toate(cls, path):
        persoane = []
        for f_name in os.listdir(path):
            persoane.append(cls(os.path.join(path, f_name)))
        return persoane

    def __init__(self, path):
        with open(path) as file_desc:
            data = json.load(file_desc)
            self.nume = data['nume']
            self.venit_anual = data['venit']
            self.identificator = data['identificator']

    # logică de busyness
    @property
    def impozit(self):
        raise NotImplementedError()


class PersoanăFizică(Persoană):
    @property
    def impozit(self):
        return self.venit_anual * 1.16


class PersoanăJuridică(Persoană):
    @property
    def impozit(self):
        return self.venit_anual * 1.22

class Spam(Persoană):
    pass
