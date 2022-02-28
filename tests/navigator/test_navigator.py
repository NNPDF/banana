# -*- coding: utf-8 -*-
import pytest

from banana import navigator
from banana.navigator import table_manager as tm


class FakeNavApp(navigator.navigator.NavigatorApp):
    def __init__(self, session, cfgpath, external=None, extra_tables=None):
        super().__init__(cfgpath, external)

        self.session = session

        if extra_tables is None:
            extra_tables = {}
        self.input_tables = {**self.input_tables, **extra_tables}

    def fill_ciao(self, theo, obj):
        obj["name"] = theo["name"]

    def is_valid_physical_object(_name):
        return True


class TestNavigatorApp:
    def test_change_external(self, banana_yaml, dbsession):
        app = FakeNavApp(dbsession, banana_yaml, "test")

        assert app.external == "test"

        app.change_external("comeva")
        assert app.external == "comeva"

    def test_get_all(self, banana_yaml, dbsession, tab_ciao):
        tabman = tm.TableManager(dbsession, tab_ciao)
        app = FakeNavApp(dbsession, banana_yaml, "test", extra_tables=dict(ciao=tabman))

        recs = app.get_all("ciao")
        assert len(recs) == 0

        with dbsession.begin():
            newrec = tab_ciao(uid=42, name="leorio", hash="abcdef123456789")
            dbsession.add(newrec)
        recs = app.get_all("ciao")
        assert len(recs) == 1
        assert isinstance(recs[0], dict)

    def test_list_all(self, banana_yaml, dbsession, tab_ciao):
        tabman = tm.TableManager(dbsession, tab_ciao)
        app = FakeNavApp(dbsession, banana_yaml, "test", extra_tables=dict(ciao=tabman))

        df = app.list_all("ciao")
        assert len(df) == 0

        with dbsession.begin():
            newrec = tab_ciao(uid=42, name="leorio", hash="abcdef123456789")
            dbsession.add(newrec)
        df = app.list_all("ciao")
        assert len(df) == 1

    def test_table_name(self, banana_yaml, dbsession, tab_ciao):
        tabman = tm.TableManager(dbsession, tab_ciao)
        app = FakeNavApp(dbsession, banana_yaml, "test", extra_tables=dict(ciao=tabman))

        assert app.table_name("l") == "logs"
        assert app.table_name("c") == "ciao"

        with pytest.raises(ValueError):
            app.list_all("b")
