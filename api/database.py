import psycopg2

postgres_db = psycopg2.connect(database="mydacia",
                               host="db",
                               user="postgres",
                               password="test123",
                               port="5432")

