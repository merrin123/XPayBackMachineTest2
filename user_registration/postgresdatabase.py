from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL Configuration
postgres_engine = create_engine('postgresql://postgres:postgres123@localhost/registration')
PostgresBase = declarative_base()

PostgresBase.metadata.create_all(postgres_engine)
PostgresSession = sessionmaker(bind=postgres_engine)
postgres_session = PostgresSession()