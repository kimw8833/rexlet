# Rexlet Money v0.1 Requirements

## Purpose

Rexlet Money v0.1 establishes the first reliable data foundation for personal transaction data.

The goal of this version is to transform raw transaction data into structured and user-understandable information while preserving the original source data.

## Functional Requirements

### FR-001 — Import transactions from CSV

The system shall allow transaction data to be imported from a CSV file.

At minimum, an imported transaction must provide:

* Transaction date
* Amount
* Currency
* Raw transaction description

### FR-002 — Preserve source transaction data

The system shall preserve the original transaction description received from the source.

Normalization and classification must not overwrite the original raw description.

### FR-003 — Validate imported transaction data

The system shall validate imported transaction records before they are accepted.

Invalid or incomplete records shall be identified rather than silently accepted as valid data.

### FR-004 — Normalize merchants

The system shall allow raw transaction descriptions to be associated with a normalized merchant.

Example:

`MAX STHLM 018392`

may be associated with:

`MAX Burgers`

Multiple raw transaction descriptions may refer to the same merchant.

### FR-005 — Classify transactions

The system shall allow transactions to be classified using:

* Category
* Optional subcategory
* Optional tags

Categories and subcategories shall be controlled by the user rather than being limited to fixed bank-provided categories.

### FR-006 — Apply reusable classification rules

The system shall allow reusable rules to classify future transactions based on their raw transaction data.

The initial supported matching operations shall be:

* Exact match
* Contains
* Starts with

A rule may assign:

* Merchant
* Category
* Subcategory
* Tags

### FR-007 — Identify transactions requiring review

Transactions that cannot be classified automatically shall remain available for manual review.

If multiple conflicting rules match the same transaction, the system shall not silently choose an arbitrary result.

### FR-008 — View structured transactions

The system shall allow the user to view imported transactions together with their normalized and classified information.

The user shall be able to distinguish between the original source description and the normalized merchant information.

## Data and Quality Requirements

### DQ-001 — Traceability

Rexlet shall retain enough information to determine which import operation introduced a transaction.

### DQ-002 — Deterministic rule processing

Given the same transaction data and the same set of classification rules, Rexlet shall produce the same classification result.

### DQ-003 — Data integrity

Relationships between transactions, merchants, categories, subcategories, and tags shall remain internally consistent.

For example, a subcategory belonging to `Transport` must not be assigned together with the category `Food`.

### DQ-004 — Testability

Core ingestion, validation, normalization, and classification behaviour shall be covered by automated tests.

## Out of Scope for v0.1

The following features are intentionally excluded from Rexlet Money v0.1:

* Direct bank connections
* Open Banking integrations
* BankID
* Payment functionality
* Bills and payment tracking
* Subscription detection
* Spending forecasting
* Savings goals
* Safe-to-spend calculations
* OCR
* AI-based classification
* Natural-language financial assistant
* Complex frontend development

These capabilities may be considered in later versions after the transaction data foundation is reliable.
