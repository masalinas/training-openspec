# Tasks

## 1. CLI Parsing & Validation

- [x] 1.1 Add `--line-style` (`-l`) argument with choices `["solid", "dashed", "dashdot", "dotted"]` and default `"solid"` in `src/sine_generator/cli.py` and verify CLI help message and parsing behavior
- [x] 1.2 Add unit tests for `--line-style` argument parsing (default and custom values) in `tests/test_cli.py` and verify with `pytest tests/test_cli.py`

## 2. Generator Engine & Main Application Wiring

- [x] 2.1 Update `plot_sine_wave` in `src/sine_generator/generator.py` to accept `line_style: str = "solid"` and pass `linestyle=line_style` to `ax.plot()`
- [x] 2.2 Update `src/sine_generator/main.py` to pass `parsed.line_style` to `plot_sine_wave()` and include line style in console logging
- [x] 2.3 Add unit tests in `tests/test_generator.py` to verify line style parameter handling and run `pytest` to confirm all tests pass
