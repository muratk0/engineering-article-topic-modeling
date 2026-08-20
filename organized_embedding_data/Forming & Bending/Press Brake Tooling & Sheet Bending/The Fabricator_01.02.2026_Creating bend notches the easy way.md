# Creating bend notches the easy way

[TARİH: 01.02.2026 The Fabricator]

Precision Matters

CAD comes to the rescue when a backgauge is not available on the brake

By

Gerald Davis

THEFABRICATOR.COM

› AUTHOR › GERALD-DAVIS

T

he incorporation of sheet metal in a product presents numerous design-for-manufacturing opportunities. Those in flatwork trades know about standards—for gauges of thickness, tempers of alloys, best practices in radii, tooling access, springback, stress relief, and more.

Since its inception, mainstream 3D CAD has offered convenient modeling with happy compliance to standards. Those in the CAD trade know that just a couple of sketched lines can create a visually accurate 3D model that predicts the reality of air bending reasonably well.

Figure 1

shows an example of modeling an L bracket with two sketched lines.

As a side note, full-blown CAM can be integrated into the 3D CAD design seat. Here we exclude the CAM features and tools. Being able to produce a flat layout with a design tool helps avoid false starts and is sometimes sufficient for fabrication of a one-off prototype.

Figure 1 shows a 2D sketch (upper screen shot) that is used to create a 3D model (lower screen shot). From a simple line sketch, the software takes care of modeling the bend radius, the uniform thickness, the neutral bend line, the direction of thickness, and the bend length (Z direction).

FIGURE 1 CAD makes it easy to model sheet metal. Just a simple 2D line sketch (upper screen shot) can control radii and thickness that will accurately unfold (lower screen shot). Some standards may apply.

Where appropriate, all modeling controls are based on user selection from standards presented by various dropdowns, radio buttons, and data entry fields.

THE PREDICTABLE PROCESS OF BENDING

Before exploring a new CAD tool/trick, let’s dive into what is old news to those who know it and perhaps useful insight for those who just inherited a Pexto: Bending sheet metal, whether in a leaf brake, folder, or a press brake, is a predictable process.

The neutral bend line is imaginary. It does not change in length as the sheet metal is bent. As a percentage of thickness, the k-factor locates where the neutral line is, which in turn predicts the length in flat layout.

Figure 2

illustrates air bending of a sheet metal part, with a stationary bottom V die providing three lines of contact and an upper punch providing one line of contact.

Those three lines of contact are all that will ever be touching during the bending cycle.

The workpiece must be positioned to locate the needed bend. If a backstop is not available on the machine, visual aiming is a routine solution.

The flat layout can be applied to scribe lines where the bending punch tip will make contact in the center of the bend. Aiming marks for the bending process can include a laser-scribed bend line or perhaps carved notches in the edges. However, notching little bend targets can be tedious. (That would be foreshadowing.)

Returning to Figure 2, as the punch moves downward, the punch tip presses the sheet metal into the valley of the lower die. In the air bending process, the sheet metal is not coined against the V die; it is merely overpressed into the desired angle and allowed to spring back into perfection. You earn the Long-Term Reader Merit Badge if you noticed that Figure 2 is a repeat from the July 2017 episode of this column ("What sheet metal shops wish you knew: Part III," The Fabricator, p. 42).

A GOOD K-FACTOR IMPROVES THE AIM

The amount of coining and the dimensional features of the tooling introduce variables in the way the sheet metal responds to being pushed beyond its yield point.

FIGURE 2 A stationary V die provides three-point contact with the workpiece. The tip of the upper tool presses the workpiece into place in the valley, never fully coining it.

FIGURE 3 Bend notches can be inserted into a flat pattern. There are settings for controlling the size and shape of the bend notch. The notches will be exported in the 2D flat pattern but will be suppressed in the formed 3D model.

These tooling variations have predictable results on the stretch of the metal, represented as a k-factor in CAD. For a given setup of tooling in a press brake and for a given gauge and alloy of sheet metal, a very accurate prediction of the flat layout is easy. The default k-factor (0.50) is usually close. It might matter a lot if there are several bends in the design.

Fabricating shops often publish their gauge tables (or other methods of calculation) to show k-factors that work with various tooling and gauge selections.

A CAD TRICK FOR BEND NOTCHES

Figure 3

presents a solution to the tedium of adding bend notches. Using a CAD tool circa 2024, I believe, select Insert>Sheet Metal>Bend Notch, making sure the flat-pattern is unsupressed. The resulting aiming notches only exist in the flat layout for export, so if you want to see what the bent bend notches might look like, simply export and import the flat, convert it to sheet metal, and add a sketched bend.

To resolve the foreshadowing, bend notches are no longer tedious little Cut-Extrudes. The k-factor is the key to success with aiming the bend notches for aiming, as it were.

Match the k-factor to the tooling and material and joy will be at hand. The default k-factor of 0.50 locates the neutral line 50% of the way into the material. It is more likely to be between 0.36 and 0.44, but that’s pretty close. For optimal results, contact your local press brake operator.

GERALD DAVIS

Gerald

would love for you to send him your comments and questions. Please send them to

ddavis@fmamfg

.

Editor’s Note: Files associated with this column, one of which is a sample part that uses a gauge table that was once used for sheet metal production, can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-dcad-downloads

.