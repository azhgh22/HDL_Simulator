HDL Parser and Chip Testing Framework

📘 Overview
This project implements a Python-based HDL (Hardware Description Language) parser and chip testing simulator. It can:

Simulate chip behavior with given input test vectors.
Automatically validate output correctness and produce test reports.

🔧 The framework assumes syntactically correct HDL files and valid test vector inputs.


🧱 Built-in Gates
These primitive gates are natively supported and do not require HDL definitions:

| Chip Name  | Description                        | Inputs         | Outputs  |
|------------|------------------------------------|----------------|----------|
| `Nand`     | Logical NAND gate                  | 2              | 1        |
| `Not`      | Logical NOT gate                   | 1              | 1        |
| `And`      | Logical AND gate                   | 2              | 1        |
| `Or`       | Logical OR gate                    | 2              | 1        |

These act as atomic units in simulation.

🧠 How It Works
✅ HDL Parsing
Parses CHIP blocks with IN, OUT, and PARTS sections.

Handles multiple-line declarations and comments.

Supports sub-chip instantiations and resolves dependencies recursively.

✅ Simulation
Executes chips from the bottom-up, starting with built-ins.

Propagates input signals and computes outputs at each level.

Simulates composed chips by evaluating their internal components.

✅ Chip Example

CHIP HalfAdder {
    IN a, b;    // 1-bit inputs
    OUT sum,    // Right bit of a + b 
        carry;  // Left bit of a + b

    PARTS:
    Xor(a=a, b=b, out=sum);
    And(a=a, b=b, out=carry);
    
}


✅ Test Runner
Reads CSV-style test vector files:

a,b,sum,carry
0,0,0,0
0,1,1,0
1,0,1,0
1,1,0,1
Compares actual vs expected outputs and prints:

Test case 1: Pass
    Inputs: a=0 b=0 → Output: expected_sum=0 your_sum=0 expected_carry=0 your_carry=0 
Test case 2: Pass
    Inputs: a=0 b=1 → Output: expected_sum=1 your_sum=1 expected_carry=0 your_carry=0 
Test case 3: Pass
    Inputs: a=1 b=0 → Output: expected_sum=1 your_sum=1 expected_carry=0 your_carry=0 
Test case 4: Pass
    Inputs: a=1 b=1 → Output: expected_sum=0 your_sum=0 expected_carry=1 your_carry=1 
Passed 4/4 tests


🚀 Usage

cd HDL_Simulator
pip install -r requirements.txt

1. Run the simulation

    python -m src.main
    inputs: 
        1. path to hdl file
        2. path to test(csv) files

2. run tests
    pytest tests


✅ Assumptions
HDL files are syntactically valid.

All referenced HDL chips exist in the provided directory.

Only 1-bit inputs/outputs are supported.

No support for sequential logic or clocks.

📌 Limitations
❌ No error reporting or syntax checking.

❌ No support for multi-bit buses or arrays.

❌ Do not use ';' in names of chip's IN, OUT bit names

