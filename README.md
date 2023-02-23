
# FAST BUSINES

um crud de usúarios e produtos onde você expor sua vitrine de produtos.




## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:CarlosX26/crud-users-products.git
```

Entre no diretório do projeto

```bash
  cd crud-users-products
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

**Back-end:** Python, Django, DjangoRestFramework e sqlite.


## link para documentação
http://localhost:8000/api/docs/
