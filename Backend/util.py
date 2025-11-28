import psycopg2



DB_URL = 'postgresql://postgres.plfcbrrmqulhjavgkyhf:1234567@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres'


def get_conn():
    conn = psycopg2.connect(DB_URL)
    return conn