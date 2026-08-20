# General Principles for Multi-Step Press Brake Bend Programming

## Scope and Safety

Multi-step press brake programs organize a sequence of bends so that each bend can use its own angle, workpiece reference dimension, tooling selection, and related machine settings. The exact screens, terminology, available calculations, and motion behavior depend on the press brake, control system, tooling, and machine configuration.

Programming and operation must follow the machine manufacturer's manual, site safety procedures, and approved tooling limits. Foot-pedal operation, hydraulic system startup, machine motion, pressure holding, and any adjustment of axes or tooling should be performed only by trained, authorized personnel. Before running a program, confirm that the selected tooling, material, sheet thickness, bend length, and planned bend sequence are compatible with the machine and workpiece.

## Establishing Bend Data

A bend program begins with the basic workpiece and bend information. The article identifies several common inputs:

- Material category
- Sheet thickness
- A selected dimensional reference, such as an inside or outside dimension
- Bend angle
- Backgauge dimension
- Bend length
- Tooling or die selection
- Number of bends or program steps

The dimensional reference should be selected consistently with the drawing and the way the part will be inspected. Material and thickness entries should match the actual sheet being formed, since controller calculations and machine settings may depend on these values.

Tooling selection also requires verification. A program may allow a die or other tool to be chosen from stored options, but the operator must confirm that the physically installed tooling matches the programmed tooling and is suitable for the intended bend.

## Building a Multi-Step Sequence

For parts with more than one bend, create a separate program step for each bend. Each step can contain a different angle and backgauge dimension. For example, a sequence may require one bend at one angle and reference position, followed by later bends with different values.

The bend order matters. It should be planned to account for the changing shape of the workpiece and to avoid interference between the formed part, tooling, backgauge fingers, and machine structure. A sequence that is geometrically possible in a program may still require review at the machine before production.

## Backgauge Retraction and Clearance

Some programs include a backgauge retraction function. Its purpose is to move the gauge fingers away after the sheet has been positioned when the formed workpiece could otherwise contact or be obstructed by the fingers. Whether retraction is needed, and the required clearance and timing, depend on the part geometry, bend sequence, tooling, and machine setup.

If a retraction feature is used, verify its movement through an approved setup procedure before running production parts. Do not assume that a default setting is suitable for every workpiece.

## Automatic Calculations and Verification

The article describes a controller that can calculate an axis position after bend-angle data are entered. Such automated calculations are controller- and setup-dependent. They should be treated as a starting point, not as a substitute for validation.

Where the control provides angle correction, pressure-holding, timing, or related settings, use only values authorized by the machine documentation and the established production process. Confirm the first-off part against the required geometry and inspect for issues such as incorrect angle, inaccurate flange dimension, tooling interference, or unintended marking.

## Controlled Execution

After the sequence has been programmed, run it through the machine's normal approved operating procedure. Multi-step programs may advance from one bend step to the next after each completed cycle, with machine axes moving to the settings for the following step. Operators should remain alert to the programmed sequence and the position of the workpiece throughout execution.

Before repeating the program, verify that the part can be safely supported and repositioned for every bend. Stop the operation and follow the applicable machine safety procedure if movement, clearance, material positioning, or bend results differ from expectations.
