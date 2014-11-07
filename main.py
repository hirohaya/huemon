#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import interface
import connection

def main():
    interface.oak_intro()
    if len(sys.argv) == 1:
        connection.local()
    elif sys.argv[1] == '--server':
        connection.server()
    elif sys.argv[1] == '--client':
        connection.client(sys.argv[2])


if __name__ == "__main__":
    main()
