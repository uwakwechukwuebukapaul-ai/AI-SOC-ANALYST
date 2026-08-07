"""
Runtime Metrics Tests
"""


from services.intelligence.runtime.runtime_metrics import (
    RuntimeMetrics,
)



def test_default_metrics():

    metrics = RuntimeMetrics()

    assert metrics.total_executions == 0

    assert metrics.success_rate == 0



def test_record_success():

    metrics = RuntimeMetrics()

    metrics.record_success(
        2.0
    )


    assert metrics.total_executions == 1

    assert metrics.successful_executions == 1



def test_record_failure():

    metrics = RuntimeMetrics()

    metrics.record_failure(
        1.0
    )


    assert metrics.failed_executions == 1

    assert metrics.total_executions == 1



def test_success_rate():

    metrics = RuntimeMetrics()


    metrics.record_success()

    metrics.record_success()

    metrics.record_failure()



    assert metrics.success_rate == 66.66666666666666



def test_failure_rate():

    metrics = RuntimeMetrics()


    metrics.record_success()

    metrics.record_failure()



    assert metrics.failure_rate == 50



def test_average_execution_time():

    metrics = RuntimeMetrics()


    metrics.record_success(2)

    metrics.record_success(4)


    assert metrics.average_execution_time == 3



def test_to_dict():

    metrics = RuntimeMetrics()


    data = metrics.to_dict()


    assert "total_executions" in data

    assert "success_rate" in data