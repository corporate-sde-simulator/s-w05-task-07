# FINSERV-4207: Investigate GST calculation returning wrong amounts

**Status:** In Progress · **Priority:** Critical
**Sprint:** Sprint 27 · **Story Points:** 8
**Reporter:** Meera Sharma (Tax Compliance Lead) · **Assignee:** You (Intern)
**Due:** End of sprint (Friday)
**Labels:** `backend`, `python`, `tax`, `compliance`
**Task Type:** Code Debugging

---

## Description

The GST calculation engine computes taxes for invoices. Merchants are reporting incorrect tax amounts on their invoices.

**DEBUGGING task — no hint comments. Investigate from symptoms.**

## Symptoms

- Invoice for Rs 1000 with 18% GST shows total as Rs 1000 instead of Rs 1180 (tax not added)
- CGST and SGST should each be 9% for intra-state, but IGST (18%) is being charged instead
- Items with GST exemption (0% rate) still show a tax amount
- Reverse charge mechanism not applying — vendor invoices should charge tax to buyer

## Acceptance Criteria

- [ ] Root cause found and fixed
- [ ] Tax amounts are correct for all scenarios (intra/inter-state, exemptions, reverse charge)
- [ ] All unit tests pass
