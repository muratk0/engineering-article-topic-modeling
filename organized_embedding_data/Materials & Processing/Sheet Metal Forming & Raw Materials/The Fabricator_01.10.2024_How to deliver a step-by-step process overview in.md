# How to deliver a step-by-step process overview in CAD

[TARİH: 01.10.2024 The Fabricator]

Precision Matters

An engineering change order provides the perfect opportunity to explore some helpful modeling tools

Gerald Davis

Editor’s Note: CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-caddownloads

.

A

recent entry in the engineering change order (ECO) log simply stated, "Remove the bracket from inside the box." I was puzzled by this change. The bracket is essential to the design. The box is a functional accessory. Before arguing with the reviewer, let me show you my investment in this project thus far.

Sheet metal origami is a mixed blessing. It’s easy to model and fun to examine in 3D, but also often impossible to fabricate and difficult to understand on a 2D PDF. A variety of design constraints led to a sheet metal box that only has a few paths to success.

It was deemed necessary to illustrate at least one of those paths. This is the story of suppression for clarity.

Figure 1

presents a sheet metal box as it progresses from flat layout to final fold in seven bending stages. To minimize setup time, the jog bends (steps 1 and 2) are designed to be similar but in opposite directions. The remainder of the bends use an 88-degree tooling setup, an overhanging upper sash die, and lower V die setup. The upper tooling will be under abuse while forming the final four bends. This is light-gauge aluminum, so we imagine that a tall enough upper punch can withstand the strain.

FIGURE 1 A model for a sheet metal box is configured to show a sequence of bending operations. The flat pattern is shown top left. The first of two setups are for jog bends in opposite directions. The remaining five setups are for 90-degree bends using a top die that is cantilevered over the lower V die.

FIGURE 2 The Modify Configurations dialog will pop up after right-clicking on a child in the Flat Pattern folder and selecting "Configure Feature." There is a row button that creates a new configuration. Seven configurations were created, with appropriate suppress check boxes for each configuration.

FIGURE 3 A box with a bracket, with an exploded view on the right, is shown. To remove the bracket, remove the three nuts found on the outside rear of the box.

You’re invited to download the CAD models used to prepare these figures. They demonstrate the use of sheet metal tools like Jog Modeling along with mirroring and Unfold/Fold as time-saving tricks. We’d love to see your revisions and suggestions to improve the creation and ease of maintenance of the model.

Step by Step on How to Step by Step

If you’ve ever wanted to make your own stepby-step bending illustration, this demonstrated trick relies on the way the CAD system

unfolds

sheet metal models.

Unsuppress the Flat Pattern folder, and the part unfolds (if all of its children are also unsuppressed). That’s the normal CAD operation when the Flatten icon is clicked. It just toggles the suppressed state of the Flat Pattern folder.

Suppress the Flat Pattern folder, and the part refolds into a normal state. When it is suppressed, its children are completely ignored.

While the Flat Pattern folder is unsuppressed, each of the children may be individually suppressed to allow the bend to unflatten (also known as

fold

).

It is intuitively a strain to suppress the flattened model to fold, but that’s the fun of CAD. And that’s the trick. Configure each of the children of the Flat Pattern folder to be suppressed or unsuppressed; each configuration represents a bend step. The table shown in

Figure 2

allows one to create a new configuration. That’s how the configurations Bend 1 to Bend 7 were added to the model.

The Department of Redundancy Department

Note that configuration Bend 7 completely folds the part. It’s also the same as the default configuration.

Yes, this is slightly redundant to have two configurations that show the part bent the same way, but by not altering the default configuration, the Sheet Metal-Flatten tool remains happily unaware that other configurations are messing with its children. People not familiar with your fancy tricks with

unsuppressed flattens

might click on things in any order for any reason.

FIGURE 4 Here’s an exploded view of a bracket and its captive studs. The explode lines can be quickly created with the Insert Smart Explode Lines tool. For those interested, my CAD workstation is set up with the custom properties pane on the right and the Feature Manager on the left.

FIGURE 5 The engineering change order says, "Remove the bracket from inside the box." Does that mean we don’t need the bracket? Figure 6 to the rescue!

FIGURE 6 The engineering change order means that the bracket is currently removed from outside the box with a wrench on three nuts that clamp captive studs. The wrench can’t be used because there is no access. So we have to remove the bracket from inside the box—using screws, not captive studs.

FIGURE 7 Pack & Go is a handy way to branch a CAD design while preserving CAD relationships between files. The Select/Replace button is handy for editing. It was used to add "inside" to the filenames to branch them from the original design.

FIGURE 8 Here’s the progress on implementing the engineering change order: The bracket is removed from inside the box with no need for access to the rear outside of the box.

After the configurations are set up and as each configuration is selected, the part flattens appropriately. A few screenshots later, you’ve got your stepby-step story.

Constrained Features, Bless Their Little Hearts

The topic of the ECO is shown in

Figure 3

, a sheet metal box with a bracket. It is shown exploded on the left. The holes in the sheet metal box are modeled with the Hole Wizard, using settings for ANSI Metric, sized M4 loose clearance. Its resulting sketch pattern will be used to pattern the hardware models.

These holes are constrained to the location of the holes in the bracket. Wherever the bracket is, the holes follow.

Also note in Figure 3 that the exploded view has dashed lines to indicate where the item belongs. The Smart Explode Lines tool, which contributes to speedy work, was used to create them. The tool works nicely for the three nuts. For the bracket, it connects to the center of mass for the bracket. Dandy, if everyone understands what it shows.

Figure 4

is a view of my workstation—Custom Properties form on the right, graphics window in the middle, and Feature Manager on the left—as I completed an exploded view of the bracket’s sheet metal and captive hardware. Why the stud-and-nut design? Captive studs offer the advantage (over screws) of no-tool-required in the field. There are no slots for a screwdriver blade. It also makes for an easy surface to clean.

While we’re pondering the effort behind Figure 4, the Smart Explode Lines tool is a great time-saver. Here’s a CAD tip: When creating an exploded view, the Smart Explode Lines tool follows the components you move with each explode step. This influences how the explode lines connect. In this example, the nuts were exploded from the stationary bracket. Thus, three lovely lines automatically connect.

We return to the original ECO requesting that the bracket be removed "from inside the box."

Figure 5

shows a bracket inside a box.

In CAD, it is easy enough to delete the sldasm for the bracket, delete the model and pattern for the nuts, and to remove the dangling holes in the box. With a finger hovering over the delete key, a chat was engaged with the author of the ECO.

After a few moments discussing the problem with the reviewer,

Figure 6

emerged to explain the cause for the ECO. The bracket is currently removed from outside the box by removing three nuts with a box end wrench. However, no access is provided for a wrench to remove the bracket from the outside, so removing the bracket must be done from the inside.

Meaning and words are odd bedfellows. That’s an inside joke. Yes, the author of the ECO is a punster.

The clarity of the task is improved. Remove the bracket with only one tool with access from inside the box. The CAD task is to replace captive studs with captive nuts and loose nuts with captive nuts.

Our workflow will be to:

Use Pack & Go to make a starting point version (branch) for post-ECO.

Edit the starting point assembly by dissolving the assembly for the bracket and studs.

Replace the stud model with a model for a screw.

This results in the box becoming an assembly with M4 captive nuts and sheet metal. The exploded views can be removed or created as needed.

Figure 7

shows the Pack & Go dialog that was used to create the branch in the CAD models.

Figure 8

presents the post-ECO design. The bracket can now be removed from inside the box. Screws now pass through the bracket and into captive nuts permanently located in the box. No access to the back of the box is required.

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Please send your questions and comments to

ddavis@fmamfg.org

.

INDUSTRY LEADER IN MANUFACTURING LUBRICANTS AND EQUIPMENT FOR MINIMUM QUANTITY LUBRICATION (MQL)

EXTENDED TOOL LIFE

ENVIRONMENTALLY SAFE

LESS MESS

BETTER PART FINISH

COMMITTED TO RESPONSIBLE MANUFACTURING

Accu-Lube

®

manufactures a complete line of environmentally friendly metalworking lubricants using renewable raw materials. These fluids are specially formulated to provide superior performance and economy while helping to keep the planet safe from industrial contaminants by getting rid of the toxins required in flood coolant and eliminating harmful waste. Our mission is to help customers create cleaner, safer, greener facilities with our non-toxic, biodegradable lubricants that are second to none in performance, quality and value.

CONTACT YOUR ITW PRO BRANDS REPRESENTATIVE TODAY!

800.241.8334 |

www.itwprobrands.com/brand/acculube

©2024 ITW Pro Brands . AccuLube

®

is a registered trademark of Illinois Tool Works