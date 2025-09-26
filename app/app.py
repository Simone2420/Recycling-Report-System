import reflex as rx
from app.components.header import header
from app.components.report_form import report_form
from app.components.chart import recycling_chart
from app.components.report_list import report_list


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            header(),
            rx.el.div(
                report_form(), recycling_chart(), class_name="grid md:grid-cols-2 gap-8"
            ),
            report_list(),
            class_name="max-w-4xl mx-auto p-4 md:p-8",
        ),
        class_name="font-['Open_Sans'] bg-gray-50 min-h-screen",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="Recycling Report")