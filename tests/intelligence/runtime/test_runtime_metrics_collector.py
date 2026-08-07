"""
Runtime Metrics Collector Tests
"""

from services.intelligence.runtime.runtime_metrics_collector import (
    RuntimeMetricsCollector,
)



def test_init():

    metrics = RuntimeMetricsCollector()

    assert (
        metrics.executions
        ==
        0
    )



def test_record_execution():

    metrics = RuntimeMetricsCollector()


    metrics.record_execution(
        "ioc_analysis"
    )


    assert (
        metrics.executions
        ==
        1
    )



def test_record_failure():

    metrics = RuntimeMetricsCollector()


    metrics.record_failure(
        "analysis",
        "timeout",
    )


    assert (
        metrics.failures
        ==
        1
    )



def test_events():

    metrics = RuntimeMetricsCollector()


    metrics.record_execution(
        "investigation"
    )


    assert (
        metrics.total_events()
        ==
        1
    )



def test_clear():

    metrics = RuntimeMetricsCollector()


    metrics.record_execution(
        "test"
    )


    metrics.clear()


    assert (
        metrics.executions
        ==
        0
    )



def test_status():

    metrics = RuntimeMetricsCollector()


    result = metrics.status()


    assert "executions" in result

    assert "failures" in result

    assert "events" in result