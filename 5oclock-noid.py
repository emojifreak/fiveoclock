#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math
import numpy
import twitter
import email
import datetime

clock_char='🕔'
target_users=('inferist', 'yamaken37',  'csemitovt')
#target_users=('inferist')


api = twitter.Api(
    consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret='',
    sleep_on_rate_limit=True
)

for target_user in target_users:
    tweets = api.GetUserTimeline(screen_name=target_user, include_rts=False, exclude_replies=True)

    for s in tweets:
        if s.text==clock_char:
            tweet_tm = time.localtime(email.utils.mktime_tz(email.utils.parsedate_tz(s.created_at)))
            if tweet_tm.tm_hour == 16 and tweet_tm.tm_yday == today_yday:
                api.PostUpdate("フライング❣\nm9(^Д^)ﾌﾟｹﾞﾗ", in_reply_to_status_id=s.id, auto_populate_reply_metadata=True)


numpy.random.seed(math.ceil(1000*time.time()) % (2**32))
delay_sec = abs(30*numpy.random.standard_cauchy())
current_sec = time.localtime().tm_sec
today_yday = time.localtime().tm_yday
#if delay_sec > current_sec:
if False:
    time.sleep(delay_sec-current_sec)
else:
    delay_sec=current_sec
    
clock_status = api.PostUpdate(clock_char)
current_time = time.time()

ranking = 1
for target_user in target_users:
    tweets = api.GetUserTimeline(screen_name=target_user, include_rts=False, exclude_replies=True)

    for s in tweets:
        if s.text==clock_char:
            tweet_tm = time.localtime(email.utils.mktime_tz(email.utils.parsedate_tz(s.created_at)))
            if tweet_tm.tm_yday == today_yday:
                ranking += 1
                true_ojisan_utc_epoch = datetime.datetime.fromtimestamp(((s.id >> 22) + 1288834974657) / 1000.0)
                true_delay = true_ojisan_utc_epoch - datetime.datetime(time.gmtime().tm_year, time.gmtime().tm_mon, time.gmtime().tm_mday, 17)
                api.PostUpdate("敗北 orz\n時間差 {0:.2f} 秒\n相手の遅延 {1:.3f} 秒".format(
                    ((int(clock_status.id)>>22)-(int(s.id)>>22))/1000.0,true_delay), in_reply_to_status_id=s.id, auto_populate_reply_metadata=True)

true_ojisan_utc_epoch = datetime.datetime.fromtimestamp(((clock_status.id >> 22) + 1288834974657) / 1000.0)
true_delay = true_ojisan_utc_epoch - datetime.datetime(time.gmtime().tm_year, time.gmtime().tm_mon, time.gmtime().tm_mday, 17)
api.PostUpdate("{:d} 人中 ".format(1+len(target_users))+"{:d} 位❣".format(ranking)
               +"\n真実の遅延 {:.2f} 秒".format(true_delay.total_seconds()), in_reply_to_status_id=clock_status.id)
