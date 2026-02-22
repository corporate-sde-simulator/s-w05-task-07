# PR Review - Tax calculation engine for multi-region (by Vikram Singh)

## Reviewer: Neha Sharma
---

**Overall:** Good foundation but critical bugs need fixing before merge.

### `taxEngine.ts`

> **Bug #1:** Compound tax calculation applies tax-on-tax but uses flat rate instead of compound formula
> This is the higher priority fix. Check the logic carefully and compare against the design doc.

### `regionConfig.ts`

> **Bug #2:** Region matching is case-sensitive so California matches but california returns zero tax
> This is more subtle but will cause issues in production. Make sure to add a test case for this.

---

**Vikram Singh**
> Acknowledged. I have documented the issues for whoever picks this up.
