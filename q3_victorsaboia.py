import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root"
)

crs = connection.cursor()

execsqlcmd =  lambda cmd, crs: crs.execute(cmd)

execcreatetable = lambda table, attrs, crs: execsqlcmd("CREATE TABLE " + table + " (" + attrs + ");\n", crs)
execcreatedatabase = lambda dbname, crs: execsqlcmd("CREATE DATABASE " + dbname + ";\n", crs)
execdropdatabase = lambda dbname, crs: execsqlcmd("DROP DATABASE " + dbname + ";\n", crs)
execdroptable = lambda dbname, crs: execsqlcmd("DROP TABLE " + dbname + ";\n", crs)
execusedatabase = lambda dbname, crs: execsqlcmd("USE " + dbname + ";\n", crs)


execcreatedatabase("game12", crs);
execusedatabase("game12", crs);


execcreatetable('USERS', 'id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), country VARCHAR(255), id_console INT', crs)
execcreatetable('VIDEOGAMES', 'id_console INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), id_company INT, release_date DATE', crs)
execcreatetable('GAMES', 'id_game INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), genre VARCHAR(255), release_date DATE, id_console INT', crs)
execcreatetable('COMPANY', 'id_company INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), country VARCHAR(255)', crs)



create = lambda table, data: crs.execute(
    f"INSERT INTO {table} ({', '.join(data.keys())}) VALUES ({', '.join(['%s'] * len(data))})",
    tuple(data.values())
)

delete = lambda table, condition: crs.execute(
    f"DELETE FROM {table} WHERE {condition}"
)

select = lambda table, condition=None: (
    crs.execute(f"SELECT * FROM {table}" + (f" WHERE {condition}" if condition else "")),
    crs.fetchall()
)

insert_data_company = {
    "name": "Company 1",
    "country": "Brazil"
}

insert_data_consoles= {
    "name": "Console 1",
    "id_company": "1"
}

insert_data_user= {
    "name": "User 1",
    "id_console": "1",
    "country": "Brazil"
}

create("COMPANY", insert_data_company)
connection.commit()

create("VIDEOGAMES", insert_data_consoles)
connection.commit()

create("USERS", insert_data_user)
connection.commit()

delete("USERS", "id=1")
connection.commit()

records = select("COMPANY")[1]
print(records)

connection.close()