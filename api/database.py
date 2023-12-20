import psycopg2

postgres_db = psycopg2.connect(database="mydacia",
                               host="localhost",
                               user="postgres",
                               password="pns",
                               port="5432")

