#!/usr/bin/env python3
"""
Simple Dice Roller - Roll multiple dice with specified number of sides
"""

import random
import sys
import argparse
import re

def roll_die(sides):
    """Roll a single die with the specified number of sides"""
    return random.randint(1, sides)

def parse_dice_notation(dice_spec):
    match = re.match(r'^(\d+)d(\d+)$', dice_spec)
    if not match:
        raise ValueError(f"Invalid dice notation: {dice_spec}. Use format like '2d20' or '1d6'")
    
    count = int(match.group(1))
    sides = int(match.group(2))
    
    if count < 1:
        raise ValueError(f"Number of dice must be at least 1, got {count}")
    if sides < 1:
        raise ValueError(f"Number of sides must be at least 1, got {sides}")
    
    return count, sides

def roll_dice_group(count, sides):
    results = []
    for i in range(count):
        results.append(roll_die(sides))
    return results

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Roll multiple dice')
    parser.add_argument('dice', nargs='+', help='Dice to roll in formet like "2d20" or "1d6"')
    
    args = parser.parse_args()
    
    # Parse and validate all dice specifications
    dice_groups = []
    for dice_spec in args.dice:
        try:
            count, sides = parse_dice_notation(dice_spec)
            dice_groups.append((count, sides, dice_spec))
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    # Log what we're rolling
    dice_descriptions = []
    for count, sides, original_spec in dice_groups:
        if count == 1:
            dice_descriptions.append(f"one {sides}-sided die")
        else:
            dice_descriptions.append(f"{count} {sides}-sided dice")
    
    print(f"Rolling {', '.join(dice_descriptions)}...", file=sys.stderr)
    
    # Roll all dice and collect results
    all_results = []
    for count, sides, _ in dice_groups:
        results = roll_dice_group(count, sides)
        all_results.extend(results)
    
    # Output results
    result_strings = []
    for result in all_results:
        result_strings.append(str(result))
    sys.stdout.write(" ".join(result_strings) + "\n")
    sys.stdout.write(f"{sum(all_results)}\n")

if __name__ == "__main__":
    main()
