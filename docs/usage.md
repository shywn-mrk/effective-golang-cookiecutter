# Usage

## Prerequisites
- Python 3.13+
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
- Go 1.24+
- Docker (optional, for containerization)

## Generating a Project
Run the following command:

```bash
cookiecutter https://github.com/shywn-mrk/effective-golang-cookiecutter
```

You will be prompted for project variables (e.g., `project_slug`).

## Building and Running
Navigate to your generated project and use the provided `Makefile`:

```bash
make build
make run
```

## Docker
To build and run with Docker:

```bash
docker-compose up --build
```
