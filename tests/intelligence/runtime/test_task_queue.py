from services.intelligence.runtime.task import Task
from services.intelligence.runtime.task_queue import TaskQueue


def make_task(capability: str = "ioc_enrichment") -> Task:
    return Task(
        capability=capability,
        payload={},
    )


def test_enqueue():

    queue = TaskQueue()

    queue.enqueue(make_task())

    assert queue.size() == 1


def test_dequeue():

    queue = TaskQueue()

    task = make_task()

    queue.enqueue(task)

    result = queue.dequeue()

    assert result == task
    assert queue.empty()


def test_peek():

    queue = TaskQueue()

    task = make_task()

    queue.enqueue(task)

    assert queue.peek() == task
    assert queue.size() == 1


def test_clear():

    queue = TaskQueue()

    queue.enqueue(make_task("ioc"))
    queue.enqueue(make_task("mitre"))

    queue.clear()

    assert queue.empty()


def test_tasks():

    queue = TaskQueue()

    queue.enqueue(make_task("ioc"))
    queue.enqueue(make_task("reasoning"))

    tasks = queue.tasks()

    assert len(tasks) == 2