import mysql.connector

# Conexão ao banco de dados MySQL
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="game12"
)

# Cursor para executar comandos SQL
crs = connection.cursor()

# Lambda para executar comandos SQL
execsqlcmd = lambda cmd, crs: crs.execute(cmd)

# Lambda para gerar cláusulas INNER JOIN
generate_joins = lambda tables_with_aliases, join_conditions: \
    f"FROM {tables_with_aliases[0][0]} AS {tables_with_aliases[0][1]} " + \
    " ".join(f"INNER JOIN {tbl} AS {alias} ON {cond}" for (tbl, alias), cond in zip(tables_with_aliases[1:], join_conditions))

# Lambda para gerar consultas SELECT
generate_select = lambda columns, from_joins, where=None, group_by=None, having=None: \
    f"SELECT {', '.join(columns)} {from_joins}" + \
    (f" WHERE {where}" if where else "") + \
    (f" GROUP BY {group_by}" if group_by else "") + \
    (f" HAVING {having}" if having else "")

# Definição das tabelas e seus aliases
tables = [("GAMES", "g"), ("VIDEOGAMES", "v"), ("COMPANY", "c")]

# Condições de JOIN
conditions = [
    "g.id_console = v.id_console",
    "v.id_company = c.id_company"
]

# Gerar cláusula JOIN
joins = generate_joins(tables, conditions)

# Colunas a serem selecionadas
selected_columns = ["g.title", "c.name as Company", "COUNT(c.id_company) as NumOfCompanies"]

# Gerar consulta SELECT incluindo todas as colunas não agregadas na cláusula GROUP BY
query = generate_select(selected_columns, joins, group_by="g.title, c.name", having="COUNT(c.id_company) > 1")

print(query)
