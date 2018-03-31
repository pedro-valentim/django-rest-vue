#!/bin/bash
cd desafiodress

echo -e "\033[46;1;37m ======Instalando requisitos de desenvolvimento====== \033[0m"
make dev

echo -e "\033[46;1;37m ======Criando migrações e migrando banco====== \033[0m" 
make migrate

echo -e "\033[46;1;37m ======Rodando servidor de desenvolvimento====== \033[0m"
make run 
