# Unit Converter

A command-line Python tool for converting between common units of length, weight, and temperature.

## Features

- **Length:** meters ↔ kilometers, miles ↔ kilometers, feet ↔ meters
- **Weight:** grams ↔ kilograms, kilograms ↔ pounds
- **Temperature:** Celsius ↔ Fahrenheit, Celsius ↔ Kelvin
- Simple menu-driven interface with a loop until the user chooses to exit

## Requirements

- Python 3 (no external libraries needed)

## Usage

```bash
python Unit_Converter.py
```

1. Choose a category: Length, Weight, or Temperature.
2. Choose the specific conversion from the sub-menu.
3. Enter the value to convert.
4. View the result, then continue converting or exit.

## Notes

- Invalid menu choices are handled with an "Invalid choice" message rather than crashing.
- Results are rounded to 2–4 decimal places depending on the conversion.
