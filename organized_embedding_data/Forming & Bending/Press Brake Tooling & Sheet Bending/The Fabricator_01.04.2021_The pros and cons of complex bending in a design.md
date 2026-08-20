# The pros and cons of complex bending in a design

[TARİH: 01.04.2021 The Fabricator]

Expertise » Precision Matters

Bends have advantages, such as reduced part count, but sheet metal origami requires labor

By

Gerald Davis

Gerald would

love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

A

n assembled and exploded tote box tray is shown in

Figure 1A

. This design requires spot welding for the end plates and dividers. Riveting is specified for the handle. This project caught the attention of Reader Rick when he saw it in the February 2021 episode of this column. He observed that the end panels, as separate parts, introduce avoidable complexity and weakness.

His suggestion eliminates two parts from the flat nest, highlighted in

Figure 1B

. The frame floor and tray ends are to be bent from a single piece of metal. We shall explore Rick’s suggestion.

Figure 2A

shows legacy features that carry forward into the new design. We will keep the holes and the top flange for the handle attachment. The hemmed edges provide some safety and stiffness, so we’ll keep those. And the vertical flanges help keep things from falling out of the tray.

FIGURE 1A

This tote box tray (shown assembled to the left and exploded to the right) has separate end pieces that require welding. Why not make them part of the floor to start with?

FIGURE 1B

A suggested change is to bend the end pieces in place instead of welding them on after bending. The two separate end parts (highlighted) will be deleted from the design.

FIGURE 2A

Legacy features we need to carry forward are holes, hems, and flanges. The target sizes are noted.

FIGURE 2B

A two-step CAD technique is used to create a sheet metal flange. In Step 1 (left), the sketch for the sheet metal flange is edited to include the diagonal slope. In Step 2 (right), two flanges are added as a single feature because they share the same depth.

Mirror, Mirror to Save Time

As foreshadowing, this change is going to be modeled as a sheet metal flange, followed by sheet metal flanges, followed by a hem. That result will be mirrored and mirrored to complete the tray. There are many alternative methods for modeling this project. This demo is trying to show a shortest-path collection of CAD techniques.

The sketch for a sheet metal flange is shown to the left in

Figure 2B

(menu path to this sketch is Sheet Metal>Edge Flange>Edit Flange Profile). The sketch roughly matches our legacy 4-in. overall height and 1.25-in.-wide handle tab.

The two other legacy flanges are modeled as a single edge flange feature, shown with highlight to the right in Figure 2B. The author went with two flanges in a single feature because they share the same depth. It might be clearer for future editing to have modeled these as separate features.

The next legacy item is the hemmed stiffener along the diagonal edge.

Figure 3A

shows the sketch for the hem feature and the completed hem. The hem’s sketch was edited for good result in the flat layout.

Figure 3B

shows the sheet metal tray frame after two mirroring features are completed.

The holes for handle rivets are the next task.

The new unibody sheet metal frame is shown in

Figure 4A

. Magically, the rivets shown (to the left) are passing through the sheet metal shown in Figure 3B. As a side note for this demo, the rivets were modeled as a derived pattern based on the hole pattern in the handle part.

To demonstrate a solution to a design intent, the rivet holes (to the right in Figure 4A) were created using an Assembly Feature (Insert>Features>Assembly Feature>Hole>Hole Wizard). The setting for "propagate to selected" is selected, and only the tray gets the treatment.

The design intent for the rivets is to have the handle’s design control the location of its rivets in the frame. The handle design is suspect because of its arcane method of construction.

The completed tray, shown in

Figure 4B

, has a lovely unibody construction. Perhaps the corners are spot welded, or perhaps the handle is enough to tie this box-kite frame together rigidly.

FIGURE 3A

A sheet metal hem feature is added to stiffen the diagonal edge. The hem’s sketch has been edited (left) for good result in the flat layout. For extra credit, adjust the length of the hem to match the 90-degree flanges to reduce the backstop movement needed on the press brake during forming. The result (right), where the changes to the end bends are complete for one-quarter of the tray, is also shown.

FIGURE 3B

The Feature Manager (left) shows that we’ve added a mirror of a mirror of a body to model the other three tray corners. The rivet holes await.

FIGURE 4A

The rivets (left) are modeled as a derived pattern based on holes in the handle. The rivets don’t realize they need holes to pass through. Suitable holes are modeled using an Assembly Feature (right) that are parametrically linked to the handle’s model.

FIGURE 4B

The tray, shown upside down to reveal the unibody construction, has been updated.

Design Review

So now we chat to see if we got Rick’s suggestion right. And ponder upon change for the better.

Hemming on a press brake is dramatic, requiring lots of time wildly flopping sheet metal. While it is not so bad on a folder-style bender, hemming is still at least a two-step process—make an acute bend and then spank it down to complete the 180-degree bend.

There are many alternative methods for modeling this project. This demo is trying to show a shortest-path collection of CAD techniques.

With drama in mind, the separate end pieces, being smaller flat blank pieces, might have been easier to fabricate than the unibody version is. Even though the welding adds time, much less time is spent part handling during the origami stage.

Less welding is always a blessing. Fewer seams mean fewer leaks. The bends add floor strength while reducing the overlap weight. Having fewer parts on the BOM also is a tremendous improvement.

Could we apply this same design inspiration to the main box? Would the box depth be too much for the brake? Will the handle be redesigned?

Press Brake Louver Tools

Capacity to 12GA Stainless

3" Louver Tool $850 3"/4"/6" in Stock

DEALERS WANTED

www.punchtools.com

Tel:

604.521.6444

Toll Free:

1.800.668.4996 •

Fax:

604.521.3143

Website:

www.punchtools.com

•

Email:

sales@punchtools.com

Proudly Made in Canada by Punch Tools

603-402-3055

Automated Layout

Technology™

"It easily doubles our output - no mistakes"

Plant Manager • Papp Iron Works

The first automated marking machine created specifically for the layout of commercial handrails, stair stringers and so much more utilizing your steel detailer’s dxf files.

Cut fabrication time by more than 50%

Ensure the highest level of accuracy

Boost your profit margins!

Lay out complex geometry in seconds

Designed to replace your existing fabrication table

"The guys love it. They jumped right in on it and have been working to make the most use of it. Great purchase."

Nat Killpatrick • Basden Steel Corporation

"I think it’s fair to say that this machine continues to exceed our expectations. We are very happy with it."

Visit

AUTOMATEDLAYOUT.COM

for a Quote

Reliable Leveling and Deburring.

Metal quality at its best. Deburring and edge rounding, double-sided in a single pass. Precision leveling for flat and stress-relieved parts and sheets. Optimize your downstream processing with ARKU.

www.arku.com