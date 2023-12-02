from invoke import task

@task
def run(e):
    e.run("python main.py")

@task
def run_partie1(e):
    # Write score instead of underscore in the terminal while executing tasks :)
    e.run("python -m stat_desc_unv")