# Transportation Lakeflow Pipeline

### From raw trip events to governed analytics in Databricks

![Databricks](https://img.shields.io/badge/Databricks-Runtime_14.3+-red?logo=databricks)
![Language](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Unity Catalog](https://img.shields.io/badge/Unity_Catalog-Enabled-orange)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)

Transportation Lakeflow Pipeline is a medallion-style data engineering solution for trip and city analytics. It uses Databricks Delta Live Tables, Lakeflow, and PySpark to move data from raw ingestion into cleaned, enriched, and business-ready gold outputs.

## Architecture

The pipeline follows the Bronze -> Silver -> Gold pattern to keep each transformation layer focused and easy to maintain.

```mermaid
graph LR
    A[Raw Source] --> B[Bronze: Ingestion]
    B --> C[Silver: Cleaning, Validation & Calendar Join]
    C --> D[Gold: Aggregated Analytics Views]
```

### Layer Breakdown

- **Bronze:** Ingests raw city and trip files from object storage using schema evolution and Auto Loader where needed.
- **Silver:** Standardizes trip fields, applies data quality expectations, and builds a reusable calendar dimension from the configured date range.
- **Gold:** Joins trips with city and calendar dimensions to produce analytics-ready views for reporting and dashboards.

## Features

- **Automated Schema Evolution** - Handles changing source structures with minimal manual intervention.
- **Data Quality Expectations** - Uses DLT expectations to validate trip dates and rating ranges.
- **Parameter-driven ETL** - Reads `start_date` and `end_date` from Spark configuration to control the calendar range and pipeline window.

## Folder Guide

```text
Goodcabs-Travels/
└── transformations/
    ├── bronze/
    │   ├── city.py
    │   └── trips.py
    ├── silver/
    │   ├── calendar.py
    │   ├── city.py
    │   └── trips.py
    └── gold/
        ├── trips_gold.sql
        ├── trips_chandigarh.sql
        ├── trips_coimbatore.sql
        ├── trips_indore.sql
        ├── trips_jaipur.sql
        ├── trips_kochi.sql
        ├── trips_lucknow.sql
        ├── trips_mysore.sql
        ├── trips_surat.sql
        ├── trips_vadodara.sql
        └── trips_visakhapatnam.sql
```

### Bronze

- `bronze/city.py`: Reads raw city data from S3 and adds file metadata and ingest timestamps.
- `bronze/trips.py`: Streams raw trip data with Auto Loader, renames problematic columns, and captures ingest metadata.

### Silver

- `silver/calendar.py`: Generates a date dimension from `start_date` to `end_date`, adds date attributes, and flags weekends and holidays.
- `silver/city.py`: Cleans the city dimension and carries forward bronze ingest metadata.
- `silver/trips.py`: Normalizes trip data, applies expectations, and prepares a CDC-friendly silver table.

### Gold

- `gold/trips_gold.sql`: Builds the main gold analytics view by joining trip, city, and calendar data.
- `gold/trips_*.sql`: City-specific gold views for targeted reporting and dashboard slices.

## How to Configure

Set the pipeline window in the DLT JSON settings before running the pipeline.

```json
{
  "configuration": {
    "start_date": "2024-01-01",
    "end_date": "2024-12-31"
  }
}
```

In the transformation code, the calendar layer reads these values directly from Spark:

```python
start_date = spark.conf.get("start_date")
end_date = spark.conf.get("end_date")
```

## Data Model

- **Bronze city:** raw city attributes plus file lineage metadata.
- **Bronze trips:** raw trip events with source metadata and standardized column names.
- **Silver calendar:** date dimension with fiscal-style attributes, weekdays, weekends, and holiday flags.
- **Silver trips:** cleaned transactional trip data ready for downstream joins.
- **Gold fact trips:** combined trip, city, and calendar view for analytics.

## Dashboards

### KPI Snapshot

| Metric | Value | Visual |
|---|---:|---|
| Total Revenue | $94M | ![Total Revenue](Dashboards/Total%20Revenue.png) |
| Total Trips | 366.14K | ![Total Trips](Dashboards/Total%20Trips.png) |
| Avg Distance (km) | 19.21 | ![Avg Distance](Dashboards/Avg%20Distance%20(km).png) |
| Avg Passenger Rating | 7.68 | ![Avg Passenger Rating](Dashboards/Avg%20Passenger%20Rating.png) |
| Holiday Trips | 4.93K | ![Holiday Trips](Dashboards/Holiday%20Trips.png) |
| Weekday Trips | 284.88K | ![Weekday Trips](Dashboards/Weekday%20Trips.png) |
| Weekend Trips | 81.26K | ![Weekend Trips](Dashboards/Weekend%20Trips.png) |

### Trend Analysis

![Revenue Over Time](Dashboards/Revenue%20Over%20Time.png)

![Trips Over Time](Dashboards/Trips%20Over%20Time.png)

### Segment Analysis

![Revenue by City](Dashboards/Revenue%20by%20City.png)

![Trips by City](Dashboards/Trips%20by%20City.png)

![Trips by Day of Week](Dashboards/Trips%20by%20Day%20of%20Week.png)

![Trips by Passenger Category](Dashboards/Trips%20by%20Passenger%20Category.png)

These visuals are sourced from the [Dashboards](Dashboards) folder and represent the current Gold-layer analytics outputs.

## Deployment Notes

- Use Unity Catalog objects for governed table and view registration.
- Configure the pipeline with the required DLT JSON parameters before deployment.
- Run the Bronze, Silver, and Gold layers in Databricks to materialize the full medallion flow.

## Contributing

Pull requests that improve transformations, documentation, or analytics coverage are welcome.

## License

Add your preferred license here.