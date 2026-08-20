# Specifying Functional Tolerances for Formed Sheet Metal Parts

## Purpose of Tolerance Specification

Sheet-metal parts are produced through cutting, forming, finishing, and sometimes secondary operations. Their final geometry is affected by material thickness, alloy behavior, rolling direction, tooling, bend sequence, cutting heat input, fixturing, and inspection condition. Therefore, blanket tight tolerances on every feature may not reflect the functional needs of the part or the variation introduced by the manufacturing sequence.

Tolerance requirements should be assigned according to function. Features that control assembly, sealing, mounting, hardware engagement, or interface with rigid mating parts may need explicit control. Non-critical edges, tabs, and cosmetic features can often use less restrictive requirements when their variation does not affect performance.

## Consider Material and Forming Effects

Material designation and nominal gauge alone do not fully define sheet behavior. Gauge thickness can vary among material families, and incoming thickness variation can affect bend deduction, formed flange dimensions, and final fit. Specifications should account for the material condition used for production rather than assuming nominal thickness alone determines final geometry.

Elastic recovery after bending can change final angles and dimensions. The amount of springback depends on material properties, thickness, bend radius, tooling, and other process conditions. A formed feature should therefore be toleranced with awareness that a nominal bend angle or flange location may vary after release from the tooling.

Rolling direction can also affect bending behavior. When grain direction is important to cracking risk, springback behavior, or structural performance, it should be identified on the drawing or otherwise agreed with the fabricator. Part nesting and rotation can change the orientation of a part relative to the sheet, so critical orientation requirements should not be left implicit.

## Account for the Full Manufacturing Sequence

Cutting processes primarily establish flat-pattern features, while bending establishes the three-dimensional relationships among flanges, holes, and edges. A hole may be accurate in the flat blank but shift relative to another feature after several bends. Tolerances across multiple bends should therefore consider accumulated variation rather than relying only on the accuracy of the cutting operation.

Heat introduced during thermal cutting can contribute to distortion, particularly in large panels or dense patterns of cut features. Where flatness or feature location is critical, the drawing should identify the relevant inspection condition and functional requirement. The process route should be selected and verified by qualified manufacturing personnel.

Tooling condition, machine repeatability, material lot changes, and production volume can affect consistency. Prototype results may not represent long-run production behavior. Requirements intended for repeated production should be reviewed against the planned material, tooling, inspection method, and fabrication sequence.

## Place Features with Respect to Bend Zones

Features near a bend line can be distorted as material stretches and compresses through the bend region. Holes, slots, and cutouts close to bends may become oval, shift in position, or interfere with tooling. The article presents the rule of thumb that holes should be kept outside a clearance zone defined by material thickness and bend radius; however, the appropriate clearance must be confirmed for the actual material, tooling, bend geometry, and required feature function.

When a feature must remain highly accurate after forming, consider whether it should be moved away from the bend, located on a stable flat area, or produced through a planned secondary operation. The final process choice should be defined with the fabricator and performed according to approved procedures.

Short flanges can also be difficult to form because the part may not be adequately supported by the selected die. Minimum practical flange length depends on sheet thickness and tooling geometry. A preliminary manufacturability review is appropriate when a design includes narrow lips, short return flanges, or other features with limited tooling engagement.

## Dimension from Functional Datums

Chained dimensions across several bends can create tolerance stack-up. Critical dimensions should be referenced from functional datums or directly between the features that must mate in assembly. This makes the design intent clear and helps distinguish dimensions that must be controlled from those that may vary.

Geometric tolerancing can be used selectively to communicate requirements for position, profile, orientation, and related functional relationships. It should not be used as a substitute for identifying the actual assembly condition, datum scheme, and inspection approach. Requirements should be clear enough that a fabricator can determine which features are critical and how they are to be evaluated.

## Include Finishing and Hardware Conditions

Coatings and plating add material to surfaces and can reduce clearance in holes, slots, press-fit locations, and mating interfaces. Dimensions for hardware and assemblies should be defined for the relevant condition, such as before finish or after finish. The required condition should be stated explicitly where it affects fit.

Hardware insertion also depends on hole geometry, edge condition, burr removal, material condition, and the intended installation method. A laser-cut hole should not automatically be assumed equivalent to a drilled or machined hole for every hardware application. Hardware-related dimensions should be coordinated with the applicable hardware requirements and validated in representative production conditions.

## Design Review Checklist

Before releasing a sheet-metal drawing, review the following:

- Identify features that are critical to assembly or function.
- Define material, thickness basis, and any critical grain-direction requirement.
- Evaluate dimensions that cross one or more bends for stack-up risk.
- Keep sensitive holes and cutouts clear of bend deformation zones where possible.
- Confirm that short flanges and complex bends can be supported by the intended tooling.
- State whether dimensions and clearances apply before or after finishing.
- Define functional datums and inspection conditions for critical relationships.
- Consider a secondary operation when a critical feature cannot reliably be achieved through cutting and bending alone.

Final tolerances and process plans should be reviewed against the machine manual, approved tooling limits, material data, and the capabilities of qualified fabrication and quality personnel.
