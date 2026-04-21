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
