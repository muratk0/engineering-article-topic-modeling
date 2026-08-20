# Recording Press Brake Tool Geometry in a Controller Database

## Purpose

Press brake controllers may store geometric descriptions of upper and lower tools so that programmed operations can reference the installed tooling. The source material describes creating tool profiles by entering dimensions measured from a physical tool or taken from its technical drawing.

Tool data should be treated as controlled production information. Before use, compare entered values with the approved tool drawing, the actual tool identification, and the machine documentation. Any controller workflow, screen labels, sign conventions, and available profile options depend on the controller version and machine configuration.

## Information Needed for an Upper Tool

An upper-tool profile may require basic dimensions and a sequence of geometric segments. Relevant information described in the article includes:

- Overall tool height.
- Tool angle.
- Chamfer dimensions.
- Width-related dimensions.
- Individual line or segment lengths.
- Segment directions.
- Internal or included angles.

A profile can be built by entering each measured edge and angle in sequence. The article notes that a displayed angle may be incorrect when its sign convention does not match the direction of the corresponding line. If a profile check indicates an angle error, do not guess at corrections. Review the drawing orientation, reference direction, and the controller’s documented convention for positive and negative angles.

Some systems can generate a preliminary outline after the tool geometry has been entered. Such an outline is a representation of the supplied data, not independent verification of the physical tool. Review the completed profile against the approved drawing before releasing it for production use.

## Information Needed for a Lower Tool

A lower-tool entry may similarly require overall geometry together with groove and support details. The article identifies the following categories of information:

- Overall die width and height.
- V-groove angle and opening width.
- Groove shoulder or chamfer geometry.
- Left and right margins or offsets.
- Segment heights, widths, and directions.
- Handle or mounting-feature dimensions where applicable.
- The selected groove or profile type, such as a standard V-shaped, round, or square representation when those options are available.

Where the lower-tool profile is symmetric about a centerline, symmetry should be confirmed from the drawing or measurement record rather than assumed. Directional lines and signed angles must also be checked against the controller documentation. A reversed direction or incorrect angle sign can produce a profile that looks plausible but does not represent the actual tool.

## Verification and Safe Use

The article mentions entering a tool pressure-resistance value. This information should not be inferred from geometry alone or copied from an unverified example. Use only the tool manufacturer’s approved rating and the machine’s documented limits. Capacity depends on the tooling, material, bend arrangement, machine condition, and the applicable setup; it must be validated through approved procedures.

Before using a newly created or edited tool record:

1. Verify all dimensions against an approved technical drawing or controlled measurement process.
2. Confirm the unit system, datum locations, segment order, directions, and angle-sign convention.
3. Check that the selected tool type matches the physical tool and its mounting arrangement.
4. Confirm that tool ratings and machine limits are documented and suitable for the intended operation.
5. Have setup and production use reviewed by qualified personnel in accordance with the machine manual and site safety procedures.

Do not rely solely on an automatically generated profile or on-screen visualization. Incorrect tool data can affect programmed clearances, bend calculations, and collision-related evaluations. Any uncertainty about geometry, ratings, or controller interpretation should be resolved using the machine manual, approved tooling documentation, and qualified technical support.
