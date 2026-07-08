-- PURPOSE:
-- Create raw tables for Snowflake data ingestion

CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE if not exists raw.afru (
    aufnr TEXT,                     -- order number
    budat TEXT,                     -- posting date (YYYYMMDD)
    gmnga NUMERIC,                  -- yield qty
    xmnga NUMERIC,                  -- scrap qty
    gmein TEXT,                     -- unit
    werks TEXT,                     -- plant
    vornr TEXT                      -- operation
);

CREATE TABLE if not exists raw.material_movements (
    document_segment_material_order TEXT,   -- order number
    posting_date DATE,                      -- posting date
    inventory_movement_type_code TEXT,      -- 261 / 262 / 531 / 532
    material_movement_quantity NUMERIC,     -- quantity
    material_number TEXT,                  -- gold code
    plant TEXT                              -- plant
);