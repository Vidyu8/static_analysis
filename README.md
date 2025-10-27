# Static_analysis

## Issue Table

<img width="805" height="772" alt="image" src="https://github.com/user-attachments/assets/028745cc-e970-4f11-a6ab-eb7df823cb16" />


## Easiest vs. Hardest Issues

### Easiest Fixes:
* Removing unused imports (line 2) - simply deleting one line
* Converting to f-strings (line 12) - straightforward syntax change
* Adding explicit file encoding - just adding encoding='utf-8' parameter

### Hardest Fixes:
* Mutable default arguments - Required understanding of Python's function scope and the None pattern
* Replacing eval() safely - Needed research on ast.literal_eval vs direct code execution risks
* Specific exception handling - Determining which exact exceptions to catch instead of bare except:

## False Positives

Yes, one potential false positive:
The global variable warning (W0603) for stock_data could be considered a false positive in this context. For a simple script managing shared state, using a global variable is a valid design choice, though Pylint flags it as poor practice. In a larger application, this would legitimately need refactoring into a class.

## Integration into Development Workflow

### Local Development:

* Pre-commit hooks to run Pylint/Flake8 before each commit
* Editor integrations (VS Code extensions) for real-time feedback
* Makefile targets for easy manual execution
* CI/CD Pipeline:</br>
	GitHub Actions to run all three tools on every pull request</br>
	Quality gates - block merges if security issues (Bandit) or low scores (Pylint) detected</br>
	Automated reporting - post results as PR comments</br>
	Team Process: Score thresholds in CI (e.g., Pylint ≥ 8.0 required)

## Tangible Improvements Observed

### Security:
* Eliminated dangerous eval() usage preventing code injection
* Specific exception handling prevents masking unexpected errors

### Code Quality:
* Input validation prevents type errors during runtime
* Proper resource management with with statements prevents file handle leaks
* Immutable defaults eliminate subtle bugs from shared state

### Readability & Maintainability:
* Comprehensive docstrings make the API self-documenting
* Consistent naming (snake_case) follows Python conventions
* Structured error handling makes failure modes explicit

### Robustness:
* Graceful degradation - functions return False/defaults instead of crashing
* Defensive programming - type checks prevent invalid operations
* Clear separation between business logic and I/O operations


Overall Impact: The code transformed from a fragile script with security risks to a professional, maintainable, and secure inventory management system. Static analysis proved invaluable for catching issues that manual review would likely miss.
