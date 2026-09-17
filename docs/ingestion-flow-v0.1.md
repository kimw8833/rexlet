# Rexlet Money v0.1 — Transaction Ingestion Flow

## Purpose

This document describes how Rexlet Money v0.1 will ingest transaction data from CSV files and transform source-specific data into a consistent internal transaction format.

The ingestion process should preserve the original source information, validate incoming data, and prevent invalid records from silently entering the trusted transaction dataset.

## Core Principle

External data formats should not define Rexlet's internal data model.

Different banks or financial sources may provide different column names, formats, and levels of detail.

Rexlet should convert supported source formats into one consistent internal representation.

Example source A:

```text
Bokföringsdag,Text,Belopp
2026-09-12,MAX STHLM 018392,-149.00
```

Example source B:

```text
Date,Description,Amount,Currency
2026-09-12,MAX STHLM 018392,-149.00,SEK
```

Both may eventually become:

```text
transaction_date = 2026-09-12
amount = -149.00
currency = SEK
raw_description = "MAX STHLM 018392"
```

## Ingestion Flow

```text
CSV file
    ↓
Read source data
    ↓
Map source columns
    ↓
Validate required values
    ↓
Normalize basic data types
    ↓
Create ImportBatch
    ↓
Create Transactions
    ↓
Apply classification rules
    ↓
Store structured transaction data
```

## Step 1 — Read Source Data

Rexlet receives a CSV file containing transaction records.

The original file should be treated as source data.

Rexlet must not modify the source file during ingestion.

## Step 2 — Map Source Columns

Source-specific column names are mapped to Rexlet's internal fields.

Example:

| Source column | Rexlet field     |
| ------------- | ---------------- |
| Bokföringsdag | transaction_date |
| Text          | raw_description  |
| Belopp        | amount           |

Column mapping allows Rexlet to support different CSV formats without changing the internal Transaction model.

## Step 3 — Validate Required Data

Before creating trusted Transaction records, Rexlet must validate required fields.

For v0.1, the minimum required information is:

* Transaction date
* Amount
* Currency
* Raw description

Examples of invalid input include:

* Missing transaction date
* Invalid amount
* Missing description
* Unsupported or invalid currency value

Invalid records must be identified rather than silently accepted.

## Step 4 — Normalize Basic Data Types

Source values should be converted into consistent internal types.

Examples:

```text
"2026-09-12"
→ date
```

```text
"-149.00"
→ decimal amount
```

```text
"sek"
→ "SEK"
```

This step concerns technical normalization of data representation.

Merchant normalization and transaction classification occur later.

## Step 5 — Create Import Batch

Each successful import operation creates an ImportBatch.

Example:

```text
ImportBatch
source_filename = "transactions_september.csv"
imported_at = <timestamp>
```

Transactions created from this import reference the same ImportBatch.

This provides traceability between stored transactions and their source import.

## Step 6 — Create Transactions

Validated source records are transformed into Rexlet Transaction records.

The original transaction description is preserved.

Example:

```text
transaction_date = 2026-09-12
amount = -149.00
currency = SEK
raw_description = "MAX STHLM 018392"
classification_status = "unclassified"
```

No merchant or category needs to be known at this stage.

## Step 7 — Apply Classification Rules

After the transaction has been successfully ingested, Rexlet may attempt to apply existing ClassificationRules.

Example:

```text
raw_description contains "MAX"
```

may produce:

```text
merchant = MAX Burgers
category = Food
subcategory = Restaurants
classification_status = classified
```

If no rule matches, the Transaction remains unclassified.

If conflicting rules match, the Transaction should be marked for review rather than silently classified.

## Step 8 — Store Structured Data

Successfully processed Transactions are stored in Rexlet's database.

The resulting data should maintain:

* Source traceability
* Original raw description
* Valid internal data types
* Classification state
* Relationships to normalized entities

## Error Handling

Invalid records should not silently enter the trusted transaction dataset.

For v0.1, Rexlet should clearly identify records that fail validation.

The exact technical implementation of rejected records will be decided during implementation.

Possible later approaches include:

* Rejecting the entire import
* Accepting valid rows while reporting invalid rows
* Storing rejected rows separately for review

This decision is intentionally left open until implementation requirements are clearer.

## v0.1 Boundary

The first ingestion implementation will support one defined CSV format using sample data.

Support for additional banks or configurable source mappings should be added only after the first ingestion pipeline works reliably.

This keeps the first implementation small while preserving an architecture that can support additional sources later.
