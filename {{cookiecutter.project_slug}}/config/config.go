package config

import "github.com/spf13/viper"

func NewConfig() *viper.Viper {
	v := viper.New()
	v.SetConfigName("config")
	v.AddConfigPath("./config")
	_ = v.ReadInConfig()
	return v
}
