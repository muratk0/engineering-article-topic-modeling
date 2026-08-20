# Sheet metal CAD skills applied to leather

[TARİH: 01.12.2025 The Fabricator]

Precision Matters

Just in time for the holidays, learn how to use configurations to control flat and formed sheet stock for improving a leather dopp kit design

GERALD DAVIS

M

ainstream 3D CAD is great for sheet metal projects. It’s a tool with which to make well-behaved sheet metal models that are both visually and mechanically accurate—useful for generating flat patterns and other predictions of the sheet metal changing shape under the influence of tooling. When it comes to predicting the behavior of a sheet material like leather under the influence of sewing, 3D CAD remains a great planning resource.

Figure 1A

is taken (without permission) from packaging for a product offered by Tandy Leather. The dopp kit is a tough leather box to stuff in a suitcase when traveling. I’ve made several as gifts, and they’re always well-received. Tandy’s kit is fully ready for assembly. Having the piece parts punched and cut-to-size is what makes the kit so user-friendly.

CAD came into play when I was making a stiffer-walled variation of Tandy’s design.

Figure 1B

reveals some of the changes in what we will call the FMA Box. It has similar flop-over lid but replaces the tie strap in the original design with a latch. The latch works best with stiff walls, thus the need for stiffening panels covered with an inner box liner.

The goals for the CAD effort included creating:

A flat pattern for profiles of leather parts.

Sizes and locations for stiffening panels.

Stitching paths that match available tooling.

FIGURE 1A

The commercial design from Tandy Leather’s dopp kit is the inspiration for a CAD project.

FIGURE 1B

The FMA version of the box has a latch (not specified) instead of a strap for closure. The walls are stiffened with thin cardboard panels that are glued in a sandwich between the outer leather and the inner liner (deer skin in this project). We also stretched the width a bit to work to accommodate a roll of 81/2-in.-wide paper.

FIGURE 1C

The 3D CAD model gives a reasonable visual prediction of what the leather might look like. Note that the 5-mm perforation pattern enters and exits the bend with equal spacing.

Plan in 3D for the 2D

Viewed in 3D, the model resembles the finished item. To generate flat patterns in 2D, a CAD trick is used to flatten the "impossible" sheet metal corners. But before being tricky, there’s more about goals for the 3D model.

As with Tandy’s design, a pair of end caps are sewn into place to form the rectangular box. The floppy flaps on the end panels help retain whatever contents might be in the box when the lid is latched.

A hemmed edge in the main frame adds stiffness to the box’s opening. One corner of a tab of the end panel will be trapped inside that hemmed edge. A spacer inside most of the length of the hem keeps it open and adds stiffness.

Shop Tooling as a Design Constraint

An important design constraint in the FMA Box is its sewn seam.

Figure 1C

is a closeup of one of the corners ready for sewing. The sewn overlap of end panel with main frame controls the box’s finished size.

The manual sewing technique used in this project is saddle stitching requiring prepunched holes. For punching by hammer blow, forked tooling is available to make up to six holes per stroke on 5-mm spacing.

The 5-mm PERF PATH in

Figure 2A

is a consequence of the 5-mm tooling fork. The punch tool works great when the main frame is flat. A two-pronged fork works when going around the corners. The end panels will be punched to match this perforation path.

A CAD tip regarding linear patterns is shown in

Figure 2B

. The linear pattern of stitch holes has instances skipped where the hem is formed.

The flat pattern for the main frame shows the location of the stiffening panels. This was done by creating blind (0.004 in. deep in this example) Cut-Extrudes in the main frame so their profiles show up in the flat pattern.

FIGURE 2A

The flat pattern for the main frame shows the location of punching for the perforated pattern of stitching holes. It also shows locations where the stiffening panels should be glued. There are also centerlines to show where the box frame is expected to bend. And, of course, the overall size is correct, ready for one-to-one transfer to the workpiece.

FIGURE 2B

Linear pattern features have the option to skip instances. This is used for the blank stretch that arcs around the hemmed front lip.

FIGURE 2C

As with the flat pattern for the main frame, the flat pattern for the end panel shows the path for perforation and overall profile. The flat corner fill-ins only exist in the flat configuration; their formed counterparts only exist in the default configuration.

FIGURE 3

The finished box resembles the prediction. In the relaxed condition, it is with ¼ in. of the overall size. It can be constrained to be within 1/16 in. of the crafty goal, but the leather sags into its preferred radius.

The flat pattern for the end panel is shown in

Figure 2C

. As with the main frame, it will be printed one-to-one and then used to transfer to the leather workpiece.

When the bends in the main frame are formed, the inside interval between punched holes will shrink around the bends. The holes going around the corners on the end panel will be less than 5 mm when formed and greater than 5 mm when the end panel is in the flattened condition.

Ordinary Sheet Metal with Suppression Issues

The end panels were modeled as conventional sheet metal with open corners. In the formed configuration (named the familiar Default in this example), a sweep was modeled and mirrored to fill in the open corners and give the illusion of a cup-formed corner. The sweeps were useful for modeling the perforation pattern to align with the main frame. The sweeps and the perf holes are suppressed in the flat pattern configuration (named DefaultSM-FLAT-PATTERN, in this example).

When the DefaultSM-FLAT-PATTERN configuration is active, a Base-Extrude and a Cut-Extrude (for the stitch holes) are unsuppressed to fill in the open corners and to complete the stitch path in the flat condition.

Some effort was made with the resources of 3D CAD to adjust the size, the bend radii, and the seam overlap to get the punched stitch holes in both corners of the end panels to be symmetrical and identical. This was a process that required several iterations.

The best success in iteration was had by forcing the main frame’s perforation pattern to go around the corners nicely in both formed and flat condition. Then the end panel’s pattern was constrained to the main frame’s hole location.

The 3D model makes it practical to observe the advance and retreat of the linear pattern as the main frame’s size is edited. Starting with the front flap, adjust the bend radius for the flap to arrive with the pattern advancing around the corner and across the top nicely. Then repeat for the top rear bend, and so forth all around the sewn path.

Success from Planning

Figure 3

compares prediction to reality. The completed box features a carved trough to keep the thread below surface that the CAD plan lacked. It also has a latch that wasn’t modeled. Other than that, the resemblance is strong with this one.

In terms of precision, it is within ¼ in. in the unconstrained condition. It can be stretched or shoved into better than 1/16-in. tolerance, but the radii in the leather relax as soon as you let go.

For the crafty, this project used a K-factor of 0.5 for 0.090-in. material. The sandwich of inner liner and outer leather turned out to range between 0.070 and 0.1 in.

From front flap to rear wall is 33/4 in.—the goal was 4 in. Vertically, the predicted 43/16 in. arrived at 41/8 in. The overall width was supposed to be 813/16 in. and finished at 83/4 in., and the bottom corner radii were close to predicted at ½ in.

The main benefits of expending the effort in 3D CAD were in the punching plan for the stitching in the corners and in getting the stiffening panels located correctly. The result was almost as easy as Tandy’s to assemble.

Gerald would

love for you to send him your comments and questions. Please send them to

ddavis@fmamfg.org

.

GET EQUIPPED FOR 2026’S CHALLENGES WITH TODAY’S LEADING TECH

While planing for 2026, you need more than just a faster machine to face the competition in industry. You need a decisively advanced equipment that drives down your cost-per-part and helps to win more business.

Double-table high-speed machine

Single-table high-speed machine

High-speed pipe cutting machine

Large-format high-speed machine

THE HYMSON HIGH-SPEED LASER CUTTING SYSTEM IS ENGINEERED FOR:

◼

SURPASSING ONLY SPEED

Our high-dynamic performance and intelligent software convert ‘shorter cutting time’ into ‘higher productive output’, helping you achieve up to 200% boost in productivity

∗

◼

24/7 LOCAL SUPPORT

With our U.S.-based supportive team, we deliver on-site services, spare parts and commissioning support with rapid response, ensuring your production never stops.

◼

AN INVESTMENT FOR YOUR FUTURE

Partnering with HYMSON means gaining more than just machines, it is about building long-term resilience to equip for market fluctuations and technological shifts.

∗

Productivity increase based on internal testing and typical application scenarios. Actual results may vary.

As 2025 draws to a close, we are thrilled to look back on a year of exceptional partnerships. At HYMSON, we are incredibly proud to have empowered over 1,500 manufacturers with our new high-speed laser systems, and receiving over massive amount of resounding feedback.This success was further solidified by our reliable delivery and responsive after-sales support.

We extend our deepest gratitude to every customers who placed their trust in us. Thank you for making 2025 a record-breaking year! As the Christmas bell gradually rang out, we sincerely wish you a MERRY CHRISTMAS and a prosperous New Year!

PROUDLY SUPPORTED BY OUR U.S. TEAM FOR PARTS, SERVICE & TRAINING

Contact Us for Your Free, No-Obligation Productivity Assessment

Hymson USA, Inc.

Office & Service Address: 46782 Lakeview Blvd, Fremont, CA 94538

Showroom, Warehouse & Service Address: 1020

Chapel Street, Dayton, OH 45404

usa@hymson.com

(General)

rfq@hymson.com

(Quotes)

628-219-9530

www.hymsonlaser.net