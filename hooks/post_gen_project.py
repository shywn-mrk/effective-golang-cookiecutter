
import shutil
import subprocess
from pathlib import Path

cookiecutter = {
    "use_git": "{{cookiecutter.use_git}}"
}


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
    print("Running go mod tidy...")
    subprocess.run(["go", "mod", "tidy"], check=True)


def build_compose():
    print("Building Docker Compose files...")
    subprocess.run(["docker", "compose", "build"], check=True)


def git_init():
    print("Initializing Git repository...")
    subprocess.run(["git", "init"], check=True)


def install_pre_commit():
    if cookiecutter.get("use_git", "yes") == "no":
        print("Skipping pre-commit installation because Git is not used.")
        return

    result = subprocess.run(
        ["which", "pre-commit"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("pre-commit is not installed or not found in PATH. Skipping pre-commit hooks.")  # noqa
        return

    print("Installing pre-commit ...")
    subprocess.run(["pre-commit", "install"], check=True)


def remove_grpc_server():
    shutil.rmtree(Path("pkg", "grpc_server"), ignore_errors=True)


def remove_docker():
    # Remove Dockerfiles
    shutil.rmtree(Path("docker"), ignore_errors=True)

    # Remove docker compose file
    (Path("docker-compose.yaml")).unlink(missing_ok=True)


def remove_licence():
    path = Path("LICENSE")
    if path.exists():
        path.unlink()


def run():
    print("Running post-generation hook...")

    remove_database_clients()

    if "{{cookiecutter.open_source_license}}" == "Not open source":
        remove_licence()

    if "{{cookiecutter.use_redis}}" == "no":
        remove_redis_client()

    if "{{cookiecutter.go_tidy}}" == "yes":
        go_tidy()

    if "{{cookiecutter.use_docker}}" == "no":
        remove_docker()

    if "{{cookiecutter.build_compose}}" == "yes":
        build_compose()

    if "{{cookiecutter.use_git}}" == "yes":
        git_init()

    if "{{cookiecutter.install_pre_commit}}" == "yes":
        install_pre_commit()

    if "{{cookiecutter.use_grpc_server}}" == "no":
        remove_grpc_server()


if __name__ == "__main__":
    run()
