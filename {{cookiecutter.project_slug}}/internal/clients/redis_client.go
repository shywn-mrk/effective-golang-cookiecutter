package clients

import (
    "github.com/go-redis/redis/v8"
    "github.com/spf13/viper"
)

var Client *redis.Client

func NewRedisClient(cfg *viper.Viper) *redis.Client {
    addr := cfg.GetString("redis.addr")
    password := cfg.GetString("redis.password")
    db := cfg.GetInt("redis.db")

    return redis.NewClient(&redis.Options{
        Addr:     addr,
        Password: password,
        DB:       db,
    })
}
