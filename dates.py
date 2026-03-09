# Note: the datetime module has changed a LOT since Corey's video was filmed on August 2 2016

import datetime # main module when working with dates and times in Python

# Naive dates and times don't have enough info to determine time zones or daylight savings. Aware dates and times do have that info

d = datetime.date(2026, 7, 24)
print(d)

today = datetime.date.today()
print(today.day)
print(today.weekday()) # Monday = 0 Sunday = 6
print(today.isoweekday()) # Monday = 1 Sunday = 7

# Time deltas are the difference between 2 dats or times
tdelta = datetime.timedelta(days=7)
print(today + tdelta)
print(today - tdelta)

# date2 = date1 +/- timedelta
# timedelta = date2 +/- date1

bday = datetime.date(2026, 9, 24)
till_bday = bday - today
print(till_bday.days, till_bday.total_seconds())

# datetime.date works with year, month, day. datetime.time works with hours, minutes, seconds, and microseconds. No year, month, or day or timezone info (so this is still naive)
t = datetime.time(9, 30, 45, 100000) # hours, minutes, seconds, microseconds
print(t)

# datetime.datetime has both the date (year, month, day) and time (hours, minutes, seconds, microseconds)
dt = datetime.datetime(2026, 9, 24, 9, 30, 45, 100000)
print(bday)
print(t)
print(dt)
print(dt.date(), dt.time(), dt.year) # can still access date, time, and fields
print("One week in future:", dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now() # We have the option to pass in a timezone
dt_utcnow = datetime.datetime.utcnow() # Gives UTC time. Deprecated. Use below instead
dt_utcnow2 = datetime.datetime.now(datetime.timezone.utc)
print("dt_today =", dt_today)
print("dt_now =", dt_now)
print("dt_utcnow =", dt_utcnow)
print("dt_utcnow2 =", dt_utcnow2)

import pytz # pytimezone

dt = datetime.datetime(2026, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
print("dt with tzinfo:", dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print("dt_now with tz:", dt_now) # Identical to datetime.datetime.now(datetime.timezone.utc), and similar to datetime.datetime.utcnow() (no +00.00 in utcnow)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print("dt_utcnow replace tzinfo:", dt_utcnow) # identical to datetime.datetime.now(datetime.timezone.utc) since we now have time zone info

dt_central = dt_now.astimezone(pytz.timezone("US/Central"))
print(f"{dt_now} -> {dt_central}")
print(pytz.all_timezones)
# We took a timezone-aware datetime set to UTC and converted to CST

# What if we have naive datetime and we want to make that naive datetime timezone aware?
dt_cst = datetime.datetime.now() # did not pass in timezone, so this is naive datetime
print(dt_cst)

dt_central = dt_cst.astimezone(pytz.timezone("US/Central"))
print(dt_central) # This works now in 2026

cst_tz = pytz.timezone("US/Central")
dt_cst = cst_tz.localize(dt_cst)
print(dt_cst)

dt_central = dt_cst.astimezone(pytz.timezone("US/Central"))
print(dt_central)

print(dt_cst.isoformat())
print(dt_cst.strftime("%B %d, %Y")) # Convert datetime to string, passing in format

dt_str = "March 08, 2026"
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y") # Convert string to datetime, passing in format
print(dt)