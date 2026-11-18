
# AI-Assisted Workflow & Policy Reviewer

## Overview

AI-Assisted Workflow & Policy Reviewer is a Python-based system that reviews workflow requirements, specifications, approvals, and implementation code to detect inconsistencies before deployment.

The reviewer combines deterministic rule validation, formal verification using Z3 SMT Solver, and AI-assisted analysis to generate evidence-backed review reports.

This project was developed as part of an AI/ML engineering assessment.

---

# Features

- Requirement and specification consistency checking
- Workflow validation
- Approval-aware policy verification
- Python code consistency checking
- Evidence-backed findings
- Z3 SMT-based counterexample generation
- LLM response validation with guardrails
- Regression testing
- Offline evaluation benchmark
- Command Line Interface (CLI)

---

# Technologies Used

### Language

- Python

### Libraries

- Pydantic
- Z3 Solver
- NetworkX
- PyTest
- argparse
- json
- os

### Concepts

- Artificial Intelligence
- Formal Verification
- Constraint Solving
- Workflow Validation
- Policy Compliance
- LLM Guardrails
- Automated Testing
- Regression Testing
- JSON Processing

---

# Project Structure

```text
AI-Workflow-Reviewer/
│
├── reviewer/
│   ├── stage1_contracts.py
│   ├── stage2_review.py
│   ├── stage3_orchestrator.py
│   ├── stage4_eval.py
│   └── ...
│
├── tests/
│   └── test_regressions.py
│
├── fixtures/
│
├── outputs/
│   ├── evaluation_report.json
│   └── cli_eval_stdout.json
│
├── cli.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/AI-Workflow-Reviewer.git
cd AI-Workflow-Reviewer
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

```bash
pytest -v tests/test_regressions.py
```

---

# Running Evaluation

```bash
python cli.py eval
```

The evaluation report will be generated inside the **outputs/** directory.

---

# Reviewing a Bundle

```bash
python cli.py review --bundle path/to/bundle.json
```

---

# Evaluation Results

## Final System

| Metric | Result |
|---------|--------|
| Correct Predictions | 14 / 14 |
| Accuracy | 100% |
| False Passes | 0 |
| False Blocks | 0 |

---

## Supported Review Capabilities

- Requirement validation
- Workflow verification
- Boundary condition checking
- Rule precedence validation
- Approval conflict detection
- Code-specification consistency checking
- LLM output validation
- Counterexample generation using Z3

---

## Ablation Study

| Configuration | Correct |
|--------------|---------|
| Full System | 14 / 14 |
| Without SMT Verification | 7 / 14 |

The SMT-based verification significantly improved the system's ability to detect behavioral inconsistencies and generate concrete counterexamples.

---

# Example Counterexample

```json
{
  "ticket_input": {
    "category": "present_value",
    "urgent": true,
    "wait_time": 1800
  },
  "expected_route": "priority_queue",
  "actual_route": "escalation"
}
```

---

# Testing

The project includes automated regression tests covering:

- Cache invalidation
- LLM hallucination filtering
- Dataset evaluation
- Approval updates
- Workflow correctness

Run:

```bash
pytest -v
```

---

# Future Improvements

- Support additional workflow formats
- Enhanced LLM reasoning
- Rich HTML/PDF report generation
- Support for larger enterprise workflow datasets

---

# Author

**Trupti Panchwatkar**

B.Tech in Electronics Engineering (2026)

Interested in Artificial Intelligence, Machine Learning, Python Development, and Workflow Automation.
