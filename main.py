#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import connection

def main():
    if len(sys.argv) == 1:
        connection.local()
    elif sys.argv[1] == '--server':
        if len(sys.argv) == 2: connection.server("user")
        if len(sys.argv) == 3: connection.server("ai")
    elif sys.argv[1] == '--client':
        if len(sys.argv) == 3: connection.client(sys.argv[2], "user")
        if len(sys.argv) == 4: connection.client(sys.argv[2], "ai")


if __name__ == "__main__":
    main()
