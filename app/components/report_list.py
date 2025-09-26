import reflex as rx
from app.states.state import RecyclingState


def report_list() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Recent Reports", class_name="text-xl font-semibold text-gray-800 mb-4"
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Item",
                            class_name="px-4 py-2 text-left text-sm font-semibold text-gray-600",
                        ),
                        rx.el.th(
                            "Material",
                            class_name="px-4 py-2 text-left text-sm font-semibold text-gray-600",
                        ),
                        rx.el.th(
                            "Quantity",
                            class_name="px-4 py-2 text-right text-sm font-semibold text-gray-600",
                        ),
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        RecyclingState.reports,
                        lambda report: rx.el.tr(
                            rx.el.td(
                                report["item"],
                                class_name="px-4 py-3 border-t border-gray-200 text-sm text-gray-700",
                            ),
                            rx.el.td(
                                report["material"].capitalize(),
                                class_name="px-4 py-3 border-t border-gray-200 text-sm text-gray-700",
                            ),
                            rx.el.td(
                                report["quantity"],
                                class_name="px-4 py-3 border-t border-gray-200 text-sm text-gray-700 text-right",
                            ),
                            class_name="hover:bg-gray-50 transition-colors",
                        ),
                    )
                ),
                class_name="w-full",
            ),
            rx.cond(
                RecyclingState.reports.length() == 0,
                rx.el.div(
                    "No reports yet. Add one using the form.",
                    class_name="text-center text-gray-500 py-10",
                ),
            ),
            class_name="overflow-x-auto",
        ),
        class_name="p-6 bg-white border border-gray-200 rounded-lg shadow-sm mt-8",
    )