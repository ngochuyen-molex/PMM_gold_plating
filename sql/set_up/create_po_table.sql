CREATE TABLE IF NOT EXISTS raw.gold_movement (
    raw_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    -- ETL metadata
    load_batch_id TEXT,
    source_extract_time TIMESTAMP DEFAULT now(),

    -- order info
    order_number TEXT NOT NULL,
    part_number TEXT,
    part_name TEXT,
    work_center TEXT,
    posting_date DATE NOT NULL,
    
    -- production info
    yield NUMERIC,
    scrap NUMERIC,

    -- gold movement (important!)
    gold_usage NUMERIC,
    gold_backflush NUMERIC,
    gold_byproduct_531 NUMERIC,
    gold_reversal_532 NUMERIC,

    -- derived count
    movement_entry_count NUMERIC
);