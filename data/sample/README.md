# Sample Transaction Data

This directory contains synthetic transaction data used for development and testing of Rexlet Money.

The files do not contain real personal financial information.

## Files

### `transactions.csv`

Contains valid sample transaction records.

It is intended to represent a simple source CSV that Rexlet Money v0.1 should be able to ingest successfully.

The dataset includes examples such as:

* Merchant descriptions that require normalization
* Expenses
* Income
* Unknown merchants
* Different future classification use cases

### `transactions_invalid.csv`

Contains intentionally invalid transaction records.

It is used to test Rexlet's data validation behaviour.

The file currently includes examples of:

* Missing transaction date
* Invalid amount
* Missing description
* Missing currency

These records should not silently enter Rexlet's trusted transaction dataset.

## Privacy

All data in this directory is synthetic and created for development purposes.

Real bank statements, account information, personal identifiers, credentials, or other sensitive financial information must not be committed to this repository.
