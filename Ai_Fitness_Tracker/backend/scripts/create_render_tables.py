"""
Script to create all database tables on Render PostgreSQL.
Run from backend directory: python scripts/create_render_tables.py
"""
import sys
import os

# Add the parent directory to path so we can import app modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.database import sync_engine, Base
# Import ALL models so they register themselves on Base before create_all
from app.db import models  # noqa: F401

def create_tables():
    print("Connecting to database...")
    print(f"Database URL: {str(sync_engine.url)[:60]}...")
    print("\nCreating all tables...")
    try:
        Base.metadata.create_all(bind=sync_engine)
        print("\n✅ All tables created successfully!")
        print("\nTables created:")
        for table_name in Base.metadata.tables.keys():
            print(f"  - {table_name}")
    except Exception as e:
        print(f"\n❌ Error creating tables: {e}")
        raise

if __name__ == "__main__":
    create_tables()
