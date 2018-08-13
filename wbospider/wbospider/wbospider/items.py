# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InformationItem(scrapy.Item):
    """ 个人信息 """
    _id = scrapy.Field()  # 用户ID
    NickName = scrapy.Field()  # 昵称
    Gender = scrapy.Field()  # 性别
    Province = scrapy.Field()  # 所在省
    City = scrapy.Field()  # 所在城市
    BriefIntroduction = scrapy.Field()  # 简介
    Birthday = scrapy.Field()  # 生日
    Num_Tweets = scrapy.Field()  # 微博数
    Num_Follows = scrapy.Field()  # 关注数
    Num_Fans = scrapy.Field()  # 粉丝数
    SexOrientation = scrapy.Field()  # 性取向
    Sentiment = scrapy.Field()  # 感情状况
    VIPlevel = scrapy.Field()  # 会员等级
    Authentication = scrapy.Field()  # 认证
    URL = scrapy.Field()  # 首页链接


class TweetsItem(scrapy.Item):
    """ 微博信息 """
    _id = scrapy.Field()  # 用户ID-微博ID
    ID = scrapy.Field()  # 用户ID
    Content = scrapy.Field()  # 微博内容
    PubTime = scrapy.Field()  # 发表时间
    Co_oridinates = scrapy.Field()  # 定位坐标
    Tools = scrapy.Field()  # 发表工具/平台
    Like = scrapy.Field()  # 点赞数
    Comment = scrapy.Field()  # 评论数
    Transfer = scrapy.Field()  # 转载数


class RelationshipsItem(scrapy.Item):
    """ 用户关系，只保留与关注的关系 """
    fan_id = scrapy.Field()
    followed_id = scrapy.Field()  # 被关注者的ID