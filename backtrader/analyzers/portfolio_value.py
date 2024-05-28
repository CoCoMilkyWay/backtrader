#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2023 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from collections import OrderedDict

from backtrader.utils.py3 import range
from backtrader import Analyzer


class Portfolio_Value(Analyzer):
    def stop(self):
        index_1st = len(self.data) - 1
        self.portfolio_value = OrderedDict()
        self.daily_return = OrderedDict()
        last_value = self.strategy.stats.broker.value[-index_1st]
        for i in range(index_1st, -1, -1):
            dt = self.data.datetime.date(-i)
            # Must have stats.broker
            current_value = self.strategy.stats.broker.value[-i]
            self.portfolio_value[dt] = current_value
            self.daily_return[dt] = current_value/last_value
            last_value = current_value
        
        # instance = self.datas[0]
        # for attribute in dir(instance):
        #   if callable(getattr(instance, attribute)):
        #       print(attribute)
        #   else:
        #       print(attribute)

    def get_analysis(self):
        return self.portfolio_value, self.daily_return
