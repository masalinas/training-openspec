# Spec Delta: sine-generator

## MODIFIED Requirements

### Requirement: CLI Argument Parsing
The system SHALL accept five parameters via standard library `argparse`: frequency (`--frequency`), amplitude (`--amplitude`), line color (`--color`), line style (`--line-style` / `-l`), and an optional PNG export flag (`--export`).

#### Scenario: User provides all arguments via CLI
- **WHEN** the user executes the command with `--frequency 5.0 --amplitude 2.0 --color red --line-style dashed --export`
- **THEN** the CLI parses frequency as 5.0, amplitude as 2.0, color as "red", line style as "dashed", and sets export flag to True

#### Scenario: Default line style value
- **WHEN** the user executes the command without specifying `--line-style`
- **THEN** the CLI parses line style as "solid" by default

#### Scenario: User requests help
- **WHEN** the user executes the CLI with `--help`
- **THEN** the CLI displays parameter descriptions and usage guidance in English including line style options

### Requirement: Sine Wave Plotting
The system SHALL calculate sine wave data points for the given frequency and amplitude over a standard time range and render a plot using matplotlib with the specified line color and line style.

#### Scenario: Rendering a sine wave plot
- **WHEN** valid frequency, amplitude, color, and line style parameters are provided to the generator engine
- **THEN** the system generates data points and plots the curve with the specified line color and line style
