

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
