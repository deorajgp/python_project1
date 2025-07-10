# Graph Assignment

This Python project processes a list of numbers with a sequence of operations — summation, multiplication, and division — with custom rules for handling odd results.

## Folder Structure
```
Python_project1/
├── helpers/
│ ├── general_utils.py
│ └── math_utils.py
├── main.py
├── .gitignore
└── README.md
```

## Project Overview

The project:

1. Accepts a list of numbers (atleast 2) through a function and the last number entered must not be zero.
2. Summation:
   - Sums all the numbers.
   - If the sum is odd, appends numbers (up to 3 times) to try and reach an even sum.
3. Multiplication:
   - Multiplies all the numbers.
   - If the result is odd, appends numbers (up to 3 times) to try and reach an even product.
4. Division:
   - Divides the first number by the last number in the final list.

---

## How to Run

1. **Clone the repository**: 

```bash
git clone https://github.com/yourusername/Python_project1.git
cd Python_project1
```

2. **Run the main script**:

```bash
python main.py
```
## Libraries used

1. random:
   - to generate random number in case the result of addition or division is odd
2. math:
   - to sum and multiply elements
3. time:
   - for better user experience
