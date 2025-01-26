from exceptions.crawler_error import CrawlerError


class InvalidFieldError(CrawlerError):
    def __init__(self, field_name: str, force_message=False) -> None:
        if force_message:
            super().__init__(field_name)
        else:
            super().__init__(f"The field {field_name} is invalid")
