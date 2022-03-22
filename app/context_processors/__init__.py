from os import getenv
import datetime


def utility_text_processors():
    message = "Thank You For Visiting"

    def deployment_environment():
        return getenv('FLASK_ENV', None)

    def current_year():
        currentdatetime = datetime.datetime.now()
        date = currentdatetime.date()
        year = date.strftime("%Y")
        return year

    def format_price(amount, currency="$"):
        return f"{currency}{amount:.2f}"

    return dict(
        mymessage=message,
        deployment_environment=deployment_environment(),
        year=current_year(),
        format_price=format_price
    )
