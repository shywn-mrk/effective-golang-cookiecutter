# Fast development with live reload
dev:
	@which air > /dev/null || (echo 'Please install air: https://github.com/cosmtrek/air' && exit 1)
	air

# Build the binary
build:
	go build -o orderbook ./cmd/main.go

# Run tests
test:
	go test ./...

# Start all services with Docker Compose
docker-up:
	docker-compose up --build

# Stop all services
docker-down:
	docker-compose down
