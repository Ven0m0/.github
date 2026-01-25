# Multi-stage Go Dockerfile
# Customize for your project

# Build stage
FROM golang:1.22-alpine AS builder

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache git ca-certificates

# Copy go mod files
COPY go.mod go.sum ./
RUN go mod download && go mod verify

# Copy source
COPY . .

# Build with optimizations
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build \
    -ldflags="-w -s -X main.version=$(git describe --tags --always --dirty 2>/dev/null || echo dev)" \
    -trimpath \
    -o /app/server \
    ./cmd/server


# Production stage - distroless for security
FROM gcr.io/distroless/static-debian12 AS production

WORKDIR /app

# Copy binary and certs
COPY --from=builder /app/server /app/server
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

# Non-root user (distroless provides nonroot user)
USER nonroot:nonroot

EXPOSE 8080

ENTRYPOINT ["/app/server"]
