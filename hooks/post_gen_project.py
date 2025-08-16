from pathlib import Path
import subprocess

def remove_mysql_client():
    path = Path("internal", "clients", "mysql_client.go")
    if path.exists():
        path.unlink()

def remove_postgresql_client():
    path = Path("internal", "clients", "postgresql_client.go")
    if path.exists():
        path.unlink()

def remove_redis_client():
    path = Path("internal", "clients", "redis_client.go")
    if path.exists():
        path.unlink()

def remove_database_clients():
    if "{{cookiecutter.database}}" == "mysql":
        remove_postgresql_client()
    elif "{{cookiecutter.database}}" == "postgresql":
        remove_mysql_client()

def go_tidy():
    print('Running go mod tidy...')
    subprocess.run(["go", "mod", "tidy"], check=True)

def build_compose():
    print('Building Docker Compose files...')
    subprocess.run(["docker", "compose", "build"], check=True)

def run():
    print('Running post-generation hook...')

    remove_database_clients()
    
    if "{{cookiecutter.use_redis}}" == "no":
        remove_redis_client()

    if "{{cookiecutter.go_tidy}}" == "yes":
        go_tidy()

    if "{{cookiecutter.build_compose}}" == "yes":
        build_compose()

if __name__ == "__main__":
    run()
