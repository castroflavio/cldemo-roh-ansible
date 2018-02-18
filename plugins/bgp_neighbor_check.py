#!/usr/bin/python
import re
from ansible import errors

class FilterModule(object):
    def filters(self):
        return {
            'bgp_neighbor_check': self.bgp_neighbor_check
        }

    def bgp_neighbor_check(self, bgp_summary):
        s = bgp_summary.split('Neigh')[1]
        return s 
