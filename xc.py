# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 21:55:58 2017

"""
from __future__ import absolute_import
import pandas as pd
import time

#rl
if __name__=="__main__":
    
    """
    ########################处理对应表################################
    dyb = {}
    dyb_pd = pd.read_excel("duiyingbiao.xlsx", encoding="gbk")
    r, c = dyb_pd.shape
    for i in range(r):
        a = dyb_pd.iloc[i,:]
        code, name = a[0],a[1]
        dyb[code] = name
    
    ########################处理天气################################
    
    def norm_tq(tq):
        if pd.isnull(tq):
            return -1
        elif u'暴雨' in tq:
            return 3
        elif u'暴雪' in tq:
            return 3
        elif u'大雨' in tq:
            return 3
        elif u'大雪' in tq:
            return 3
        elif u'雷阵雨' in tq:
            return 3
        elif u'雷雨' in tq:
            return 3
        elif u'大风' in tq:
            return 2
        elif u'冻雨' in tq:
            return 2
        elif u'中雨' in tq:
            return 2
        elif u'雨夹雪' in tq:
            return 2
        elif u'中雪' in tq:
            return 2
        elif u'扬沙' in tq:
            return 2
        elif u'雾' in tq:
            return 2
        elif u'小雨' in tq:
            return 1
        elif u'小雪' in tq:
            return 1
        elif u'阵雪' in tq:
            return 1
        elif u'阵雨' in tq:
            return 1
        elif u'浮尘' in tq:
            return 1
        elif u'风' in tq:
            return 1
        elif u'雨' in tq:
            return 1
        elif u'雪' in tq:
            return 1
        elif u'严寒' in tq:
            return 1
        elif u'极其寒冷' in tq:
            return 1
        elif u'晴' in tq:
            return 0
        elif u'阳光' in tq:
            return 0
        elif u'酷热' in tq:
            return 0
        elif u'潮湿' in tq:
            return 0
        elif u'凉爽' in tq:
            return 0
        elif u'暖' in tq:
            return 0
        elif u'冷' in tq:
            return 0
        elif u'云' in tq:
            return 0
        elif u'阴' in tq:
            return 0
        elif u'星光璀灿' in tq:
            return 0
        elif u'月光明亮' in tq:
            return 0
        elif u'烈日' in tq:
            return 0
        else:
            return -1
    
    def norm_temp(temp_low, temp_high): 
        if pd.isnull(temp_low) and pd.isnull(temp_high):
            return -1
        elif pd.isnull(temp_low):
            if float(temp_high) > 40 or float(temp_high) < -20:
                return 1
            else:
                return 0
        elif pd.isnull(temp_high):
            if float(temp_low) > 40 or float(temp_low) < -20:
                return 1
            else:
                return 0
        else:
            if float(temp_high) > 40 or float(temp_low) < -20:
                return 1
            else:
                return 0
        
    tianqi = {}
    tianqi_pd = pd.read_csv("tianqi.csv")
    r, c = tianqi_pd.shape
    for i in range(r):
        a = tianqi_pd.iloc[i,:]
        try:
            temp = norm_temp(a[2],a[3])
        except:
            temp = 0
        city, tq, date = a[0],norm_tq(a[1]),a[4]
        
        try:
            tianqi[city]
            tianqi[city][date] = [tq, temp]
        except:
            tianqi[city] = {}
            tianqi[city][date] = [tq, temp]

    """
    
    
    ########################处理data################################
    def format_time(time_g):
        time_formate = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time_g))
        return time_formate.split()[0], time_formate.split()[1]
    
    def get_late(a):
        if a[8] == u"取消":
            late = 1
        elif int(a[5]) - int(a[3]) > 3 * 3600:
            late = 1
        else:
            late = 0        
        return late
    data = {}
    data_pd = pd.read_csv("data.csv", encoding="gbk")    
    r, c = data_pd.shape
    for i in range(r):
        a = data_pd.iloc[i,:]
        cf, dd, hbbh, fjbh = a[0],a[1],a[2],a[7]  
        qf_date, qf_time = format_time(a[3])   
        try:
            late = get_late(a)
        except:
            pass
            
    