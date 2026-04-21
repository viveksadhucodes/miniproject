# Miniproject

![Databricks](https://img.shields.io/badge/Databricks-Runtime_14.3+-red?logo=databricks)
![Language](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)

This repository contains a Databricks-based transportation analytics pipeline built with Delta Live Tables, Lakeflow, PySpark, and Unity Catalog. The full implementation lives in the [Goodcabs Travels project](Goodcabs-Travels/README.md), which documents the Bronze, Silver, and Gold transformation layers in detail.

## What's Inside

- [Goodcabs-Travels](Goodcabs-Travels/README.md): end-to-end project documentation for the transportation Lakeflow pipeline.
- [transformations](Goodcabs-Travels/transformations): source code for Bronze, Silver, and Gold processing.

## Repository Layout

```text
miniproject/
├── Goodcabs-Travels/
│   ├── README.md
│   └── transformations/
│       ├── bronze/
│       ├── silver/
│       └── gold/
└── README.md
```

## Quick Start

1. Open [Goodcabs-Travels/README.md](Goodcabs-Travels/README.md) for the full pipeline overview.
2. Review the Bronze, Silver, and Gold folders under [transformations](Goodcabs-Travels/transformations).
3. Configure `start_date` and `end_date` in your DLT pipeline settings before deployment.

## Purpose

The project ingests transportation and trip data, standardizes it through medallion architecture, enriches it with a calendar dimension, and publishes analytics-ready gold tables for downstream reporting.

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

## Data Quality and Governance

- Built with DLT expectations for predictable, testable pipelines.
- Unity Catalog-ready design for secure governance and discoverability.
- Layered model supports clear lineage from raw ingestion to business outputs.

## Future Enhancements

- Add CI/CD for automated deployment and validation.
- Introduce data drift monitoring for trip KPIs.
- Expand Gold models for route-level and demand forecasting analytics.

## Contributing

Contributions are welcome. If you want to improve transformations, add quality rules, or optimize Gold models, open an issue or submit a pull request.
