import reflex as rx
from typing import TypedDict
import logging


class Report(TypedDict):
    item: str
    material: str
    quantity: int


class RecyclingState(rx.State):
    reports: list[Report] = []
    materials: list[str] = ["plastic", "glass", "metal", "paper"]

    @rx.event
    def add_report(self, form_data: dict):
        try:
            quantity = int(form_data.get("quantity", 0))
            if quantity <= 0:
                return rx.toast("Quantity must be a positive number.", duration=3000)
            new_report = Report(
                item=form_data["item"],
                material=form_data["material"],
                quantity=quantity,
            )
            self.reports.append(new_report)
        except (ValueError, KeyError) as e:
            logging.exception(f"Error adding report: {e}")
            return rx.toast(
                "Invalid form data. Please check your inputs.", duration=3000
            )

    @rx.var
    def total_items_recycled(self) -> int:
        return sum((report["quantity"] for report in self.reports))

    @rx.var
    def material_summary(self) -> list[dict[str, str | int]]:
        summary: dict[str, int] = {material: 0 for material in self.materials}
        for report in self.reports:
            if report["material"] in summary:
                summary[report["material"]] += report["quantity"]
        return [
            {"name": material, "quantity": qty} for material, qty in summary.items()
        ]