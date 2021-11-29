# Objeto de conexão para encontrar o servidor, sql logon e efetivar a conexão
from app import app
from flaskext.mysql import MySQL
from flask_basicauth import BasicAuth
import os
from  dotenv  import  load_dotenv, find_dotenv

load_dotenv (find_dotenv())   # obtém variáveis ​​de ambiente de .env. find_dotenv()

# USERNAME = os.environ['BASIC_AUTH_USERNAME']

app.config['BASIC_AUTH_USERNAME']= os.environ['BASIC_AUTH_USERNAME']
app.config['BASIC_AUTH_PASSWORD']= os.environ['BASIC_AUTH_PASSWORD']
auth = BasicAuth(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_DATABASE_PASSWORD'] #insira a sua senha do DB
app.config['MYSQL_DATABASE_DB'] = 'db_clientes' #insira o nome do seu DB
app.config['MYSQL_DATABASE_DB'] = 'db_produtos' #insira o nome do seu DB
app.config['MYSQL_DATABASE_DB'] = 'db_vendas' #insira o nome do seu DB
app.config['MYSQL_DATABASE_HOST'] = 'db_mysql' #colocar o endpoint do RDS


mysql.init_app(app)