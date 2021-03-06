#########################################################################
#
#   Astronomy Club Event Generator
#   file: test.py
#
#   Copyright (C) 2016  Teruo Utsumi, San Jose Astronomical Association
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   Contributors:
#       2016-02-25  Teruo Utsumi, initial code
#
#########################################################################

import sys
import datetime
import pdb

from   cal_const  import *
import cal_events
import cal_ephemeris

year  = 0
cal   = None
start = None
end   = None

locations = { 1 : "Houge Park, Blg. 1",  # indoor
              2 : "Houge Park",          # outdoor
              3 : "Rancho Cañada del Oro",
              4 : "Mendoza Ranch",
              5 : "Coyote Valley",
              6 : "Pinnacles Nat'l Park, East Side",
              7 : "Pinnacles Nat'l Park, West Side",
              8 : "Yosemite Nat'l Park, Glacier Point" }


class_intro = cal_events.EventType()
class_intro.type_id          = 1
class_intro.name             = 'Intro to the Night Sky'
class_intro.tentative        = False
class_intro.visibility       = EventVisibility.public
class_intro.coordinator_id   = 1
class_intro.location         = locations[1]
class_intro.repeat           = EventRepeat.lunar
class_intro.lunar_phase      = RuleLunar.moon_1q
class_intro.day_of_week      = RuleWeekday.friday
class_intro.rule_start_time  = RuleStartTime.nautical
class_intro.time_earliest    = datetime.time(19, 0, 0)
class_intro.time_offset      = datetime.timedelta(hours=-1)
class_intro.time_length      = datetime.timedelta(hours=1)
class_intro.url              = 'www.sjaa.net/programs/beginners-astronomy'
class_intro.notes            = ''

class_101 = cal_events.EventType()
class_101.type_id            = 2
class_101.name               = 'Astronomy 101'
class_101.tentative          = False
class_101.visibility         = EventVisibility.public
class_101.coordinator_id     = 1
class_101.location           = locations[1]
class_101.repeat             = EventRepeat.lunar
class_101.lunar_phase        = RuleLunar.moon_3q
class_101.day_of_week        = RuleWeekday.friday
class_101.rule_start_time    = RuleStartTime.nautical
class_101.time_earliest      = datetime.time(19, 0, 0)
class_101.time_offset        = datetime.timedelta(hours=-1)
class_101.time_length        = datetime.timedelta(hours=1)
class_101.url                = 'www.sjaa.net/programs/beginners-astronomy'
class_101.notes              = ''

itsp_1q = cal_events.EventType()
itsp_1q.type_id              = 3
itsp_1q.name                 = 'In-town Star Party'
itsp_1q.tentative            = False
itsp_1q.visibility           = EventVisibility.public
itsp_1q.coordinator_id       = 1
itsp_1q.location             = locations[2]
itsp_1q.repeat               = EventRepeat.lunar
itsp_1q.lunar_phase          = RuleLunar.moon_1q
itsp_1q.day_of_week          = RuleWeekday.friday
itsp_1q.rule_start_time      = RuleStartTime.nautical
# set 1 second so classes get scheduled before ITSP
itsp_1q.time_earliest        = datetime.time(19, 0, 1)
itsp_1q.time_offset          = datetime.timedelta(hours=0)
itsp_1q.time_length          = datetime.timedelta(hours=2)
itsp_1q.url                  = 'www.sjaa.net/events/monthly-star-parties'
itsp_1q.notes                = '1st quarter moon ITSP'

itsp_3q = cal_events.EventType()
itsp_3q.type_id              = 4
itsp_3q.name                 = 'In-town Star Party'
itsp_3q.tentative            = False
itsp_3q.visibility           = EventVisibility.public
itsp_3q.coordinator_id       = 1
itsp_3q.location             = locations[2]
itsp_3q.repeat               = EventRepeat.lunar
itsp_3q.lunar_phase          = RuleLunar.moon_3q
itsp_3q.day_of_week          = RuleWeekday.friday
itsp_3q.rule_start_time      = RuleStartTime.nautical
# set 1 second so classes get scheduled before ITSP
itsp_3q.time_earliest        = datetime.time(19, 0, 1)
itsp_3q.time_offset          = datetime.timedelta(hours=0)
itsp_3q.time_length          = datetime.timedelta(hours=2)
itsp_3q.url                  = 'www.sjaa.net/events/monthly-star-parties'
itsp_3q.notes                = '3rd quarter moon ITSP'

dark_sky = cal_events.EventType()
dark_sky.type_id             = 5
dark_sky.name                = 'Dark Sky Night'
dark_sky.visibility          = EventVisibility.member
dark_sky.coordinator_id      = 1
dark_sky.location            = locations[4]
dark_sky.repeat              = EventRepeat.lunar
dark_sky.lunar_phase         = RuleLunar.moon_new
dark_sky.day_of_week         = RuleWeekday.saturday
dark_sky.rule_start_time     = RuleStartTime.civil
dark_sky.time_offset         = datetime.timedelta(hours=0)
dark_sky.time_length         = datetime.timedelta(hours=4)
dark_sky.url                 = 'www.sjaa.net/dark-sky-nights??'
dark_sky.notes               = ''

quick_start = cal_events.EventType()
quick_start.type_id          = 6
quick_start.name             = 'Quick STARt'
quick_start.visibility       = EventVisibility.private
quick_start.private          = True
quick_start.hide_location    = True
quick_start.coordinator_id   = 1
quick_start.location         = locations[1]
quick_start.repeat           = EventRepeat.lunar
quick_start.lunar_phase      = RuleLunar.moon_1q
quick_start.day_of_week      = RuleWeekday.saturday
quick_start.rule_start_time  = RuleStartTime.absolute
quick_start.time_start       = datetime.time(hour=19)
quick_start.time_length      = datetime.timedelta(hours=3)
quick_start.url              = 'www.sjaa.net/programs/quick-start'
quick_start.email            = 'joe@null.dev'
quick_start.notes            = ''

solar_sunday = cal_events.EventType()
solar_sunday.type_id         = 7
solar_sunday.name            = 'Solar Sunday'
solar_sunday.visibility      = EventVisibility.public
solar_sunday.coordinator_id  = 1
solar_sunday.location        = locations[1]
solar_sunday.repeat          = EventRepeat.monthly
solar_sunday.week            = RuleWeek.week_1
solar_sunday.day_of_week     = RuleWeekday.sunday
solar_sunday.rule_start_time = RuleStartTime.absolute
solar_sunday.time_start      = datetime.time(hour=14)
solar_sunday.time_length     = datetime.timedelta(hours=2)
solar_sunday.url             = 'www.sjaa.net/solar-observing??'
solar_sunday.notes           = ''

fix_it = cal_events.EventType()
fix_it.type_id               = 8
fix_it.name                  = 'Fix It'
fix_it.visibility            = EventVisibility.public
fix_it.coordinator_id        = 1
fix_it.location              = locations[2]
fix_it.repeat                = EventRepeat.monthly
fix_it.week                  = RuleWeek.week_1
fix_it.day_of_week           = RuleWeekday.sunday
fix_it.rule_start_time       = RuleStartTime.absolute
fix_it.time_start            = datetime.time(hour=14)
fix_it.time_length           = datetime.timedelta(hours=2)
fix_it.url                   = 'www.sjaa.net/programs/fix-it'
fix_it.notes                 = ''

board_mtg = cal_events.EventType()
board_mtg.type_id            = 9
board_mtg.name               = 'Board Meeting'
board_mtg.visibility         = EventVisibility.member
board_mtg.coordinator_id     = 1
board_mtg.location           = locations[1]
board_mtg.repeat             = EventRepeat.lunar
board_mtg.lunar_phase        = RuleLunar.moon_full
board_mtg.day_of_week        = RuleWeekday.saturday
board_mtg.rule_start_time    = RuleStartTime.absolute
board_mtg.time_start         = datetime.time(hour=18)
board_mtg.time_length        = datetime.timedelta(hours=1.5)
board_mtg.url                = 'www.sjaa.net/board-meeting??'
board_mtg.notes              = ''

gen_mtg = cal_events.EventType()
gen_mtg.type_id              = 10
gen_mtg.name                 = 'General Meeting'
gen_mtg.visibility           = EventVisibility.public
gen_mtg.coordinator_id       = 1
gen_mtg.location             = locations[1]
gen_mtg.repeat               = EventRepeat.lunar
gen_mtg.lunar_phase          = RuleLunar.moon_full
gen_mtg.day_of_week          = RuleWeekday.saturday
gen_mtg.rule_start_time      = RuleStartTime.absolute
gen_mtg.time_start           = datetime.time(hour=19, minute=30)
gen_mtg.time_length          = datetime.timedelta(hours=2)
gen_mtg.url                  = 'www.sjaa.net/programs/monthly-guest-speakers'
gen_mtg.notes                = ''

starry_night = cal_events.EventType()
starry_night.type_id         = 11
starry_night.name            = 'Starry Night (OSA)'
starry_night.visibility      = EventVisibility.public
starry_night.coordinator_id  = 1
starry_night.location        = locations[3]
starry_night.repeat          = EventRepeat.lunar
starry_night.lunar_phase     = RuleLunar.moon_3q
starry_night.day_of_week     = RuleWeekday.saturday
starry_night.rule_start_time = RuleStartTime.civil
starry_night.time_offset     = datetime.timedelta(hours=0)
starry_night.time_length     = datetime.timedelta(hours=2)
starry_night.url             = 'www.sjaa.net/events/starry-nights-public-star-party/'
starry_night.notes           = ''

image_sig = cal_events.EventType()
image_sig.type_id            = 12
image_sig.name               = 'Imaging SIG'
image_sig.visibility         = EventVisibility.public
image_sig.coordinator_id     = 1
image_sig.location           = locations[1]
image_sig.repeat             = EventRepeat.monthly
image_sig.week               = RuleWeek.week_3
image_sig.day_of_week        = RuleWeekday.tuesday
image_sig.rule_start_time    = RuleStartTime.absolute
image_sig.time_start         = datetime.time(hour=19, minute=30)
image_sig.time_length        = datetime.timedelta(hours=2)
image_sig.url                = 'www.sjaa.net/programs/imaging-sig'
image_sig.notes              = ''

mem_mtg = cal_events.EventType()
mem_mtg.type_id              = 13
mem_mtg.name                 = '*Membership Meeting/Awards Night'
mem_mtg.visibility           = EventVisibility.public
mem_mtg.coordinator_id       = 1
mem_mtg.location             = locations[1]
mem_mtg.repeat               = EventRepeat.annual
mem_mtg.lunar_phase          = RuleLunar.moon_full
mem_mtg.day_of_week          = RuleWeekday.saturday
mem_mtg.rule_start_time      = RuleStartTime.absolute
mem_mtg.month                = 2
mem_mtg.time_start           = datetime.time(hour=19, minute=30)
mem_mtg.time_length          = datetime.timedelta(hours=2)
mem_mtg.url                  = 'www.sjaa.net/membership-meeting??'
mem_mtg.notes                = ''

swap_spring = cal_events.EventType()
swap_spring.type_id          = 14
swap_spring.name             = '*Spring Swap Meet'
swap_spring.visibility       = EventVisibility.public
swap_spring.coordinator_id   = 1
swap_spring.location         = locations[1]
swap_spring.repeat           = EventRepeat.annual
swap_spring.lunar_phase      = RuleLunar.moon_full
swap_spring.day_of_week      = RuleWeekday.sunday
swap_spring.rule_start_time  = RuleStartTime.absolute
swap_spring.month            = 3
swap_spring.time_start       = datetime.time(hour=11)
swap_spring.time_length      = datetime.timedelta(hours=4)
swap_spring.url              = 'www.sjaa.net/events/swap-meet'
swap_spring.notes            = ''

movie_night = cal_events.EventType()
movie_night.type_id          = 15
movie_night.name             = '*Movie Night'
movie_night.visibility       = EventVisibility.member
movie_night.coordinator_id   = 1
movie_night.location         = locations[1]
movie_night.repeat           = EventRepeat.annual
movie_night.lunar_phase      = RuleLunar.moon_full
movie_night.day_of_week      = RuleWeekday.saturday
movie_night.rule_start_time  = RuleStartTime.absolute
movie_night.month            = 8
movie_night.time_start       = datetime.time(hour=19, minute=30)
movie_night.time_length      = datetime.timedelta(hours=3)
movie_night.url              = 'www.sjaa.net/movie-night'
movie_night.notes            = "Don't publicize title on public media like Meetup!"

show_n_tell = cal_events.EventType()
show_n_tell.type_id          = 16
show_n_tell.name             = '*Show-n-tell'
show_n_tell.visibility       = EventVisibility.public
show_n_tell.coordinator_id   = 1
show_n_tell.location         = locations[1]
show_n_tell.repeat           = EventRepeat.annual
show_n_tell.lunar_phase      = RuleLunar.moon_full
show_n_tell.day_of_week      = RuleWeekday.saturday
show_n_tell.rule_start_time  = RuleStartTime.absolute
show_n_tell.month            = 9
show_n_tell.time_start       = datetime.time(hour=19, minute=30)
show_n_tell.time_length      = datetime.timedelta(hours=2)
show_n_tell.url              = 'www.sjaa.net/events/show-n-tell??'
show_n_tell.notes            = ''

swap_fall = cal_events.EventType()
swap_fall.type_id            = 17
swap_fall.name               = '*Fall Swap Meet'
swap_fall.visibility         = EventVisibility.public
swap_fall.coordinator_id     = 1
swap_fall.location           = locations[1]
swap_fall.repeat             = EventRepeat.annual
swap_fall.lunar_phase        = RuleLunar.moon_full
swap_fall.day_of_week        = RuleWeekday.sunday
swap_fall.rule_start_time    = RuleStartTime.absolute
swap_fall.month              = 10
swap_fall.time_start         = datetime.time(hour=11)
swap_fall.time_length        = datetime.timedelta(hours=4)
swap_fall.url                = 'www.sjaa.net/events/swap-meet'
swap_fall.notes              = ''


def gen_events(start, end):
    events_public      = []
    events_member      = []
    events_volunteer   = []
    events_coordinator = []
    events_private     = []
    events_board       = []
    event_types = (class_intro, class_101, itsp_1q, itsp_3q, dark_sky,
                   quick_start, solar_sunday, fix_it, board_mtg, gen_mtg,
                   starry_night, image_sig, mem_mtg, swap_spring, movie_night,
                   show_n_tell, swap_fall)
#   event_types = (class_intro, class_101, itsp_1q, itsp_3q, dark_sky,
#                  quick_start, solar_sunday)
    # generate all events for each type of visibility
    for evtype in event_types:
        if   evtype.visibility == EventVisibility.public:
            events = events_public
        elif evtype.visibility == EventVisibility.member:
            events = events_member
        elif evtype.visibility == EventVisibility.volunteer:
            events = events_volunteer
        elif evtype.visibility == EventVisibility.coordinator:
            events = events_coordinator
        elif evtype.visibility == EventVisibility.private:
            events = events_private
        elif evtype.visibility == EventVisibility.board:
            events = events_board
        # create list of time/event name pairs
        if evtype.repeat == EventRepeat.lunar:
            event_dates = cal_events.calc_lunar_dates(start, end, evtype)
        elif evtype.repeat == EventRepeat.monthly:
            event_dates = cal_events.calc_monthly_dates(start, end, evtype)
        elif evtype.repeat == EventRepeat.annual:
            event_dates = cal_events.calc_annual_dates(start, end, evtype)

        # create list of all events
        for date in event_dates:
            sun  = None
            moon = None
            if evtype.rule_start_time != RuleStartTime.absolute:
                # get ephemeris data for sun, moon for start times based on twilight
                sun, moon = cal_ephemeris.calc_date_ephem(date)
            events.append((date, evtype.name, sun, moon))

#   pdb.set_trace()
    # sort events by time and print
    for evtype in EventVisibility:
        if   evtype == EventVisibility.ephemeris:
            events = cal_ephemeris.astro_events
        elif evtype == EventVisibility.public:
            events = events_public
        elif evtype == EventVisibility.member:
            events = events_member
        elif evtype == EventVisibility.volunteer:
            events = events_volunteer
        elif evtype == EventVisibility.coordinator:
            events = events_coordinator
        elif evtype == EventVisibility.private:
            events = events_private
        elif evtype == EventVisibility.board:
            events = events_board
        if events:
            events.sort()
            print("======================================")
            print("{} events - total: {}".format(event_visibility[evtype], len(events)))
            print("--")
            for ev in events:
                if len(ev) > 2 and ev[2]:
                    # event has sun/moon ephemeris times
                    print("{} - {}".format(ev[0].strftime(FMT_YEAR_DATE_HM),
                          ev[1]))
                    print("{:23}   {}".format('', ev[2]))
                    print("{:23}   {}".format('', ev[3]))
                else:
                    print("{} - {}".format(ev[0].strftime(FMT_YEAR_DATE_HM),
                          ev[1]))


if __name__ == '__main__':
    year = '2016'
    if len(sys.argv) > 1:
        year = sys.argv[1]
    else:
        tmp = input("Specify year [{}]: ".format(year))
        if tmp:
            year = tmp
    if not year.isdigit():
        print("{} is not a number".format(year))
        print("  test.py [year]")
        exit()
    year = int(year)
    cal   = cal_ephemeris.calc(year)
    start = TZ_LOCAL.localize(datetime.datetime(year, 1, 1))
    end   = datetime.datetime(year+1, 1, 1) - datetime.timedelta(seconds=1)
    end   = TZ_LOCAL.localize(end)
    gen_events(start, end)
