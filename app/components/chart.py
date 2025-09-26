import reflex as rx
from app.states.state import RecyclingState


def recycling_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Recycling Summary", class_name="text-xl font-semibold text-gray-800 mb-4"
        ),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(
                stroke_dasharray="3 3", horizontal=True, vertical=False
            ),
            rx.recharts.x_axis(data_key="name", stroke_width="1"),
            rx.recharts.y_axis(stroke_width="1"),
            rx.recharts.tooltip(cursor={"fill": "rgba(200, 200, 200, 0.2)"}),
            rx.recharts.bar(data_key="quantity", fill="#8884d8"),
            data=RecyclingState.material_summary,
            height=300,
            class_name="font-sans",
        ),
        class_name="p-6 bg-white border border-gray-200 rounded-lg shadow-sm",
    )