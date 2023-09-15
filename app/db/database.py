# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # PostgreSQL connection information
# DATABASE_URL = "postgresql://useradm:hacka123@localhost:5488/divzero-db"

# # Create a SQLAlchemy database engine
# engine = create_engine(DATABASE_URL)

# # Create a session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create a base class for declarative models
# Base = declarative_base()


# # Function to initialize the database tables
# def init_db():
#     Base.metadata.create_all(bind=engine)


# # Function to get a database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
