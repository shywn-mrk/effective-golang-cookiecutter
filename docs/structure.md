# Project Structure

The generated project includes the following structure:

```
{{cookiecutter.project_slug}}/
├── cmd/
│   └── main.go
├── config/
│   ├── config.go
│   └── config.yaml
├── docker/
│   └── golang/
│       └── Dockerfile
├── internal/
│   ├── clients/
│   │   ├── mysql_client.go
│   │   ├── postgresql_client.go
│   │   └── redis_client.go
│   ├── handlers/
│   │   └── health.go
│   ├── logging/
│   │   └── logging.go
│   ├── routes/
│   │   └── health.go
│   └── server/
│       └── server.go
├── pkg/
│   ├── grpc_server/
│   │   └── server.go
│   └── models/
├── docker-compose.yaml
├── go.mod
├── go.sum
├── LICENSE
├── main.go
├── Makefile
└── README.md
```

This structure supports modular development, containerization, and easy configuration.
