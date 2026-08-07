"""
Runtime Cache Manager Tests
"""

from services.intelligence.runtime.runtime_cache_manager import (
    RuntimeCacheManager,
)



def test_init():

    cache = RuntimeCacheManager()

    assert (
        cache.size()
        ==
        0
    )



def test_set_get():

    cache = RuntimeCacheManager()


    cache.set(
        "ioc_123",
        {
            "risk":
                "high"
        },
    )


    result = cache.get(
        "ioc_123"
    )


    assert (
        result["risk"]
        ==
        "high"
    )



def test_cache_hit():

    cache = RuntimeCacheManager()


    cache.set(
        "key",
        "value",
    )


    cache.get(
        "key"
    )


    assert (
        cache.hits
        ==
        1
    )



def test_cache_miss():

    cache = RuntimeCacheManager()


    cache.get(
        "missing"
    )


    assert (
        cache.misses
        ==
        1
    )



def test_remove():

    cache = RuntimeCacheManager()


    cache.set(
        "test",
        True,
    )


    cache.remove(
        "test"
    )


    assert (
        cache.exists(
            "test"
        )
        is False
    )



def test_clear():

    cache = RuntimeCacheManager()


    cache.set(
        "test",
        True,
    )


    cache.clear()


    assert (
        cache.size()
        ==
        0
    )



def test_status():

    cache = RuntimeCacheManager()


    result = cache.status()


    assert "size" in result

    assert "hits" in result

    assert "misses" in result