# Proposal

## Why

Users currently cannot customize the line style (solid, dashed, dotted, etc.) when generating sine wave plots. Adding a `--line-style` parameter improves plot visualization and flexibility for users presenting or analyzing sine waves.

## What Changes

- Add `--line-style` (`-l`) parameter to the CLI parser in `sine_generator/cli.py` supporting `solid`, `dashed`, `dashdot`, and `dotted` styles (defaulting to `solid`).
- Update `plot_sine_wave` in `sine_generator/generator.py` to accept the `line_style` parameter and render the wave using the requested Matplotlib line style.
- Update `sine_generator/main.py` to pass the parsed line style option to the plotting engine.
- Add test coverage for line style parsing and plotting logic.

## Capabilities

### New Capabilities

*(None)*

### Modified Capabilities

- `sine-generator`: Extend CLI argument parsing and sine wave plotting requirements to support line style specification.

## Impact

- `src/sine_generator/cli.py`: Adds `--line-style` / `-l` argument to `argparse`.
- `src/sine_generator/generator.py`: Modifies `plot_sine_wave` function signature and Matplotlib `ax.plot` call.
- `src/sine_generator/main.py`: Connects CLI argument to plotting invocation.
- `tests/`: Unit test suite updates for CLI argument parsing and plot generation.
