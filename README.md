# qa_guru_lecture_14
REST API. Part 1. Requests
Документация по pytest-voluptuous https://github.com/F-Secure/pytest-voluptuous
Документация по voluptuous https://github.com/alecthomas/voluptuous
Документация по Requests https://requests.readthedocs.io/en/latest/

Если нужно отметить обязательные поля в схеме
from voluptuous.schema_builder import Required

single_user_schema = Schema(
        {
            "data":
                {
                    Required("id"): int,
                    Required("email"): str,
                    "first_name": str,
                    "last_name": str,
                    "avatar": str
                },
            "support":
                {
                    "url": str,
                    "text": str
                },
        },
        required=False,
        extra=PREVENT_EXTRA
)

Также в схеме можно отмечать необязательные (Optional) поля
