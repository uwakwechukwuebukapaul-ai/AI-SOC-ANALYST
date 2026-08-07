from services.intelligence.runtime.runtime_base import (
    RuntimeBase,
)


def test_init():

    runtime = RuntimeBase()

    assert runtime.count() == 0


def test_exists():

    runtime = RuntimeBase()

    runtime.items["a"] = {}

    assert runtime.exists("a")


def test_get():

    runtime = RuntimeBase()

    runtime.items["x"] = 123

    assert runtime.get("x") == 123


def test_remove():

    runtime = RuntimeBase()

    runtime.items["a"] = {}

    runtime.remove("a")

    assert runtime.count() == 0


def test_clear():

    runtime = RuntimeBase()

    runtime.items["a"] = {}

    runtime.items["b"] = {}

    runtime.clear()

    assert runtime.count() == 0


def test_status():

    runtime = RuntimeBase()

    runtime.items["one"] = {}

    result = runtime.status()

    assert result["count"] == 1