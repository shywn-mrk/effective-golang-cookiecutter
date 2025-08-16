package main

import (
	"go.uber.org/fx"
	"{{cookiecutter.project_complete_name}}/config"
	{%- if cookiecutter.use_redis == "yes" or cookiecutter.database == "mysql" %}
	"{{cookiecutter.project_complete_name}}/internal/clients"
	{%- endif %}
	"{{cookiecutter.project_complete_name}}/internal/logging"
	"{{cookiecutter.project_complete_name}}/internal/server"
)

func main() {
	app := fx.New(
		fx.Provide(
			logging.NewLogger,
			config.NewConfig,
			{%- if cookiecutter.use_redis == "yes" %}
			clients.NewRedisClient,
			{%- endif %}
			{%- if cookiecutter.database == "mysql" %}
			clients.NewMySQLClient,
			{%- endif %}
			server.NewGinRouter,
		),
		fx.Invoke(server.RegisterHTTPServer),
	)
	app.Run()
}
