from datetime import datetime


def get_city_from_name(name: str) -> str | None:
    try:
        return (
            name
            .split('г.')[1]
            .replace(',', '')
            .replace(' ', '')
        )
    except IndexError:
        return


def get_date_from_str(date: str) -> datetime:
    return datetime.strptime(date, "%d.%m.%Y")
