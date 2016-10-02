# coding=utf-8

import transitfeed


class FeedInfoCreator(object):

    def __init__(self, config):
        self.config = config

    def __repr__(self):
        rep = ""
        if self.config is not None:
            rep += str(self.config) + " | "
        return rep

    def add_feed_info_to_schedule(self, schedule):
        schedule.AddFeedInfoObject(self.prepare_feed_info())

    def prepare_feed_info(self):
        """
        Loads feed info data from a json config file.
        Return a transitfeed.FeedInfo object
        """
        feed_info = transitfeed.FeedInfo()
        feed_info.feed_publisher_name = self.config['feed_info']['publisher_name']
        feed_info.feed_publisher_url = self.config['feed_info']['publisher_url']
        feed_info.feed_lang = self.config['agency']['agency_lang']
        feed_info.feed_start_date = self.config['feed_info']['start_date']
        feed_info.feed_end_date = self.config['feed_info']['end_date']
        feed_info.feed_version = self.config['feed_info']['version']
        return feed_info
