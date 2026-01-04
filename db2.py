#!/usr/bin/env python3

import os
import uuid
from sqlalchemy import create_engine, Column, String, Boolean, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import JSONB, UUID

Base = declarative_base()


class FacebookListing(Base):
    __tablename__ = "facebookListingDataRecord"

    id = Column(Integer, primary_key=True)
    query = Column(String(100))
    record_hash = Column(String(255), unique=True)
    batch_id = Column(UUID(as_uuid=True), nullable=False)
    listing_id = Column(String)
    primary_listing_photo = Column(JSONB)
    if_gk_just_listed_tag_on_search_feed = Column(JSONB)
    listing_price = Column(JSONB)
    location = Column(JSONB)
    is_hidden = Column(Boolean, default=False)
    is_live = Column(Boolean, default=False)
    is_pending = Column(Boolean, default=False)
    is_sold = Column(Boolean, default=False)
    is_viewer_seller = Column(Boolean, default=False)
    marketplace_listing_category_id = Column(String)
    marketplace_listing_title = Column(String(100))
    parent_listing = Column(String)
    marketplace_listing_seller = Column(JSONB)
    delivery_types = Column(JSONB)
    product_feedback = Column(String)


class Database:
    """Manages database connection and provides access to repositories"""

    def __init__(self):
        self.db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        self.engine = create_engine(self.db_url)
        self.sessionLocal = sessionmaker(bind=self.engine)
        self.session = None

    def __enter__(self):
        Base.metadata.create_all(self.engine)
        self.session = self.sessionLocal()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()
        return False


def main():
    with Database() as db:
        print("initializing db")
        db.session.add(
            FacebookListing(
                query="Nvidia GPU 5070",
                record_hash="123",
                batch_id=uuid.uuid4(),
                listing_id="abc",
                primary_listing_photo={"abc": "123"},
                if_gk_just_listed_tag_on_search_feed={"abc": "123"},
                listing_price={"abc": "123"},
                location={"abc": "123"},
                is_hidden=False,
                is_live=False,
                is_pending=False,
                is_sold=False,
                is_viewer_seller=False,
                marketplace_listing_category_id="abc",
                marketplace_listing_title="abc",
                parent_listing="abc",
                marketplace_listing_seller={"abc": "123"},
                delivery_types={"abc": "123"},
                product_feedback="abc",
            )
        )
        # db.session.commit()

if __name__ == "__main__":
    main()  
