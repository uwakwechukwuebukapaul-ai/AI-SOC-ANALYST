from services.intelligence.runtime.runtime_hooks import (
    RuntimeHook,
    RuntimeHookManager,
)



def test_hook_manager_init():

    manager = RuntimeHookManager()

    assert len(manager.hooks) == 0



def test_register_hook():

    manager = RuntimeHookManager()


    hook = RuntimeHook(
        name="analysis",
        callback=lambda: "done"
    )


    manager.register(hook)


    assert "analysis" in manager.hooks



def test_execute_hook():

    manager = RuntimeHookManager()


    hook = RuntimeHook(
        name="test",
        callback=lambda: "success"
    )


    manager.register(hook)


    result = manager.execute(
        "test"
    )


    assert result == "success"



def test_disable_hook():

    manager = RuntimeHookManager()


    hook = RuntimeHook(
        name="test",
        callback=lambda: "success"
    )


    manager.register(hook)


    manager.disable(
        "test"
    )


    result = manager.execute(
        "test"
    )


    assert result is None



def test_to_dict():

    manager = RuntimeHookManager()


    data = manager.to_dict()


    assert "hooks" in data