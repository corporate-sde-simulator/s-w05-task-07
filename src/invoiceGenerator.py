"""
Invoice Generator — generates tax invoices in standard GST format.

Author: Meera Sharma (Tax team)
Last Modified: 2026-03-05
"""

from typing import Dict, List, Optional
from datetime import datetime


class InvoiceGenerator:
    def __init__(self, tax_calculator):
        self.calculator = tax_calculator
        self.invoice_counter = 0

    def generate(self, seller: Dict, buyer: Dict, items: List[Dict],
                 reverse_charge: bool = False) -> Dict:
        """Generate a complete GST invoice."""
        self.invoice_counter += 1
        from taxCalculator import TaxLineItem

        tax_items = [
            TaxLineItem(
                description=item['description'],
                amount=item['amount'],
                gst_rate=item.get('gst_rate', 18),
                hsn_code=item.get('hsn_code', ''),
                exempt=item.get('exempt', False),
            )
            for item in items
        ]

        calculation = self.calculator.calculate_invoice(
            tax_items,
            seller.get('state', ''),
            buyer.get('state', ''),
            reverse_charge,
        )

        invoice = {
            'invoice_number': f"INV-{datetime.utcnow().strftime('%Y%m%d')}-{self.invoice_counter:04d}",
            'date': datetime.utcnow().isoformat(),
            'seller': seller,
            'buyer': buyer,
            'reverse_charge': reverse_charge,
            **calculation,
        }

        return invoice

    def format_for_print(self, invoice: Dict) -> str:
        """Format invoice for text printing."""
        lines = [
            f"Invoice: {invoice['invoice_number']}",
            f"Date: {invoice['date'][:10]}",
            f"Seller: {invoice['seller'].get('name', '')} (GSTIN: {invoice['seller'].get('gstin', '')})",
            f"Buyer: {invoice['buyer'].get('name', '')} (GSTIN: {invoice['buyer'].get('gstin', '')})",
            "",
            "Items:",
        ]

        for item in invoice['line_items']:
            lines.append(f"  {item['description']}: Rs {item['taxable_amount']} @ {item['gst_rate']}%")

        lines.append("")
        lines.append(f"Subtotal: Rs {invoice['subtotal']}")
        if invoice['is_intra_state']:
            lines.append(f"CGST: Rs {invoice['cgst_total']}")
            lines.append(f"SGST: Rs {invoice['sgst_total']}")
        else:
            lines.append(f"IGST: Rs {invoice['igst_total']}")
        lines.append(f"Tax Total: Rs {invoice['tax_total']}")
        lines.append(f"Grand Total: Rs {invoice['grand_total']}")

        return '\n'.join(lines)
