
# FAST BUSINES

Este é um aplicativo back-end desenvolvido em Python e Django que oferece um CRUD de usuários e produtos. Ele permite a exposição de uma vitrine de produtos aos clientes e oferece aos administradores a capacidade de gerenciar o estoque de produtos. Com esta aplicação, é possível realizar todas as operações básicas de um CRUD, incluindo criar, ler, atualizar e excluir usuários e produtos.




## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:CarlosX26/fast-busines-back-end.git
```

Entre no diretório do projeto

```bash
  cd fast-busines-back-end
```

A partir disso, prossiga com os passos:

1 - crie seu ambiente virtual:
```bash
  python -m venv venv
```

2 - ative seu venv:
```bash
# linux:
  source venv/bin/activate

# windows:
  .\venv\Scripts\activate
```
3 - instalando dependências:
```bash
  pip install -r requirements.txt 
```
4 - rodando migrações:
```bash
  python manage.py migrate
```



## Stack utilizada

**Back-end:** Python, Django, DjangoRestFramework e PostgreSQL.


## link para documentação
https://fast-busines.onrender.com/api/docs/
