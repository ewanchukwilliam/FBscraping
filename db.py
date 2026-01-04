#!/usr/bin/env python3

from contextlib import contextmanager
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import psycopg2
import os
import json
import uuid
from api_handler import debuggingMarketplaceQuery

@dataclass
class jsonListingData:
    query: str
    record_hash: str
    batch_id: uuid.UUID
    listing_id: str
    primary_listing_photo: dict
    if_gk_just_listed_tag_on_search_feed: dict
    listing_price: dict
    location: dict
    is_hidden: bool
    is_live: bool
    is_pending: bool
    is_sold: bool
    is_viewer_seller: bool
    marketplace_listing_category_id: str
    marketplace_listing_title: str
    parent_listing: str
    marketplace_listing_seller: dict
    delivery_types: dict
    product_feedback: str

class Database:
    """Manages database connection and provides access to repositories"""

    def __init__(self):
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.conn = None
        self.cursor = None
        self.initialized = False

    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port
        )
        self.cursor = self.conn.cursor()
        if not self.initialized:
            self.facebookListingData = facebookListingDataRecord(self.cursor, self.conn)
            self.facebookListingData.createTable()
            # self.errors = ErrorRecords(self.cursor, self.conn)
            # self.errors.createTable()
            # self.pricing = InsiderTradingPricingRecords(self.cursor, self.conn)
            # self.pricing.createTable()
            # self.options = InsiderTradingOptionsRecords(self.cursor, self.conn)
            # self.options.createTable()
            # self.logging = logging(self.cursor, self.conn)
            # self.logging.createTable()
            self.initialized=True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.close()
        return False

class facebookListingDataRecord:
    """records all responses from facebook query"""

    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn
        self.table_name = "facebookListingDataRecord"

    def createTable(self):
        """Create options table if it doesn't exist"""
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (

                id SERIAL PRIMARY KEY,
                query VARCHAR(100),
                record_hash VARCHAR(255) UNIQUE,
                batch_id UUID,
                listing_id TEXT,
                primary_listing_photo JSONB,
                if_gk_just_listed_tag_on_search_feed JSONB,
                listing_price JSONB,
                location JSONB,
                is_hidden BOOL,
                is_live BOOL,
                is_pending BOOL,
                is_sold BOOL,
                is_viewer_seller BOOL,
                marketplace_listing_category_id TEXT,
                marketplace_listing_title VARCHAR(100),
                parent_listing TEXT,
                marketplace_listing_seller JSONB,
                delivery_types JSONB,
                product_feedback TEXT

            )
        """)
        # Index for querying by query
        self.cursor.execute(f"""
            CREATE INDEX IF NOT EXISTS idx_{self.table_name}_query
            ON {self.table_name}(query)
        """)
        # Index for foreign key relationship
        print(f"Table {self.table_name} created successfully")

    def insert(self, data: jsonListingData):
        """
        Insert Options data for a specific trade (record_hash).
        df: pandas DataFrame from options API
        queryData: the specific trade this Options data belongs to
        """
        self.cursor.execute(f"""
            INSERT INTO {self.table_name}
            (query, record_hash, batch_id, listing_id, primary_listing_photo, if_gk_just_listed_tag_on_search_feed,
             listing_price, location, is_hidden, is_live, is_pending, is_sold, is_viewer_seller, marketplace_listing_category_id,
             marketplace_listing_title, parent_listing, marketplace_listing_seller, delivery_types, product_feedback)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (record_hash) DO NOTHING
        """, (data.query, data.record_hash, str(data.batch_id), data.listing_id, json.dumps(data.primary_listing_photo),
              json.dumps(data.if_gk_just_listed_tag_on_search_feed), json.dumps(data.listing_price), json.dumps(data.location), data.is_hidden,
              data.is_live, data.is_pending, data.is_sold, data.is_viewer_seller, data.marketplace_listing_category_id,
              data.marketplace_listing_title, data.parent_listing, json.dumps(data.marketplace_listing_seller), json.dumps(data.delivery_types),
              data.product_feedback))
        print(f"Inserted {data.query} (hash: {str(data.record_hash)[:8]}...)")
        return True

    def get_duplicates(self, queryData):
        """Check for duplicates in the database"""
        self.cursor.execute(f"""
            SELECT * FROM {self.table_name}
            WHERE record_hash = %s
        """, (queryData.record_hash,))
        if self.cursor.rowcount > 0:
            return True
        return False

# class ErrorRecords:
#     """Records All API errors and their raw responses"""
#     def __init__(self, cursor, conn):
#         self.cursor = cursor
#         self.conn = conn
#         self.table_name = "ErrorRecords"
#
#     def createTable(self):
#         """Create error records table if it doesn't exist"""
#         self.cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS {self.table_name} (
#                 id SERIAL PRIMARY KEY,
#                 batch_id UUID,
#                 occurred_at TIMESTAMP DEFAULT NOW(),
#                 error_type VARCHAR(100),
#                 error_message TEXT,
#                 raw_json JSONB,
#                 stack_trace TEXT
#             )
#         """)
#         # Create index for querying by batch
#         self.cursor.execute(f"""
#             CREATE INDEX IF NOT EXISTS idx_error_batch_id
#             ON {self.table_name}(batch_id)
#         """)
#         print(f"Table {self.table_name} created successfully")
#
#     def log_error(self, batch_id, error_type, error_msg, raw_data, stack_trace=None):
#         """Log an error to the error table"""
#         self.cursor.execute(f"""
#             INSERT INTO {self.table_name}
#             (batch_id, error_type, error_message, raw_json, stack_trace)
#             VALUES (%s, %s, %s, %s, %s)
#         """, (batch_id, error_type, error_msg, json.dumps(raw_data), stack_trace))
#
#     def show_all_errors(self):
#         """Show all errors in the error table"""
#         self.cursor.execute(f"""
#             SELECT * FROM {self.table_name}
#         """)
#         for row in self.cursor:
#             print(row)  # Prints each row as a tuple    

# class logging:
#     def __init__(self, cursor, conn):
#         self.cursor = cursor
#         self.conn = conn
#         self.table_name = "LoggingInfo"
#
#     def createTable(self):
#         """Create options table if it doesn't exist"""
#         self.cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS {self.table_name} (
#                 id SERIAL PRIMARY KEY,
#                 batch_id UUID,
#                 started_at TIMESTAMP DEFAULT NOW(),
#                 ended_at TIMESTAMP DEFAULT NOW(),
#                 status VARCHAR(10),
#                 total_records_processed INTEGER,
#                 records_inserted INTEGER,
#                 records_skipped INTEGER,
#                 pricing_records_inserted INTEGER,
#                 options_records_inserted INTEGER,
#                 error_count INTEGER,
#                 execution_time_seconds DECIMAL,
#                 db_operation_time_seconds DECIMAL,
#                 api_call_time_seconds DECIMAL,
#                 querys_with_pricing INTEGER,
#                 querys_with_options INTEGER,
#                 exit_code INTEGER,
#                 duplicated_trades INTEGER,
#                 time_to_fetch_trades DECIMAL,
#                 time_to_fetch_price DECIMAL,
#                 time_to_fetch_options DECIMAL,
#                 log_timestamp TIMESTAMP DEFAULT NOW()
#             )
#         """)
#         print(f"Table {self.table_name} created successfully")
#
#
#     def log_batch(self, batch_id, metrics: BatchMetrics):
#         """Log batch execution metrics to database"""
#         if not isinstance(metrics, BatchMetrics):
#             raise TypeError(f"metrics must be BatchMetrics, got {type(metrics)}")
#         self.cursor.execute(f"""
#             INSERT INTO {self.table_name}
#             (batch_id, started_at, ended_at, status, total_records_processed, records_inserted, records_skipped,
#             pricing_records_inserted, options_records_inserted, error_count, execution_time_seconds,
#             db_operation_time_seconds, api_call_time_seconds, querys_with_pricing, querys_with_options, exit_code,
#             duplicated_trades, time_to_fetch_trades, time_to_fetch_price, time_to_fetch_options, log_timestamp)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """, (batch_id, metrics.started_at, metrics.ended_at, metrics.status, metrics.total_records_processed,
#               metrics.records_inserted, metrics.records_skipped, metrics.pricing_records_inserted,
#               metrics.options_records_inserted, metrics.error_count, metrics.execution_time_seconds,
#               metrics.db_operation_time_seconds, metrics.api_call_time_seconds, metrics.querys_with_pricing,
#               metrics.querys_with_options, metrics.exit_code, metrics.duplicated_trades,
#               metrics.time_to_fetch_trades, metrics.time_to_fetch_price, metrics.time_to_fetch_options,
#               metrics.log_timestamp))
#         print(f"Data processed for {metrics.status} (hash: {batch_id[:8]}...)")
        



# if __name__ == "__main__":
#     print("Running main...")
#     with Database() as db:
#         print("Initialized DB")
#         collection = queryCollection()
#         listData = collection.queryList
#         total_time_outside_requests=0
#         batch_id = str(uuid.uuid4())
#         for data in listData:
#             print(data.symbol)      
#             try:
#                 db.querys.insert(data)
#                 data.getPriceData()
#                 interval1_start= time.time()
#                 db.pricing.insert(data.priceData, data)
#                 interval1_end= time.time()
#                 data.getOptionsData()
#                 interval2_start= time.time()
#                 db.options.insert(data.optionsData, data)
#                 interval2_end= time.time()
#                 total_time_outside_requests=total_time_outside_requests+(interval1_end-interval1_start)+(interval2_end-interval2_start)
#
#             except Exception as e:
#                 print("threw an error down here " + str(e)+ " for query symbol: "+ data.symbol)
#                 db.errors.log_error(batch_id, "Error inserting data for "+data.symbol, str(e), {"symbol": data.symbol})
#         print(f"Total time spent outside requests: {total_time_outside_requests}")

if __name__ == "__main__":
    print("Running main...")
    with Database() as db:
        print("Initialized DB")
        qe = debuggingMarketplaceQuery()
        qe.change_query("Nvidia GPU 5070")
        # qe.change_location(49.2327, -123.1207) # Vancouver
        qe.fetchRequest()
        qe.printResponseListingTitles()

        # Loop through listings and insert each one
        batch_id = uuid.uuid4()

        # Define expected fields from the API response
        expected_fields = {
            "primary_listing_photo",
            "if_gk_just_listed_tag_on_search_feed",
            "listing_price",
            "location",
            "is_hidden",
            "is_live",
            "is_pending",
            "is_sold",
            "is_viewer_seller",
            "marketplace_listing_category_id",
            "marketplace_listing_title",
            "parent_listing",
            "marketplace_listing_seller",
            "delivery_types",
            "product_feedback"
        }

        for listing_edge in qe.responseListingData:
            if "listing" in listing_edge["node"]:
                listing = listing_edge["node"]["listing"]

                # Only extract fields that exist in both the API response and dataclass
                filtered_listing = {}
                for k, v in listing.items():
                    if k in expected_fields:
                        filtered_listing[k] = v

                # filtered_listing = {k: v for k, v in listing.items() if k in expected_fields}

                listing_data = jsonListingData(
                    query="GPU",
                    record_hash=str(listing["id"]),
                    batch_id=batch_id,
                    listing_id=str(listing["id"]),
                    **filtered_listing
                )

                db.facebookListingData.insert(listing_data)

