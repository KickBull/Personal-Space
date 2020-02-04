import datetime


def timestamp(time: datetime, extra_seconds: int = 0, format="hour:minute am_or_pm, month day"):
    """Makes a datetime object prettier.

    time: datetime object to convert to a pretty timestamp.
    extra_seconds: seconds to add to the date. (default: 0)[optional]
    format: the format in which to return the prettified date. (default: "hour:minute am_or_pm, month day")[optional]

    supported format parts:
    second,
    minute,
    hour,
    day - with st/nd/rd/th added to the end of it depending on the number,
    month,
    year,
    am_or_pm - "AM" or "PM" depending on the hour.
    Basically those keywords get replaced with the actual day/month/year/etc

    Examples:
    "hour:minute am_or_pm, month day" -> "11:25 AM, February 3rd"
    "year, month day" -> "2020, February 3rd"
    "It's the day of month right now" -> "It's the 3rd of February right now"
    """

    # adding the extra seconds
    dummydate = datetime.datetime(year=100, month=time.month, day=time.day, hour=time.hour, minute=time.minute)
    dummydate += datetime.timedelta(seconds=extra_seconds)

    second = dummydate.second
    minute = f"0{dummydate.minute}" if len(str(dummydate.minute)) == 1 else dummydate.minute
    hour = dummydate.hour
    day = dummydate.day
    month = dummydate.month
    year = time.year

    # prettifying different parts of the date
    months = {
              1: "January",
              2: "February",
              3: "March",
              4: "April",
              5: "May",
              6: "June",
              7: "July",
              8: "August",
              9: "September",
              10: "October",
              11: "November",
              12: "December"
    }

    ordinal_ends = {
                    1: "st",
                    2: "nd",
                    3: "rd",
                    11: "th"
    }

    if day in (11, 12, 13):
        ordinal_end = "th"
    elif int(str(day)[-1]) <= 3:
        ordinal_end = ordinal_ends[int(str(day)[-1])]
    else:
        ordinal_end = "th"

    if hour <= 11:
        am_or_pm = "AM"
    elif hour >= 12:
        am_or_pm = "PM"

    # adding all the parts together in the desired format
    parts = {
        "second": second,
        "minute": minute,
        "hour": hour,
        "am_or_pm": am_or_pm,
        "day": f"{day}{ordinal_end}",
        "month": months[month],
        "year": year,
    }

    for part in parts:
        format = format.replace(part, str(parts[part]))

    return format
