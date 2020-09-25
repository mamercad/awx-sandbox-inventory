#!/usr/bin/env python3

import argparse
import json


class TestInventory1(object):
    def __init__(self):
        self.inventory = {}
        raise Exception('Whoops')
        print(self.json_format_dict(self.inventory))

    def json_format_dict(self, data, pretty=False):
        if pretty:
            return(json.dumps(data, sort_keys=True, indent=2))
        else:
            return(json.dumps(data))


if __name__ == '__main__':
    TestInventory1()
