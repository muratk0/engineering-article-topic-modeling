# Designing for the punch/shear combo

[TARİH: 01.09.2025 The Fabricator]

Blanking

The right approach optimizes the technology’s strengths

FIGURE 1

A conveyor whisks a cut blank to the next operation. A punch/shear combo’s greatest strength is its throughput—delivering parts ready for the next operation, no shake-and-break required.

Editor’s Note: The following is based on "Design for Manufacturing: Punch/Shear Combination Machines," presented at FABTECH 2025,

www.fabtechexpo.com

, by Fred Cooke, systems sales manager for Prima Power North America,

www.primapower.com

.

T

he punch/shear combination machine is an industry workhorse, but it’s not as ubiquitous as its turret punch and laser cutting cousins. It even gets less attention than the punch/laser combo, even though the machines have been quietly producing immense volumes of cut parts over the years. Punch/shear technology has progressed significantly, and it has several key advantages, the most obvious of which is its sheer capacity (bad pun intended) for flexible throughput.

The machine can achieve high material yields while sending parts immediately to the next operation—no manual denesting or shake-andbreak operation required (see

Figure 1

). If you have the right application, and you design your parts around the punch/shear’s strengths, you can reap its benefits.

Fundamentals First

Picture the tooling carousel of your typical turret punch press. Adjacent to this is a raked right-angle shear blade with a 60-in. leg that runs parallel to the turret (Y direction) and another 39-in. leg of the blade that runs in the X direction, parallel to the clamps that hold and move the sheet. That shear essentially replaces the two large cutting tool punch stations on a conventional turret punch.

The shear assembly comprises three components—an X blade, a corner blade, and a Y blade—that act as "one" right-angle blade, with the rake starting at the far end of the X blade and growing to the far end of the Y blade. The blade action determines whether your burr will be on the top or bottom.

The punches in the turret initiate the initial hits to create the part profile, while the shear blade destroys the skeleton and separates the parts. A typical sequence might go as follows: The shear blade cuts away portions of the skeleton, which drop below; a conveyor moves into place before that same shear blade parts-out and conveys the cut blanks away from the work envelope. Put simply, the scrap gets trimmed away and the parts get separated and sent on their way, usually into bins or an integrated sorting system (see

Figure 2

).

The shear can boost throughput significantly, but it also limits the thickness you can process. Specific thickness limits vary by machine brand, but the physics behind the process doesn’t change: The shear force isn’t as strong as punching force. A turret punch might process up to 5/16-in.-thick mild steel, while a punch/shear with the same punching tonnage might be limited to 0.157-in.-thick mild steel.

Just as in an old-school guillotine shear, the punch/shear combo machine’s right-angle shear uses hold-downs to ensure the part doesn’t pull during the cutting action. Hold-downs are less than 0.5 in. wide, and they’re tapered to account for lances, louvers, or other forms that might be close to the part’s left and top edges. If forms are too close (say, within 0.63 in.) to the edge, the shear can deform them (see

Figure 3

).

FIGURE 2

With the part conveyor retracted, the Y blade of the shear cuts web sections, which drop down to a chute (left). Once the conveyor moves in, the X blade of the shear cuts parts that drop onto the conveyor, which are immediately carried to a bin, sorting station, or integrated downstream process like panel bending.

FIGURE 3

The right-angle shear incorporates a sheet holder that clamps the material during the shear action. The shear holder can be programmed to not engage in certain areas, to accommodate louvers or other forms near the edge. Of course, the simplest approach might be to avoid close-to-theedge forms altogether.

FIGURE 4

The right-angle shear blade puts a downward burr on the inside. You can reduce the burr by reducing the blade clearance. The trade-offs include more frequent sharpening and shorter tool life.

FIGURE 5

Common-line cuts require clearance for the tool. Punching right on top of the sheared edge can create slivers or "whiskers" that can cause issues for press brake gauging and safe handling of the cut blank. Notch expansion positions the punches slightly inward, creating the needed clearance for the common-line cutting. In this nest, square punches knock out the common notches while the right-angle shear separates the part. On-the-part clamping and part edges sharing the sheet edge make processing even more efficient.

FIGURE 6

An asymmetric feature like this can cause issues for common-line cutting on a punch/shear machine.

FIGURE 7

Nesting software for a punch/shear system automatically identifies the part encroachment (on the top, see the square punch encroaching on the green area, a common-cut part). To solve for this, the nest layout software inserts web sections, as shown on the bottom. Depending on edge quality, though, a common cut still might be possible.

The hold-downs can be programed, so you can turn them off in different zones to accommodate forms that can’t move. Of course, if forms don’t need to be close to the part edge, it’s probably easier to move them in to avoid complications.

Because of the way the upper and lower blades are oriented, the sheared edge produces a downward burr on the inside and an upward burr on the outside. So, if the blade shears a part from the material it connects to—either scrap (web section) or a part cut along a common line—the burr on the released part will be down while the burr on the connecting material will be up (see

Figure 4

).

You can reduce this burr with a tighter clearance between the upper and lower blades, but this will require more blade sharpening and shorten overall blade life. If a part design can live with a slight burr, the shear blade clearances can be looser, which will require fewer blade sharpenings and prolong tool life.

Mind the Notch

This kind of part separation and skeleton destruction changes the way you nest. Say you have a collection of rectangular parts with notches. Because you’re separating the part, you need to destroy the notch, not just trim out its shape.

In a conventional punch press, you’d likely use rectangular tools to make a notch. In a punch/shear combination machine, you would use square punches to destroy the entire notch. This requires more hits, but considering the speed of a punch/shear machine—often up to 1,100 hits per minute, or 600 SPM on 1-in. centers—increased hits don’t slow the process significantly. Nibbling speeds for skeleton destruction can really fly, and using square punches (think of them as your "hammer") to nibble material works best, considering the increased side loading those square punches can withstand.

Most notch geometries can be destroyed by a square punch, with a few notable exceptions. You might have a part’s upper-left corner that can be removed by the right-angle shear. In rare cases you might have a large web section to deal with at the corner notch, in which case it would make sense to micro-joint the scrap section for later removal. (Repeatedly destroying a large web can add cycle time and reduce the life of your "hammer.")

FIGURE 8

This part is being formed on a panel bender, which gauges from the notch, not the edge of the flange. If the final edge is hidden in an assembly, edge quality concerns might not be an issue.

Getting the most out of a punch/shear involves using robust, simple tooling and a nest layout that allows you to use those tools effectively, with as many common-line cuts as possible without sacrificing edge quality.

Yield and Efficiency

You have two clamping strategies to consider. You can either use a minimum Y width (usually a little more than 1.5 in.) or you can clamp directly onto the parts themselves. This is where flat, consistent, high-quality material really begins to pay off. If you’ve got high-quality, straight material, you can now start nesting with the sheet edge being the edge of the part. Combine this with common-line cutting, and the processing efficiencies really start to add up.

The kinds of efficiencies differ, however, depending on what you’re nesting. An entire nest might be full of common-line cuts, which can shorten your cycle time, since you’re cutting two parts at once with every common cut. Clamping on the parts themselves shortens processing time even further, since you’re using the sheet edges at part edges. You gain speed, but you don’t necessarily improve yield. After all, your yield really doesn’t improve unless you can fit another part on the sheet.

Common-line cutting is especially beneficial on the punch/shear, but you need to ensure you can achieve good edge quality. This demands an ever-so-slight offset between your tool edge and the part edge it will be cutting. Cutting directly on top of a part edge can create tiny slivers (sometimes just a whisker or a hair) that can degrade your edge quality and, not least, make cut parts less safe to handle. This means you need an ever-so-slight gap when cutting a common line between two part edges.

This can create issues when you’re nesting common notches that will create the flanges to be formed into panels or boxes downstream. To avoid the edge quality, you program your square punch to "expand" and encroach into the notch area (by about 0.020 in., depending on the area and material). This strategy gives the nest the clearance it needs so that tools aren’t shearing directly on top of the part edge, giving you the best edge quality that your press brake operators will appreciate (see

Figure 5

).

This strategy works especially well when you have symmetrical parts that nest cleanly across the sheet. Problems arise with asymmetrical parts, however. Consider a flange with a cutout on one side but not on the other (see

Figure 6

). This can require another square punch tool that can encroach on the part profile line. If it’s encroaching into a scrap area, that’s not a problem. But if it’s encroaching into another part edge, that’s a problem.

Here, software will detect that encroachment and automatically apply a web between the parts (see

Figure 7

). Before you let that go and deal with the longer punching cycle time, ask downstream operations and the quality department if that part edge is really a concern, especially if it will be hidden in the final assembly.

The encroachment might cause issues for brake operators, who need a consistent edge surface for the backgauge fingers. However, the edge might not be an issue if the part will be formed on a panel bender, which gauges parts differently (such as on the outside notches, instead of the edge of the flange to be formed, as shown in

Figure 8

). If the bad edge doesn’t matter for the final part design or downstream operations, you can (within the nesting software) set a common-line tolerance. This will force a common-line nest layout, even though a tool is encroaching to create that asymmetric feature.

50 KW LASER CUTTING

CNC BORING MILLS

BRIDGE MILLS

MACHINING

50KW AND 30KW BEVEL CUTTING

TUBE LASER CUTTING

CNC TURNING

ROBOT WELD

PRESS BRAKE FORMING

BRING IT HOME!

Cupples J&J Company Inc.

www.cupplesjandj.com

rfq@cupplesjandj.com

731-571-7910

Hip to be Square

As you can probably tell by now, punch/shear machines operate best with a square punch. Again, they’re more robust and can take a beating—good for a production machine churning away at more than 1,000 SPM. This creates issues when you need to produce corner fillets with rounded edges. These can require a four-way round punch, which usually needs a web section, killing your chances for common-line cutting.

Chamfers have straight edges and, hence, give you a geometry better suited for common-line cutting. Special "star" radius tools can produce rounded corners and still allow for common-line cutting in certain thin materials—but "designing out" the punching challenge is always a good first step. When possible, go with the chamfer.

In fact, where appropriate, go with a straight line. Rounded edges require complex nibbling. A good rule of thumb: If you use three or more different tools to create a corner notch—due to rounded edges or other special shapes—you might want to consider that part for the laser or punch/laser combo.

Optimal Yield, Optimal Throughput

Getting the most out of a punch/shear involves using robust, simple tooling (remember, square punches are your "hammer") and a nest layout that allows you to use those tools effectively, with limited contours, few if any large web sections, and as many common-line cuts as possible without sacrificing edge quality.

Common-line cutting gives you the speed. It means the shear spends less time shearing web sections that become scrap and more time releasing and sending parts onto the conveyor.

But again, it doesn’t necessarily give you greater yield if you can’t fit more parts on a sheet.

But what if you weren’t limited to standard sheet sizes? This is one reason why integrating cut-to-length coil lines directly with punch/shear combos have become more popular. Not only is material less expensive per pound and easier to store, the leveling process is controlled in-house (no more crashing turret heads due to material distortion—though good leveling at the service center is still critical). The strategy also improves material yield, since material can be cut to the length you need.

The cut-to-length lines can feed a buffer or storage table or go into a tower, which can house a wide variety of material. From there, the punch/shear might feed a panel bender directly, then offloaded automatically. Some of the latest installations now are making great use of autonomous mobile robots, which deliver kits of parts to welding and assembly—downstream processes that represent the first time humans touch the parts.

Such lines work best with consistent material having nests that make the best use the punch/shear’s strengths: fast cutting cycle times, sending parts downstream as quickly as possible—no denesting, no manual shake-and-break—just smooth, flexible part flow, without the constraints and expense of the dedicated tooling stamping presses require.

Your Complete Source For Metal Fabrication

Medium to High Volume Fabrication and Manufacturing

Flat Sheet Laser Cutting

Tube Laser Cutting

Flat Bending

Tube Bending

Welding

Machining

Finishing and Assembly

Stocking and Kitting

Logistics

9001:2015

oesindustries.com

| 605-239-4884 |

info@OESindustries.com