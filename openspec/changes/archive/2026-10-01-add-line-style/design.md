# Design

## Context

See `proposal.md` for motivation. Currently, `sine_generator` accepts frequency, amplitude, color, and export options, rendering the wave with a fixed solid line style.

## Goals / Non-Goals

**Goals:**
- Provide a CLI parameter `--line-style` (`-l`) allowing users to choose the line style of the plotted sine wave.
- Support standard Matplotlib line style names (`solid`, `dashed`, `dashdot`, `dotted`).
- Maintain backward compatibility by defaulting to `solid`.

**Non-Goals:**
- Custom tuple-based dash sequences or complex line marker configurations.

## Decisions

### Decision 1: CLI Argument Validation via `choices`
In `sine_generator/cli.py`, add `--line-style` / `-l` with `choices=["solid", "dashed", "dashdot", "dotted"]` and `default="solid"`.
- *Rationale*: Restricting choices at the CLI boundary provides clear error messages when invalid line styles are passed.

### Decision 2: Function Signature Update in `plot_sine_wave`
Update `plot_sine_wave(time, wave, color="blue", line_style="solid", output_path=None)` in `sine_generator/generator.py`. Pass `linestyle=line_style` to `ax.plot()`.
- *Rationale*: Keeps `plot_sine_wave` flexible and reusable programmatically while maintaining sensible default values.

## Risks / Trade-offs

- *Risk*: Passing an unsupported line style programmatically outside the CLI could cause a Matplotlib `ValueError`.
- *Mitigation*: The CLI enforces `choices`, and `plot_sine_wave` uses standard Matplotlib linestyle values.
