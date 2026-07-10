from flask import Flask, render_template, request, redirect

from src.storage import (
    add_task,
    get_tasks,
    delete_task,
    toggle_task,
    update_task,
    get_task
)

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "index.html",
        tasks=get_tasks()
    )


@app.route("/add", methods=["POST"])
def add():

    title = request.form["title"]
    description = request.form["description"]
    priority = request.form["priority"]

    add_task(title, description, priority)

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):

    delete_task(id)

    return redirect("/")

from src.storage import update_task, get_task

@app.route("/toggle/<int:id>")
def toggle(id):

    toggle_task(id)

    return redirect("/")

@app.route("/edit/<int:id>")
def edit(id):

    task = get_task(id)

    return render_template(
        "edit.html",
        task=task
    )


@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    title = request.form["title"]
    description = request.form["description"]
    priority = request.form["priority"]

    update_task(
        id,
        title,
        description,
        priority
    )

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)