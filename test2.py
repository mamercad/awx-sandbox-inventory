#!/usr/bin/env python3

import argparse
import json
import time


class TestInventory1(object):
    def __init__(self):
        self.inventory = {
            "_meta": {
                "hostvars": {
                    "host1": {
                        "var1": "value"
                    },
                    "host2": {
                        "var2": "value"
                    }
                }
            },
            "all": {
                "children": [
                    "ungrouped"
                ]
            },
            "ungrouped": {
                "hosts": [
                    "host1",
                    "host2"
                ]
            }
        }
        if int(time.time())%2: # Fail about half the time
            raise Exception('Whoops')
        print(self.json_format_dict(self.inventory))

    def json_format_dict(self, data, pretty=False):
        if pretty:
            return(json.dumps(data, sort_keys=True, indent=2))
        else:
            return(json.dumps(data))


if __name__ == '__main__':
    TestInventory1()
