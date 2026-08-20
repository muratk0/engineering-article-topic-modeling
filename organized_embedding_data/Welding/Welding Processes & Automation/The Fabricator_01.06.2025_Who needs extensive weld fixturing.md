# Who needs extensive weld fixturing?

[TARİH: 01.06.2025 The Fabricator]

Tech Spotlight

Uncovering the potential of autonomous robotic welding

By

Tim Heston

W

elding automation in metal fabrication usually falls along a spectrum. At one end, upscale arc or even laser welding systems weld assembly after assembly, each precisely fixtured, each component precisely cut and formed. High volumes make it practical for welding engineers to truly dial in the process, even for complex components.

In these cases, traditional approaches to fixturing and teach-pendant programming make sense. Alternatively, a shop might turn to offline weld programming. Here, programmers simulate the operation offline, and, because the digital model never exactly matches the real part, operators tweak the program as necessary on the shop floor.

In recent years, however, a new kind of robotic weld cell has hit the market: autonomous robotic welding—where (grossly oversimplified) the robot "looks" at the part, then starts to weld.

Welding an Auger

Alex Burnham, product manager at Fairmont Machinery, Honey Brook, Pa., pointed to a robot welding a continuous helix shape onto a central shaft rotating on a headstock-tailstock unit. The cell used no teach pendant for programming. Instead, the operator standing outside the perimeter guarding viewed a digital twin onscreen. Cameras in the cell captured the actual position of the tack-welded assembly. The software compared the actual part to the model and adjusted as necessary. At that point, welding commenced.

Alongside the rotating headstock/tailstock, this particular cell had a static weld table as well as another table with a single-axis positioner. The robot ran on tracks to access the three different stations, so theoretically, the cell could run one different part after another. Again, no teach pendant was used.

As Chip Burnham, Fairmont Machinery’s CEO, explained, "The system located and scanned the part in 61 seconds, using a 3D camera. There’s no zero point in the fixturing. Then, it took 15 seconds for a laser interferometer scanner to locate the seams. Then we weld it."

He added that the laser interferometer scan eliminates the need for wire touch-offs, which required "a clean nozzle and perfectly trimmed wire. This new system bypasses all of that, and the no-touch laser scan is many times faster than touch-offs."

A robot welds an auger rotating on a headstock/tailstock positioner. The robot "finds" the workpiece and required welds, then commences the job.

Images: Fairmont Machinery

Instead of using a teach pendant, a programmer pulls up the job on a screen and defines the welds, desired geometries, and other parameters.

See It, Weld It

Fairmont Machinery, which recently entered a distribution agreement with Abagy Robotic Welding (

abagy.com

), offers an autonomous robotic welding platform called VisiWeld AI Robotic Welding. As sources explained, the system works with a variety of robot and torch brands and can be retrofitted to a variety of existing robot installations. It works best with robots that have through-wrist cabling, allowing space for a camera to be mounted on the arm. Robots can be in various configurations: mounted on a pedestal, on an overhead gantry, or on a track to access different welds on a large workpiece or different worktables in a multiworkstation cell.

The platform has been employed in applications requiring coordinated motion between the robot and workpiece (which can be on a rotating headstock/tailstock, trunnion, J hook, or other servo-driven workholding device). It’s welded small parts on simple welding tables, but it’s also tackled bridge girders and other large-scale welding applications, with robots welding meters-long seams as they travel down the track of an overhead gantry.

Each setup consists of cameras for viewing and recording the process, a 3D camera that scans and locates the part, and a laser interferometer that detects where the weld seam is, making the needed adjustments from the 3D file.

The software does need to know some information in advance. As Alex Burnham explained, operators load a STEP or similar 3D part file, then identify the weld joints, the joint geometry (fillet, butt, etc.), weld technique (stitch, stringer bead, or weave), and number of passes. They also identify which weld segments should be connected in a continuous pass, and what weld position the robot should use—horizontal, vertical up, vertical down, and so on—to access and complete the joint.

Operators view the preset weld parameters and can tweak some as necessary. In doing so, they can define certain tolerances. These include part fitup tolerances as well as tolerances for certain parameters like torch angles. "These tolerances say what the robot is allowed to do in order to avoid obstacles and complete the weld," Alex Burnham said. "The torch might need to move at a certain angle to avoid a collision with a clamp, for instance."

From here, the programmer can run a digital twin animation, to ensure everything checks out. Once the part is tacked and clamped onto a table (again, using no dedicated weld fixture), a 3D camera within the cell locates the part, the laser interferometer detects the seam adjusting path as necessary, then the robot commences welding.

High-Accuracy, Fast Turnaround Fabrication for Complex Geometries

IATF 16949:2016 | AS 9100D + ISO 9001:2015 | ITAR

Chip Burnham added that certain steps can be skipped, depending on the scenario. If parts have very consistent fit-up, the laser interferometer needn’t spend 15 seconds scanning to locate the joint. If a part has hard fixturing, the robot needn’t spend a minute scanning the area to locate the part and its orientation. The same goes for the process simulation, with the operator viewing the digital twin prior to welding.

He added, however, that most early adopters have opted to run some or all of these optional processes, mainly because of the niche in metal fabrication the technology targets: custom and high-productmix operations (where programming and fixture development time can be extensive) as well as manufacturers where robotic welding simply didn’t make sense because of upstream process variation.

Why Fixturing Matters

For the custom fab shop, eliminating the need for extensive weld fixturing can be especially significant. Custom shops that adopt automated welding can have rows of fixtures feeding their robotic welding cells. Each job requires a specific fixture, and building them all takes serious time and investment. Even if the fixtures are simple, with little to no machined components—consisting of, say, stacked laser-cut parts and off-the-shelf springs and stops—the fixtures still consume a lot of space on the floor.

This, Chip Burnham said, is where the autonomous robotic welding technology fills a need. Instead of complex fixturing, an operator can tack-weld an assembly together, then clamp the piece on a table or multiaxis positioner. Operations might use a few custom fixtures to, say, account for heat buildup during welding. In other cases, a shop might develop fixtures to address weld access requirements. For instance, the robot might complete interior welds, then pause to allow the operator to place the final piece in a custom fixture. Custom, high-product-mix manufacturing environments never come without exceptions, but as sources explained, for most of a fabricator’s product mix, the autonomous welding technology can eliminate the need for dedicated fixtures.

At this writing, most installations have involved gas metal arc welding (GMAW), but some new applications incorporate wire-fed robotic gas tungsten arc welding (GTAW, or TIG). "There are trade-offs with TIG," Alex Burnham said. "You will need to laser-scan every seam. But regardless, the system does work with TIG."

Like any other technology, the autonomous welding platform does have a few limitations. It accounts for nonprecision fit-ups, but not extremely poor fit-ups or extreme positional deviations between the model and the real part.

It can work with seam tracking and other technologies already integrated with the welding robot, but as sources explained, it does not replace these systems. Instead, it focuses on automated programming and simplified setup—most notably by eliminating the need for a custom weld fixture and teach-pendant programming.

As Chip Burnham put it, "High-product-mix operations in particular want to be able to tack-weld a piece, slap it down on a table, have the robot find it, and start welding."

Fairmont Machinery

,

www.fairmontmachinery.com

MANUFACTURING IS RETURNING TO THE USA

IT IS TIME TO AUTOMATE

2-3x Throughput | ROI in < 1 year | Superior Quality

Cobot Spot Welder // Cobot MIG Welder // Cobot Sander // Automated Rotary Table

www.prospotautomation.com

info@prospot.com

+1 760-407-1414

MADE IN THE USA

Scan to Learn