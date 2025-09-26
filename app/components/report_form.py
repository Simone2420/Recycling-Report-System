import reflex as rx
from app.states.state import RecyclingState


def report_form() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Submit a Report", class_name="text-xl font-semibold text-gray-800 mb-4"
        ),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    "Item Name",
                    html_for="item",
                    class_name="text-sm font-medium text-gray-700 mb-1 block",
                ),
                rx.el.input(
                    id="item",
                    name="item",
                    placeholder="e.g., Water Bottle",
                    class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-purple-500",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Material",
                    html_for="material",
                    class_name="text-sm font-medium text-gray-700 mb-1 block",
                ),
                rx.el.select(
                    rx.foreach(
                        RecyclingState.materials,
                        lambda material: rx.el.option(
                            material.capitalize(), value=material
                        ),
                    ),
                    id="material",
                    name="material",
                    class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-purple-500",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Quantity",
                    html_for="quantity",
                    class_name="text-sm font-medium text-gray-700 mb-1 block",
                ),
                rx.el.input(
                    id="quantity",
                    name="quantity",
                    type="number",
                    placeholder="e.g., 5",
                    class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-purple-500",
                ),
                class_name="mb-6",
            ),
            rx.el.button(
                "Add Report",
                type="submit",
                class_name="w-full bg-gray-900 text-white py-2.5 rounded-lg font-semibold hover:bg-gray-800 transition-colors",
            ),
            on_submit=RecyclingState.add_report,
            reset_on_submit=True,
            class_name="w-full",
        ),
        class_name="p-6 bg-white border border-gray-200 rounded-lg shadow-sm",
    )