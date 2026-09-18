# Rexlet Money v0.1 — CSV Data Contract

## Purpose

This document defines the expected input contract for the first CSV transaction source supported by Rexlet Money v0.1.

The contract describes the required source fields, expected formats, validation rules, and the boundary between source data validation and later transaction enrichment.

A transaction does not need to be understood or classified by Rexlet in order to be valid.

## Core Principle

Rexlet separates **source facts** from **Rexlet interpretation**.

For example, a source may provide:

`UNKNOWN SHOP 48291`

Rexlet preserves this value as the original transaction description.

The transaction may initially have no normalized Merchant:

```text
raw_description = "UNKNOWN SHOP 48291"
merchant = null
classification_status = "unclassified"
```

This is still a valid transaction.

Later, the user or a classification rule may associate the transaction with a normalized Merchant.

For example:

```text
raw_description = "UNKNOWN SHOP 48291"
merchant = "ABC Convenience Store"
```

The original source description must remain unchanged.

## Required Source Columns

The first supported CSV format must contain the following columns:

| Source Column | Required | Rexlet Internal Field | Description                                      |
| ------------- | -------- | --------------------- | ------------------------------------------------ |
| `Date`        | Yes      | `transaction_date`    | Date of the transaction                          |
| `Description` | Yes      | `raw_description`     | Original transaction description from the source |
| `Amount`      | Yes      | `amount`              | Transaction amount                               |
| `Currency`    | Yes      | `currency`            | Currency used by the transaction                 |

## Field Rules

### `Date`

Expected source format:

`YYYY-MM-DD`

Example:

`2026-09-12`

Rules:

* Must not be empty.
* Must represent a valid calendar date.
* Rexlet converts the source value into an internal date type.

Invalid examples:

* empty value
* `2026-13-40`
* `not-a-date`

---

### `Description`

Examples:

`MAX STHLM 018392`

`UNKNOWN SHOP 48291`

Rules:

* Must not be empty.
* The original value must be preserved as `raw_description`.
* The value does not need to match an existing Merchant in Rexlet.
* Rexlet must not modify the original description when merchant normalization occurs.

A source description is considered valid even when Rexlet does not yet understand what merchant it represents.

For example:

```text
raw_description = "UNKNOWN SHOP 48291"
merchant = null
```

is valid.

The transaction may be reviewed and enriched by the user later.

---

### `Amount`

Examples:

`-149.00`

`32000.00`

Rules:

* Must not be empty.
* Must represent a valid numeric amount.
* Negative values represent outgoing money.
* Positive values represent incoming money.
* Rexlet should use a decimal representation suitable for financial values rather than binary floating-point arithmetic.

Invalid examples:

* `not-a-number`
* empty value

---

### `Currency`

Examples:

`SEK`

`sek`

Rules:

* Must not be empty.
* Alphabetic values are normalized to uppercase.
* For example, `sek` becomes `SEK`.
* Currency validation in v0.1 is intentionally simple.

More comprehensive currency validation may be introduced later if product requirements justify it.

## Source-to-Internal Mapping

| CSV Source Column | Rexlet Internal Field |
| ----------------- | --------------------- |
| `Date`            | `transaction_date`    |
| `Description`     | `raw_description`     |
| `Amount`          | `amount`              |
| `Currency`        | `currency`            |

The source schema and Rexlet's internal data model are intentionally separated.

Future source formats may use different column names while still producing the same Rexlet internal representation.

## Validation vs Enrichment

Validation determines whether source data can safely become a Rexlet Transaction.

Enrichment adds additional meaning to an already valid Transaction.

Example:

```text
Date: 2026-09-07
Description: UNKNOWN SHOP 48291
Amount: -87.50
Currency: SEK
```

This record may pass validation because all required source fields are valid.

After ingestion:

```text
transaction_date = 2026-09-07
raw_description = "UNKNOWN SHOP 48291"
amount = -87.50
currency = "SEK"

merchant = null
category = null
subcategory = null
classification_status = "unclassified"
```

The transaction can later be enriched with:

```text
merchant = "ABC Convenience Store"
category = "Food"
subcategory = "Groceries"
classification_status = "classified"
```

Validation must not fail merely because Merchant, Category, or Subcategory is unknown.

## Valid Record Example

Source:

```text
2026-09-12,MAX STHLM 018392,-149.00,SEK
```

After source validation:

```text
transaction_date = 2026-09-12
raw_description = "MAX STHLM 018392"
amount = -149.00
currency = "SEK"
```

Merchant normalization may happen later.

For example:

```text
merchant = "MAX Burgers"
```

The value:

```text
raw_description = "MAX STHLM 018392"
```

must remain unchanged.

## Invalid Record Example

Source:

```text
2026-09-12,MAX STHLM 018392,not-a-number,SEK
```

The record fails validation because `Amount` cannot be converted into a valid financial amount.

The record must not silently enter Rexlet's trusted transaction dataset as a valid Transaction.

## v0.1 Scope

This contract applies only to the first sample CSV format supported by Rexlet Money.

The initial implementation will focus on making this single source format reliable before introducing configurable mappings or additional financial data sources.

Additional source formats should be handled by the ingestion layer while producing the same Rexlet internal Transaction representation.
