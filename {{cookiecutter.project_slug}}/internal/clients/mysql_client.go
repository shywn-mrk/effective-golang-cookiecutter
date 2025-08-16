package clients

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
	"github.com/spf13/viper"
)

func NewMySQLClient(cfg *viper.Viper) (*sql.DB, error) {
	user := cfg.GetString("mysql.user")
	password := cfg.GetString("mysql.password")
	host := cfg.GetString("mysql.host")
	port := cfg.GetInt("mysql.port")
	database := cfg.GetString("mysql.database")

	if user == "" || password == "" || host == "" || port == 0 || database == "" {
		return nil, fmt.Errorf("missing MySQL config values")
	}

	dsn := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?parseTime=true&loc=Asia%%2FTehran",
		user, password, host, port, database)

	db, err := sql.Open("mysql", dsn)
	if err != nil {
		return nil, err
	}

	if err := db.Ping(); err != nil {
		return nil, err
	}

	return db, nil
}
