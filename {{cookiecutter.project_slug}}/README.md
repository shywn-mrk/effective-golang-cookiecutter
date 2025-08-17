# Orderbook Service

A basic Golang service using Uber Fx for dependency injection, Uber Zap for logging, and Viper for configuration management.

## Features

- Dependency injection with Uber Fx
- Structured logging with Uber Zap
- Config management with Viper
- Containerized with Docker
- Pre-commit static analysis with golangci-lint

## Usage

### Build and Run

```bash
go build -o orderbook ./cmd/main.go
./orderbook
```

### Docker

```bash
docker build -t orderbook .
docker run --rm -p 8000:8000 orderbook
```

### Pre-commit

Install pre-commit and set up hooks:

```bash
brew install pre-commit
pre-commit install
```
