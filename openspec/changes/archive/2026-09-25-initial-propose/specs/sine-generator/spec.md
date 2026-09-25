# Spec Delta

## Purpose

Provides a command-line interface tool to calculate and visualize mathematical sine waves with customizable parameters and PNG export capability.

## ADDED Requirements

### Requirement: CLI Argument Parsing
The system SHALL accept four parameters via standard library `argparse`: frequency (`--frequency`), amplitude (`--amplitude`), line color (`--color`), and an optional PNG export flag (`--export`).

#### Scenario: User provides all arguments via CLI
- **WHEN** the user executes the command with `--frequency 5.0 --amplitude 2.0 --color red --export`
- **THEN** the CLI parses frequency as 5.0, amplitude as 2.0, color as "red", and sets export flag to True

#### Scenario: User requests help
- **WHEN** the user executes the CLI with `--help`
- **THEN** the CLI displays parameter descriptions and usage guidance in English

### Requirement: Sine Wave Plotting
The system SHALL calculate sine wave data points for the given frequency and amplitude over a standard time range and render a plot using matplotlib with the specified line color.

#### Scenario: Rendering a sine wave plot
- **WHEN** valid frequency, amplitude, and color parameters are provided to the generator engine
- **THEN** the system generates data points and plots the curve with the specified line color

### Requirement: Timestamped PNG Export
When the export flag is enabled, the system SHALL save the generated plot as a PNG image named `senoide_YYYYMMDDHHmmSS.png` using the current local system timestamp.

#### Scenario: Exporting plot to PNG file
- **WHEN** the export flag is set to True and the plot is generated
- **THEN** a PNG file named `senoide_YYYYMMDDHHmmSS.png` with the current timestamp format is saved in the working directory

### Requirement: Headless Container Execution
The system SHALL configure matplotlib to use the non-interactive `Agg` backend (`MPLBACKEND=Agg`) so that rendering and PNG exports work seamlessly inside containerized environments without an X11 display.

#### Scenario: Execution inside Docker container without display
- **WHEN** the application is executed inside the Docker container without an X11 display server
- **THEN** the application completes plot rendering and PNG generation without graphical errors
