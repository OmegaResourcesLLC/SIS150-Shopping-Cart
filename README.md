# SIS150 Shopping Cart

**Author:** Jeff Mendenhall  
**Course:** DeVry SIS150  
**Assignment:** zyBooks 7.1.1, Project: Online shopping cart

A Python console program that uses two classes to manage a shopping cart.
This is a classroom project; it does not process payments or place online orders.

## Features

- Add an item with its name, price, and quantity.
- Remove an item by name.
- Change an item's quantity while keeping its price.
- Display individual item costs, the total quantity, and the cart total.
- Report an empty cart or an item that cannot be found.
- Repeat the menu until the user chooses to quit.
- Prompt again when a menu choice is invalid.

## Classes

- **ItemToPurchase:** Stores an item's name, price, and quantity and prints its cost.
- **ShoppingCart:** Stores the customer name, date, and item list and provides cart operations.

## Run the program

Install Python 3, download `main.py`, and run:

```bash
python main.py
```

On systems that use the `python3` command:

```bash
python3 main.py
```

No additional packages are required. Enter the customer name and date, then choose a menu option.

| Option | Action |
| --- | --- |
| a | Add item |
| r | Remove item |
| c | Change quantity |
| o | Output shopping cart |
| q | Quit |

## Example cart output

```text
John Doe's Shopping Cart - February 1, 2025
Number of Items: 8

Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128

Total: $521
```

## Scope and verification

The program expects valid numeric prices and integer quantities.
It uses floating-point prices as specified in the assignment, and cart contents
are kept in memory only.

Local checks cover the lesson's example output, cart updates, missing items,
an empty cart, invalid menu choices, and quitting. The revised code still needs
to be submitted to zyBooks to confirm its automated grading result.
