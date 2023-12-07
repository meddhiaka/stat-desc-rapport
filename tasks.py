from invoke import task

@task
def run(e):
    e.run("python main.py")

@task
def run_partie1(e):
    # Write score instead of underscore in the terminal while executing tasks :)
    e.run("python -m stat_desc_unv")

@task
def run_partie2(e):
    e.run("python -m courbe_mat")