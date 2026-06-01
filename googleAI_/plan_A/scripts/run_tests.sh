#!/bin/bash
# Engineering Principle: Strict Validation & Guarded Execution
set -e

echo "[TEST] Starting unit and integration test suite..."

# Set PYTHONPATH to include the src directory
export PYTHONPATH=$PYTHONPATH:$(pwd)/googleAI_/plan_A

# Run pytest
pytest googleAI_/plan_A/tests/

if [ $? -eq 0 ]; then
    echo "[SUCCESS] All tests passed."
else
    echo "[FAILURE] Tests failed. Analyzing stack trace..."
    # In a real CI environment, we would trigger rollback here
    exit 1
fi
