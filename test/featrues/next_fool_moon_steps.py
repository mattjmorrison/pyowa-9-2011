from lettuce import step, world
from mattspackage.next_full_moon import next_full_moon

@step(u'Given today is "(.*)"')
def given_todays_date(step, date):
    world.date = date

@step(u"When I call next_full_moon with today's date")
def when_i_call_next_full_moon_with_today_s_date(step):
    world.next_full_moon_date = next_full_moon(world.date)

@step(u'Then the result should be "(.*)"')
def then_the_result_should_be_expected_date(step, expected_date):
    assert world.next_full_moon_date == expected_date, "%s != %s" % (world.next_full_moon_date, expected_date)
