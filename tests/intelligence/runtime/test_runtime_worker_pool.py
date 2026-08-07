"""
Runtime Worker Pool Tests
"""

from services.intelligence.runtime.runtime_worker_pool import (
    RuntimeWorkerPool,
)

from services.intelligence.runtime.task import (
    Task,
)



def create_task():

    return Task(
        capability="analysis",
        payload={
            "test":
                True
        },
    )



def test_init():

    pool = RuntimeWorkerPool()

    assert (
        pool.workers
        ==
        0
    )



def test_start_workers():

    pool = RuntimeWorkerPool()


    pool.start_workers(
        3
    )


    assert (
        pool.active_workers()
        ==
        3
    )



def test_submit():

    pool = RuntimeWorkerPool()


    pool.start_workers(
        1
    )


    pool.executor.register(
        "analysis",
        lambda data: {
            "ok":
                True
        },
    )


    result = pool.submit(
        create_task()
    )


    assert (
        result["ok"]
        is True
    )



def test_completed_count():

    pool = RuntimeWorkerPool()


    pool.start_workers(
        1
    )


    pool.executor.register(
        "analysis",
        lambda data: True,
    )


    pool.submit(
        create_task()
    )


    assert (
        pool.completed
        ==
        1
    )



def test_stop():

    pool = RuntimeWorkerPool()


    pool.start_workers(
        2
    )


    pool.stop_workers()


    assert (
        pool.workers
        ==
        0
    )



def test_status():

    pool = RuntimeWorkerPool()


    result = pool.status()


    assert "workers" in result

    assert "completed" in result

    assert "executor" in result