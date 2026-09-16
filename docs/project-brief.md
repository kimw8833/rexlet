# Rexlet Project Brief

## Vision

Rexlet is a personal data hub designed to turn fragmented and difficult-to-understand everyday information into reliable, structured, and useful data.

The long-term product may include multiple modules. The first module is **Rexlet Money**.

## Problem

Personal financial information is often fragmented across banks, bills, subscriptions, receipts, and other services.

Bank transaction descriptions can also be difficult to understand and inconsistent. For example:

`MAX STHLM 018392`

may be technically valid transaction data, but the user may understand it better as:

* Merchant: MAX Burgers
* Category: Food
* Subcategory: Restaurants
* Tag: Eating out

Bank-provided categories may also not reflect how an individual user wants to organize personal spending.

## Initial Goal

Rexlet Money will initially focus on transforming messy transaction data into structured, understandable, and reusable financial data.

The first version should allow transaction data to be imported from files, validated, normalized, and categorized according to user-controlled rules.

## Initial Data Sources

The first versions will use:

* Sample transaction data
* CSV imports
* Manually entered information when needed

Direct bank integrations and payment functionality are intentionally excluded from the initial scope.

## Long-Term Direction

Once a reliable data foundation exists, Rexlet Money may later support:

* Spending analysis
* Recurring expenses and subscriptions
* Bills and upcoming payments
* Bill-to-transaction matching
* Savings targets
* Safe-to-spend calculations
* Expense forecasting
* OCR and document extraction
* AI-assisted normalization and categorization
* Natural-language questions about personal financial data

AI should be introduced only when it solves a concrete problem and should operate on top of reliable structured data.

## Engineering Goal

Rexlet should be useful as a real personal product while also demonstrating practical software and data engineering skills, including:

* Python
* SQL
* PostgreSQL
* Data ingestion
* Data modelling
* Data transformation
* Data validation
* Data quality
* APIs
* Automated testing
* Docker
* Documentation
* Maintainable software architecture

The project should remain understandable and finishable rather than adding technologies only for complexity.
