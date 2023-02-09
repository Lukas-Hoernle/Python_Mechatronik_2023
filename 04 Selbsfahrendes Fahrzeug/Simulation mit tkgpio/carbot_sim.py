#! /usr/bin/env python3
"""
Startskript für das carbot_sim-Program
"""

from carbot_sim.main import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass