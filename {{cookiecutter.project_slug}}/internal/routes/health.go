package routes

import (
    "{{cookiecutter.project_complete_name}}/internal/handlers"
    "github.com/gin-gonic/gin"
)

func RegisterHealthRoutes(r *gin.Engine) {
    r.GET("/health", handlers.HealthHandler)
}
