"""
Runtime Engine Tests
"""


from services.intelligence.runtime.runtime_engine import (
    RuntimeEngine,
)

from services.intelligence.runtime.task import (
    Task,
)



def create_task():

    return Task(
        capability="test",
        payload={}
    )



def test_engine_init():

    engine = RuntimeEngine()

    assert engine.queue.size() == 0



def test_submit():

    engine = RuntimeEngine()

    task = create_task()


    engine.submit(task)


    assert engine.scheduler.size() == 1



def test_next_task():

    engine = RuntimeEngine()


    task = create_task()


    engine.submit(task)


    result = engine.next_task()


    assert result == task



def test_memory():

    engine = RuntimeEngine()


    engine.set_memory(
        "case",
        "INC001",
    )


    assert engine.get_memory(
        "case"
    ) == "INC001"



def test_status():

    engine = RuntimeEngine()


    data = engine.status()


    assert "metrics" in data

    assert "memory" in data



def test_execute_success():

    engine = RuntimeEngine()


    task = create_task()


    def handler(task, context):

        return {
            "result": "ok"
        }



    result = engine.execute(
        task,
        handler,
    )


    assert result.success is True



def test_execute_failure():

    engine = RuntimeEngine()


    task = create_task()


    def handler(task, context):

        raise Exception(
            "failed"
        )


    result = engine.execute(
        task,
        handler,
    )


    assert result.success is False