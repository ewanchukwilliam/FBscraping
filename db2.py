#!/usr/bin/env python3

import os
import uuid
from sqlalchemy import create_engine, Column, String, Boolean, Integer, inspect
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import JSONB, UUID

from api_handler import debuggingMarketplaceQuery

Base = declarative_base()


class FacebookListing(Base):
    __tablename__ = "facebookListingDataRecord"

    id = Column(Integer)
    query = Column(String(100))
    record_hash = Column(String(255), unique=True)
    batch_id = Column(UUID(as_uuid=True), nullable=False)
    listing_id = Column(String, primary_key=True)
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
    
    @classmethod
    def insert_api_response(cls, api_data: dict, query: str, batch_id: uuid.UUID):
        """
        Insert listing data from API response
        Automatically maps fields
        """
        # Get all column names
        mapper = inspect(cls)
        model_fields = {column.key for column in mapper.columns}
        exclude = {'id', 'query', 'record_hash', 'batch_id', 'listing_id'}
        filtered = {}
        for k, v in api_data.items():
            if k in model_fields and k not in exclude:
                filtered[k] = v

        return cls(
            query=query,
            record_hash=str(api_data["id"]),
            batch_id=batch_id,
            listing_id=str(api_data["id"]),
            **filtered
        )



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
        print("Fetching data...")
        qe = debuggingMarketplaceQuery()
        query = "Nvidia GPU 5070"
        qe.change_query(query)
        qe.fetchRequest()
        print("Printing response...")
        # qe.printResponseListingTitles()
        batch_id = uuid.uuid4()

        for listing_edge in qe.responseListingData:
            if "listing" in listing_edge["node"]:
                try:
                    listing = listing_edge["node"]["listing"]
                    new_listing = FacebookListing.insert_api_response(listing, query=query, batch_id=batch_id)
                    db.session.merge(new_listing)
                except Exception as e:
                    print(f"Error: {e}")    
        #
        # db.session.commit()

if __name__ == "__main__":
    main()  
