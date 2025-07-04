#!/usr/bin/env python3
"""
Simple Dice Roller - Roll a single die with specified number of sides
"""

import random
import sys
import argparse

def roll_die(sides):
    """Roll a single die with the specified number of sides"""
    return random.randint(1, sides)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Roll a single die')
    parser.add_argument('sides', type=int, help='Number of sides on the die')
    
    args = parser.parse_args()
    
    result = roll_die(args.sides)
    print(f"Rolling a {args.sides}-sided die...")
    print(result)

if __name__ == "__main__":
    main()
