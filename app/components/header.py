import reflex as rx
from app.states.state import RecyclingState


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Recycling Report System",
                class_name="text-2xl font-semibold text-gray-800",
            ),
            rx.el.p(
                "Track and visualize your recycling efforts.",
                class_name="text-gray-500 mt-1",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Total Items Recycled",
                    class_name="text-sm font-medium text-gray-600",
                ),
                rx.el.p(
                    RecyclingState.total_items_recycled,
                    class_name="text-3xl font-bold text-gray-900 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-200 rounded-lg shadow-sm",
            ),
            class_name="grid grid-cols-1",
        ),
        class_name="w-full mb-8",
    )