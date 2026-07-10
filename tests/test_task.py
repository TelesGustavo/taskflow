from src.storage import (
    add_task,
    get_tasks,
    delete_task,
    tasks
)


def setup_function():

    tasks.clear()


def test_add_task():

    add_task(
        "Estudar",
        "Engenharia de Software",
        "Alta"
    )

    assert len(get_tasks()) == 1

    assert get_tasks()[0].title == "Estudar"


def test_delete_task():

    add_task(
        "Comprar café",
        "Mercado",
        "Baixa"
    )

    task_id = get_tasks()[0].id

    delete_task(task_id)

    assert len(get_tasks()) == 0