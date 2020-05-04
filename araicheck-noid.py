#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math
import numpy
import twitter
import email
import datetime

arai_string='アライさんクエスト'
target_users=('gyakureiashuman',)


api = twitter.Api(
    consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret='',
    sleep_on_rate_limit=False
)

today_yday = time.localtime().tm_yday
for target_user in target_users:
    tweets = api.GetUserTimeline(screen_name=target_user, include_rts=False, exclude_replies=True, count=200) # , count=200

    found = False
    for s in tweets:
        #print(s.text)
        tweet_tm = time.localtime(email.utils.mktime_tz(email.utils.parsedate_tz(s.created_at)))
        if arai_string in s.text and ((tweet_tm.tm_hour == 0 and tweet_tm.tm_yday == today_yday) or
               (tweet_tm.tm_hour == 23 and tweet_tm.tm_yday == today_yday-1)):
            if s.text.count('☑') >= 5:
                api.PostUpdate("💪偉い🏋️", in_reply_to_status_id=s.id, auto_populate_reply_metadata=True)
                #print("💪偉い🏋️")
            else:
                api.PostUpdate("もうひと頑張り😘", in_reply_to_status_id=s.id, auto_populate_reply_metadata=True)
                #print("もうひと頑張り😘")
                
            found = True
            break
    if not found:
        api.PostUpdate("@" + target_user + " 👈サボってるでしょ😭", auto_populate_reply_metadata=True)
        #print("@" + target_user + " 👈サボってるでしょ😭")
