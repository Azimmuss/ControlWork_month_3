from db import main_db
import flet as ft


def main(page: ft.Page):
    page.title = 'Product List'
    page.theme_mode = ft.ThemeMode.LIGHT

    job_list = ft.Column(spacing=10)
    filter_type = 'all'

    def load_job():
        job_list.controls.clear()
        for job_id, job_text, completed in main_db.get_jobs(filter_type):
            job_list.controls.append(
                create_job_row(job_id=job_id, job_text=job_text, completed=completed)
            )
        page.update()

    def create_job_row(job_id, job_text, completed):
        job_field = ft.TextField(value=job_text, read_only=True, expand=True)

        checkbox_job = ft.Checkbox(
            value=bool(completed),
            on_change=lambda e: toggle_job(job_id, e.control.value)
        )

        return ft.Row([checkbox_job, job_field])

    def toggle_job(job_id, is_completed):
        main_db.update_job(job_id=job_id, completed=int(is_completed))
        load_job()

    def add_job(_):
        if job_input.value:
            job = job_input.value
            job_id = main_db.add_job(job)

            job_input.value = ""
            load_job()
            page.update()

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_job()

    filter_buttons = ft.Row([
        ft.ElevatedButton('Все', on_click=lambda e: set_filter('all'), icon=ft.Icons.ALL_INBOX),
        ft.ElevatedButton('Невыполненные', on_click=lambda e: set_filter('uncompleted'), icon=ft.Icons.STOP_OUTLINED),
        ft.ElevatedButton('Выполненные', on_click=lambda e: set_filter('completed'), icon=ft.Icons.CHECK_BOX)
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    job_input = ft.TextField(label="Введите продукт", expand=True, on_submit=add_job)
    add_button = ft.IconButton(icon=ft.Icons.SEND, on_click=add_job)

    page.add(
        ft.Row([job_input, add_button]),
        filter_buttons,
        job_list
    )
    load_job()


if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)