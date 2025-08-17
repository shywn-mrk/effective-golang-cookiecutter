package server

import (
    "context"
    "net/http"

    "github.com/gin-gonic/gin"
    "{{cookiecutter.project_complete_name}}/internal/routes"
    "go.uber.org/fx"
    "go.uber.org/zap"
)

func NewGinRouter() *gin.Engine {
    r := gin.New()

    routes.RegisterHealthRoutes(r)

    return r
}

func RegisterHTTPServer(lc fx.Lifecycle, logger *zap.Logger, router *gin.Engine) {
    lc.Append(fx.Hook{
        OnStart: func(ctx context.Context) error {
            go func() {
                logger.Info("HTTP server started on :8000")
                if err := http.ListenAndServe(":8000", router); err != nil && err != http.ErrServerClosed {
                    logger.Error("HTTP server error", zap.Error(err))
                }
            }()
            return nil
        },
        OnStop: func(ctx context.Context) error {
            logger.Info("HTTP server stopped")
            return nil
        },
    })
}
