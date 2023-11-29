from invoke import task

@task
def run(e):
    e.run("python main.py")
