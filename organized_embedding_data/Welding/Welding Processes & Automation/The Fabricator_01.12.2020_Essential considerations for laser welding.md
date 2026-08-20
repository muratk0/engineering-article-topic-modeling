# Essential considerations for laser welding

[TARİH: 01.12.2020 The Fabricator]

From component design to implementation

By

Travis Stempky

I

n every industry, products are being designed, redesigned, or reevaluated for better materials or functionality. The final products are made from many components, and these components need to be joined in some way. One of these joining methods is laser welding.

Laser welding uses a high-intensity beam of light to create a molten weld pool to fuse materials together. It’s a noncontact process, has low heat input relative to other fusion processes, offers high processing speeds, and produces deep fusion zones in a single pass.

Of course, to take full advantage of all these benefits and to ensure a high-quality, repeatable process, fabricators need to consider how laser welding compares to other fusion welding processes. Joint and fixture design also plays a role. As with any metal fabrication technology, smart implementation starts with a good understanding of the process fundamentals.

Laser Welding 101

Laser welding uses a beam of light focused to a small point at the workpiece. Generated from some form of medium, the light exits the laser source and begins to diverge. It is then collimated so that the beam is parallel and doesn’t grow. The distance from the exit to the collimation surface is called collimation length. The beam stays collimated until it hits a focus surface. Then the beam narrows into an hourglass shape until it becomes in focus at its smallest point. The distance from the focus surface to the smallest point is called focal length. The size of the focus spot is determined by the following equation:

Fiber diameter × (Focal length/Collimation length) = Focus diameter

The distance the focus diameter is within 86% of the focal area is called the

depth of focus

. If the focus position shifts outside this area, expect the process results to change. The larger the ratio between the focal length and collimation length, the larger the depth of focus becomes for a given fiber.

Larger fibers have a larger depth of focus compared to smaller fiber diameters. The larger ratios and fibers have a larger spot size that causes a decrease in power density and, therefore, a decrease in penetration.

There are two forms of laser welding:

heat conduction welding

and

keyhole welding

. In heat conduction welding, the laser beam melts the mating parts along a common joint, and the molten materials flow together and solidify to form the weld. Used to join thin-wall parts, heat conduction welding uses pulsed or continuous-wave solid-state lasers.

In heat conduction welding, energy is coupled into the workpiece solely through heat conduction. For this reason, the weld depth ranges from only a few tenths of a millimeter to 1 mm. The material’s heat conductivity limits the maximum weld depth, and the width of the weld is always greater than its depth. Heat conduction laser welding is used for corner welds on the visible surfaces of device housings as well as other applications in electronics.

Keyhole welding (see

Figure 1

) requires extremely high power densities of about 1 megawatt per square centimeter. It is used in applications requiring deep welds or where several layers of material must be welded simultaneously.

In this process, the laser beam not only melts the metal but also produces vapor. The dissipating vapor exerts pressure on the molten metal and partially displaces it. The material, meanwhile, continues to melt. The result is a deep, narrow, vapor-filled hole, or keyhole, surrounded by molten metal.

As the laser beam advances along the weld joint, the keyhole moves with it through the workpiece. The molten metal flows around the keyhole and solidifies in its trail. This produces a deep, narrow weld with a uniform internal structure. The weld depth may exceed 10 times the weld width. The molten material absorbs the laser beam almost completely, and the efficiency of the welding process rises. The vapor in the keyhole also absorbs laser light and is partially ionized. This results in the formation of plasma, which puts energy into the workpiece as well. As a result, deep-penetration welding is distinguished by great efficiency and fast welding speeds. Thanks to the high speed, the heat-affected zone (HAZ) is small and distortion is minimal.

Fusion Welding Comparison

Compared with other processes, laser welding offers the highest weld quality, lowest heat input, and highest penetration in a single pass. It has one of the highest ranges of material combinations and part geometries, is extremely controllable and repeatable, and is one of the easiest to automate. All this allows for new joint designs, and parts can be produced at a higher rate with less postweld processing.

Laser welding also has one of the highest initial investments, tooling costs, and weld joint fit-up requirements These must be accounted for when selecting laser welding as the joining method for your production process.

Joint Considerations

Deep-penetration welding allows for a single weld to replace multiple welds in different joint designs.

Figure 2

shows some typical laser welding joint configurations. Butt welds do not require a chamfer for thicker pieces, T-joints can be welded from a single side with full strength, and lap welds can be welded through the top sheet or along the seam. This allows for flexibility when designing your parts and weld locations.

Butt welding

requires high positional accuracy. Typical welding spot sizes are from 50 to 900 μm in diameter. The allowable positional tolerance must be less than half the beam diameter to ensure that the laser beam interacts with both sides of the joint. The allowable gap is typically 10% of the thinnest material or less than 50% of the weld beam diameter. Therefore, fixturing is critical in these joint configurations to ensure high positional repeatability and minimal gap.

Common ways to account for this are to design the part to be press-fit or to design robust fixturing. Some might use a vision system to ensure part positioning, but this will add some cycle time and complexity to the programming for production. It is also important to select the correct spot size at the part. Larger spot sizes accommodate larger variations but require much more energy input to achieve the same weld penetration depth.

FIGURE 1

Keyhole welding requires extremely high power densities and is used in applications that require deep welds.

FIGURE 2

Laser welding offers a variety of joint configurations: butt (1); lap, either along the seam (2) or through the top sheet (3); and T, through the top sheet (4) or from a single side (5).

FIGURE 3

This rigid fixture ensures a repeatable corner weld.

FIGURE 4

This lap welding fixture uses multiple clamps to ensure proper contact between two sheets.

Butt welding has many benefits. The weld strength is determined by the amount of weld along the seam, so the amount of penetration determines the amount of weld strength. Narrow, deep welds produce less heat input, which creates a small HAZ and limits distortion. It also allows for less material because no overlap is needed.

Lap welding

has many different considerations. The allowable gap typically is 10% of the top material thickness. The weld width and the fusion at the interface between the two materials determine the weld strength. Compared with butt joints, such lap configurations lead to higher energy input, a larger HAZ, and more distortion.

If welding through the top sheet (3 in Figure 2), the laser beam must penetrate through the top sheet and into the bottom sheet, and all that energy spent penetrating the top sheet doesn’t add any weld strength. Lap welds must be wider to increase their strength. This requires more energy input, achieved either through a larger spot size or by oscillation with a smaller spot size. If minimal distortion is critical, the weld should only partially penetrate the bottom sheet. If applications require low heat inputs and either low power or high processing speeds, partial-penetration joints can be ideal. They create a surface on the back side of the weld unaffected by heat input and, hence, a class A surface.

With partial-penetration welds, the minimum penetration into the bottom sheet should be between 20% and 50% for thinner materials and 0.5 mm for thicker materials to ensure repeatable fusion that accounts for variation in production. The easiest design for welding is to have the thinnest material on top and the thicker material on the bottom. If the top sheet is thicker, partial penetration into the bottom sheet becomes more difficult to control, which also makes it harder to maintain a class A surface on the back side of the weld.

Nevertheless, lap welding has many benefits. It doesn’t require high positional accuracy, which allows for fixturing without stringent positioning requirements. Compared to butt welding, lap welding has a larger process window, mainly because penetration depth is more flexible.

Joint Access and Postprocessing

Laser welding also allows for access to joints that were previously not achievable. Because it is a noncontact process, welding in holes and in tight spaces is possible if the beam width as it comes into focus is considered. This allows flexibility in joint design, and parts can be designed with less material.

Postweld heat treatment is not needed in many cases because of laser welding’s small HAZ and low overall heat input. There is also little weld protrusion on the top or back side of the weld that needs to be machined after welding. The process can have minimal spatter to create visually clean welds, especially with the addition of shielding gases. This eliminates the need to do a lot of postweld machining and cleanup.

Fixture Design Considerations

Fixture design needs to be much more accurate for laser welding than for more traditional welding processes. Since it is a noncontact process, the tooling can be closer to the part, but the tooling also must do all the positioning and tolerance control. The process has no added contact like in resistance and ultrasonic welding where the horns add pressure to ensure there is no gap. The laser also produces a small, repeatable melt pool and requires much tighter part tolerances. All of this must be considered when designing parts and fixturing.

Figure 3

shows a rigid fixturing for a corner weld. This style of fixturing is common for butt welding and edge welds for tubular or rectangular parts. The clamps are very close to the seam and apply pressure to ensure a minimal gap. There is no tooling above the joint that could interact with the weld beam as it comes into focus.

The configuration also provides clearance for a shielding gas nozzle if shielding gas is required for aesthetic purposes or for metallurgical reasons in certain metals such as titanium. Fixtures must repeatably hold the joint in the same Z position relative to the beam so that the laser beam is in the same focus position. This is critical to get the same power density to ensure repeatable results.

Lap welding requires less robust fixturing.

Figure 4

shows a typical fixture design. Instead of long, rigid clamps to hold the entire seam in place, multiple clamps ensure proper contact between the two sheets over a large area. Such fixturing can be automated with pneumatic clamps. In the example, a scanning optic quickly welds all the required joints. Galvo mirrors—high-speed mirrors inside the welding optic—position the beam for welding and provide all the motion for the weld path. This allows for a simple robot path.

For especially critical welds, a single large fixture, designed with the weld path machined out, can ensure ideal part fit-up. The fixturing method has higher tooling costs but is also very robust and repeatable. Applying a large load evenly across the part surface, such fixturing can be ideal for stamped parts with large variations in surface flatness.

Unleashing Creativity

Laser welding allows for creativity and some freedom in part design, as long as all the essential variables are considered. For example, what spot size is needed for a given process? Larger spot sizes offer more melt area and a larger depth of focus but require more energy to achieve the same welding depths.

Similarly, what joint configuration is best? Butt welding requires accuracy and process repeatability but can achieve strong welds with minimal heat input. Inversely, lap welding requires less accurate fixturing and has a larger process window but requires more heat input to achieve stronger welds.

With all of laser welding’s process considerations also come myriad opportunities. It’s a great tool to advance manufacturing with new, creative part designs that not only increase quality but also—thanks to fewer manufacturing steps, including less secondary processing—have the potential to reduce costs dramatically.

Travis Stempky

is a laser technology specialist at TRUMPF Inc.’s Laser Application Center, 47711 Clipper St., Plymouth, MI 48170, 734-454-7200,

www.trumpf.com

.