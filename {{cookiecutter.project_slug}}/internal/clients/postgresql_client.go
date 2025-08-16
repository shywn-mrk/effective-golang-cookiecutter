package clients

import (
    "context"
    "github.com/jackc/pgx/v4"
)

type PostgreSQLClient struct {
    conn *pgx.Conn
}

func NewPostgreSQLClient(ctx context.Context, connString string) (*PostgreSQLClient, error) {
    conn, err := pgx.Connect(ctx, connString)
    if err != nil {
        return nil, err
    }
    return &PostgreSQLClient{conn: conn}, nil
}
