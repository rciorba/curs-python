# coding=utf-8

from tempfile import NamedTemporaryFile, TemporaryDirectory
import json
import os

from oop import Persoană, PersoanăFizică, PersoanăJuridică


def test_impozit_persoană_fizică():
    with NamedTemporaryFile() as t_file:
        encoded = json.dumps({
            'nume': "Ana Banana",
            'venit': 1000,
            'identificator': '2860101110123'
        })
        t_file.file.write(bytes(encoded, 'utf-8'))
        t_file.file.flush()
        pers = PersoanăFizică(t_file.name)
    assert pers.impozit == 1160


def test_impozit_persoană_juridică():
    with NamedTemporaryFile() as t_file:
        encoded = json.dumps({
            'nume': "S.C 3 Bananas Global S.R.L.",
            'venit': 10000,
            'identificator': 'CUI:123456'
        })
        t_file.file.write(bytes(encoded, 'utf-8'))
        t_file.file.flush()
        pers = PersoanăJuridică(t_file.name)
    assert pers.impozit == 12200


def test_încarcă_toate():
    with TemporaryDirectory() as temp_dir:
        persoane = [
            {
                'nume': "Ana Banana",
                'venit': 1000,
                'identificator': '2860101110123'
            },
            {
                'nume': "Popescu Ion",
                'venit': 990,
                'identificator': '1860101110123'
            },
        ]
        for persoană in persoane:
            file_path = os.path.join(temp_dir, persoană['identificator'])
            with open(file_path, 'w') as f_desc:
                json.dump(persoană, f_desc)
        pers = Persoană.încarcă_toate(temp_dir)
        assert pers[0].nume == 'Ana Banana'
        assert pers[1].nume == 'Popescu Ion'
        assert len(pers) == 2
