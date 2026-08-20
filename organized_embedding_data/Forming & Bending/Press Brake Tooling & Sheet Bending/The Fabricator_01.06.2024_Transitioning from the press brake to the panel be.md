# Transitioning from the press brake to the panel bender

[TARİH: 01.06.2024 The Fabricator]

Bending Basics

Different bending methods can alter your bend calculations

Steve Benson

I

n last month’s column, we were looking at the differences between bending on a press brake and a panel bender (see

Figures 1

and

2

). The reader’s company purchased a panel bender and had issues in assembly because they were using the same flat blank that was developed for their press brakes. Changing bending methods amounted to a 0.110-in. difference in the bend allowance over a single bend, which is a lot to deal with. How can they deal with the issue without rewriting every program?

We will discuss some valid ideas for solving that central question, including how to deal with machine-specific methods that change the inside bend radius, which in turn changes the bend allowance, bend deduction, and, ultimately, the flat part itself.

Accounting for Different Bending Methods

Variations arise because of the tooling used in different bending methods. Let’s break down the contributing factors. For perspective, I’m including not just the press brake and panel bender but also the leaf brake, or Cornice brake. Each creates the bend in its own way.

In a press brake, the descending punch applies bending force, pressing the sheet metal into a V die to create the desired bend. A panel bender, on the other hand, clamps the material and creates the bend with a wiping action, both in the positive and negative direction. The radius in the part is a function of the material’s ability to flow.

The leaf brake typically uses a bending leaf or beam to bend the sheet metal over the nose of the clamping tool. The operator adjusts the angle and position of the leaf to achieve the desired bend angle. The material’s ability to flow and the nose radius on the clamping tool produce the inside bend radius.

Press brake tooling, including the punch and die, is designed for specific bend radii and material thicknesses. The tooling geometry plays a significant role in determining the bend deduction.

Leaf brakes usually have simpler tooling than press brakes. However, the bend radius might not be as precisely controlled, and due to manual adjustment, the bending process could be more variable. Press brake tooling is often precisely engineered for specific radii, while leaf brake tooling may have less precision, resulting in slight variations in the bend radius and, consequently, the bend allowance and bend deduction.

FIGURE 1 A panel bender’s tools wipe the flange up or down. The approach usually makes the inside bend radius very consistent and repeatable.

FIGURE 2 In air forming on a press brake, the radius is "floated" in the die. The resulting inside bend radius forms as a percentage of the die opening.

zilber42/iStock/Getty Images Plus

Press brakes exert significant force uniformly down the bend line, ensuring consistent bending. Leaf brakes rely on the manual or hydraulic force applied by the operator, which may not be as consistent, leading to variations in the bend allowance and deduction. Overall, the differences in bend deduction between press brake and leaf brake can be attributed to variations in bending mechanisms, tooling design, material behavior, and operator control—not mathematics.

Software packages for press brakes and panel benders consider the specific parameters of the bending process, tooling geometry, material properties, and other factors to calculate the bend calculations accurately. The differences in bend deduction calculated by the software may reflect the inherent variations between the press brake and panel bender. However, the calculations are still being solved using the standard empirical formulas.

The nuances of each process contribute to slight differences. Though there are minor differences, they can significantly affect the final part size and yield slight differences in fit-up in assembly.

What to Do About It

So, how should you deal with current programs, and how should you cope with future programmed parts? If you’ve recently purchased the machine, the first step, of course, should be to consult with your machine provider.

For legacy projects, experiment with tooling adjustments to minimize the differences in bend deduction. This could involve fine-tuning the tooling geometry, clearance, and bending parameters to achieve more consistent results between machines. For example, if you are air forming on the press brake, narrow or widen the die opening until the bend allowance and deduction match what you’re achieving on the panel bender, at least as close as possible. If you are bottom bending on the press brake, you can change the punch nose radius to achieve the same results.

Also note the relationship between the clamping tool and wiping tool on the panel bender. When they’re close together, they produce a smaller inside radius; when they’re farther apart, they produce a larger radius. When the part is run on the panel bender, parameters probably should be left as is, as the radius and resulting calculations are much more complicated to adjust. Again, you’ll want to analyze the problem and discuss specific strategies with your machine provider.

Press brakes and panel benders do form radii in different ways, and software accounts for these differences. There could be numerous potential causes for the discrepancy. For instance, material properties of the sheet metal, such as its elasticity and ductility, can influence how it behaves during bending. Variations in material properties can lead to differences in the bend allowance and bend deduction between the bending methods.

Document and Communicate

Document the differences in bend deduction and results between the two bending methods and communicate this information with operators and programmers. Document and describe how to account for these differences during programming and production to minimize fit-up issues in assembly. Ensure that everyone involved understands the goal (smooth assembly) and the need for documenting changes at each machine. Make notes on the work order for both the operators and the quality control inspectors with blanket tolerancing changes, corresponding to assembly-based fit-up issues. What these notes are will depend on your specific application and the parts involved, but to illustrate, consider the following hypothetical example.

Say you need to assemble a part formed on the panel bender with another part bent on the press brake. You might keep your panel bender parameters as is and choose to make changes to parts formed on the press brake. If the bend allowance is smaller or larger than it should be, changing the inside bend radius is easy to accomplish: You’ll start with tooling (including the appropriate die opening, if you’re air bending) that creates a radius, bend allowance, and resulting overall dimension that mates cleanly to your parts formed on the panel bender. You could add something like the following to the paperwork:

Tooling/bend radius change:

When Part No. XXX is run on XXX machine, change the tooling to X.XXX (explain purpose) by adjusting parts within the customer-allowed tolerance. Use a X.XXX die opening, and look for an inside bend radius of X.XXXX

.

Tolerance change:

Hold dimension XXX-0.000/+0.XXX

. Again, the details will depend on the circumstances.

Future Projects

Continually monitor and analyze the bend allowances and deductions used on both machines and identify opportunities for improvement. Implement adjustments to tooling, setup, programming, and quality control processes to reduce variations gradually, and improve consistency between the two bending methods.

Use your CAD/CAM software to compensate for the differences in bend deduction between the two bending methods. The software can adjust the bend allowances or deductions based on each part’s specific machine and tooling. This approach allows you to maintain a single set of part drawings and programs while accommodating the variations in bending. Also, be sure to incorporate all tolerances you have available in production.

Operator Training and Skill Development

As always, invest in operator training and skill development programs to enhance the skills and proficiency of personnel operating both the press brake and panel bender. Well-trained operators can better understand and manage the nuances of each bending method, leading to improved consistency. Again, these are all just general recommendations. There are plenty of different ways to approach the problem, depending on the specific application. Regardless, at least a few of the ideas I have laid out here give you a great place to start.

By implementing some or all of these strategies, you can effectively reconcile differences in bend allowances and deductions between press brakes, panel benders, and other bending methods. This will ensure consistent part quality and good fit-up in assembly while optimizing efficiency throughout the production process.

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362. The author’s latest book, "Bending Basics," is now available at the FMA bookstore,

www.fmamfg.org/store

.

Purveyors of Fine Machinery

®

Since 1983

EXPERIENCE

Quality tools for all your metalworking needs

Buy Direct & Save

13″ × 30″ Gearhead Lathe

Designed for advanced metalworking

Fagor

®

two-axis digital readout

Large swing and bed length

Allen-Bradley

®

controls for machining accuracy

8 Spindle speeds between 80 and 2000 RPM

Signature South Bend 3 V-way bed

SB1049F ONLY

$

18,995

10″ × 18″ 1½ HP Metal-Cutting Bandsaw

Exceeds the demands of frequent metal cutting

Centralized control panel

Adjustable hydraulic down feed

Full 45°–90° cut adjustability

4 Blade speeds between 144 and 377 FPM

2½-Gallon coolant capacity

G9744Z2 ONLY

$

4625

10″ Slow-Speed Cold-Cut Saw

Cuts slow to minimize heat and warping

Gear-driven blade for low-RPM cutting

Built-in coolant system with flow control valve

Quick-release handle for fast miter cut adjustments

Dual-clamping vise action for fast clamping

Four individually adjustable clamping jaws

T28366 ONLY

$

1395

Hand Punch

Punch holes in steel up to 3/16″ thick

Extra-long handle for increased leverage

Leverage multiplying linkage

½″ Punch and die

Work stop for repetitive operations

Heavy-duty cast-iron construction

T21321 ONLY

$

750

19½″ Floor V/S Drill Press

Execute high-performance drilling

3-phase variable-speed motor

Inverter for single-phase power

Spindle speed: 50–2000 RPM

Digital speed display

Rack-and-pinion table elevation

SB1125 ONLY

$

3750

200A MIG Welder

Industrial welder with exceptional control

Mig and stick welding up to ⅜″ thick

IGBT inverter improves efficiency

Adjustable amperage and voltage control with digital display

Arc force and wave control

Operates on 120V and 230V

G0882 ONLY

$

542

Heavy-Duty Ring Roll Pipe Bender

Create arcs, circles, and spirals

External pedestal with forward/reverse foot controls

Roll up to 1⅛″ nominal pipe

19/16″ × 19/16″ × 1/16″ square mild steel

2″ × 1″ × ⅛″ C-channel mild steel

Dual emergency stops

G0792 ONLY

$

4295

32″ Professional English Wheel

Form smooth, compound curved parts

Adjustable pressure handwheel

Quick-release lower cam lever

Lifting eyelet

3 Upper wheels

9 Lower wheels

T27621 ONLY

$

2300

1½ HP Portable Fume Extractor

Create safe, purified air

MERV-17 HEPA filter collects down to 0.3 microns at 99.97%

6″ × 10′ extraction arm to direct suction

Built-in damper for adjusting air flow

Combined filter surface area of 177.6 square ft.

Steel body with locking caster wheels

G0964 ONLY

$

4725

Please visit

grizzly.com

for up-to-date pricing.

Due to rapidly changing market conditions, our advertised prices may be changed at any time without prior notice.

WARNING! †1 : Cancer & Reproductive Harm

Some products we sell can expose you to chemicals known to the State of California to cause cancer and/or birth defects or other reproductive harm. For more information go to

www.P65Warnings.ca.gov

FINANCING AVAILABLE

23203