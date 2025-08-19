#################################
#          Build Stage          #
#################################
FROM golang:1.24-alpine AS builder
WORKDIR /app
COPY . .
RUN go mod tidy && go build -o {{ cookiecutter.project_slug }} ./cmd/main.go

#################################
#           Run Stage           #
#################################
FROM alpine:3.22
WORKDIR /app
COPY --from=builder /app/{{ cookiecutter.project_slug }} ./{{ cookiecutter.project_slug }}
COPY config/config.yaml ./config/config.yaml
EXPOSE 8000
CMD ["./{{ cookiecutter.project_slug }}"]
