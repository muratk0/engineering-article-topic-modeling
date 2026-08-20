# How a Punch Press Acts Like a Press Brake

[TARİH: 01.03.2015 The Fabricator]

New tooling, machine designs, and software make complex forms possible

By Dan Caprio

Figure 1

This cut and formed piece was created entirely in a single setup on a punch press. Advances in tooling and machine designs made this possible.

S

ome shy away from using form tools on a punch press, especially those that create high forms such as flanges, and historically they have good reason to be shy. Forming on older mechanical punch presses created problems, mainly because of the manual mechanical adjustments that had to be made to the tooling. Moreover, a lot of forming just wasn’t possible, because the mechanical machines were driven with a flywheel, so there was no way to keep the ram down.

Timing everything could get complex, and it wasn’t unusual to see hangups—tools pulling the material up during their return stroke. They often didn’t give you the exact form you needed. The idea behind form tools was (and still is) truly elegant, because they allow you to eliminate those costly secondary forming operations. But if you have a tool crash regularly in your primary punching operation, a lot of those savings go out the window.

Both punching machines and their tools have become more precise over the years. Punch press hydraulics give you control over the tool’s position, allowing you to program the hover heights you need to perform various forming operations. Because punches no longer need to perform a full return stroke, you can perform complex forms—be it with a wheel tool, a hinge tool, a bending tool, or anything else—much more reliably (see

Figures 1

and

2

). For instance, a punch press can descend a wheel tool to the exact position needed to form ribs, and you can use roll tools that let you create flares around holes or elsewhere to the exact height you need.

The transition from mechanical to hydraulic punch presses occurred years ago, but two recent innovations have tackled some remaining challenges. One relates to programming, while the other concerns the production of higher forms, such as flanges more than an inch or two high. Today punch presses can create bends in sheet metal that until recently only a press brake could produce.

New Punch Press Designs

To form on a conventional turret punch press, you might have a clearance of only 0.984 in., or even less. Part of that space is taken up by the form die, which raises the material slightly, and then you have the material thickness. Some tools allow you to use a significant portion of that clearance, but as a rule, you can perform forms reliably in a space that’s only 50 percent of the total clearance minus the material thickness. That’s not much.

New punch press designs, however, have clearances that take forming into account. Some systems make room for up to 3 in. of forming space from the lower die to the upper punch. This allows for significant forming and bending, such as flanges up to 3 in. high. And if the flange is bent to less than 90 degrees complementary (as shown in Figure 1), flange dimensions can be even longer.

Figure 2

The ability to control the punch ram motion has opened the door to more forming possibilities on the punch press.

Figure 3

These parts look as if they were formed on a press brake, but in fact were bent on a punch press.

These presses don’t have the traditional turret setup, but instead use what’s known as a toolchanger design. In a standard turret design, the sheet runs between the upper and lower turrets. This offers quick tool change, of course—that’s why turrets were invented—but at the same time, the design inherently limits space, which in some cases causes problems with part interference. It’s just the nature of the beast.

In the tool-changer-style punching machine, the lower carousel is underneath the brush table, and dies emerge and retract through a die chute as needed between and during operations. This means dies move down and out of the way, which can be important for a lot of forming operations. For instance, forming a louver involves a tall bottom die, which can scratch the material as it’s moved around the table. The tool-changer machine prevents this by allowing the die to move down and out of the way between hits.

How Punch Press Bending Tools Work

All this opens the door for more forming possibilities, and not just for ribs, louvers, and other short forms, but also the kind of tall flanges that you’d normally form on a press brake (see

Figure 3

). The bending punch and die in a punch press are a hybrid between a panel bender and a press brake, mixed in with some unique attributes. The punch looks a little like a miniature hold-down tool on a panel bender, while the die has a V geometry like you’d find on a press brake die (see

Figure 4

).

The die body looks a bit like an upward-facing Pac-Man, and it actually rotates during the bend. This rotation folds the workpiece against a stationary upper punch, and the die’s degree of rotation determines the bend angle (see

Figure 5

). The radii you can achieve depends on the V-die design, which can be determined when ordering the tool from the manufacturer. Or, if you need to achieve a certain radius, such as for a profound-radius bend, the die rotates at certain degrees to bump the metal as the piece progressively moves forward. It’s bump bending, punch press-style.

Tolerances are extremely tight, both in the positioning accuracy of the machine and the machining accuracy of the tool, similar to the tolerances available on a modern press brake with precision tooling. Press operators also can input changes in thickness. Say one batch of material is on the lower end of the thickness tolerance window, while the next batch is at the high end, such as 0.055 in. for one batch and 0.061 in. for another batch. This can make a difference in the bend angle, but as long as the operator checks the sheet thickness and makes the parameter change in the program, the machine can account for it. A change in the program code is made (usually in the G06 line) that tells the ram how far to come down before it performs its operations.

Besides the 3-in. height limitation, there are other constraints to consider. Unlike a press brake operator, a punch press can’t flip a part over, so a part with both positive and negative bends can create problems. Also, the angle of bend is usually limited to 90 degrees or less; acute bends greater than 90 degrees complementary aren’t practical, for the most part (depending on the tooling you have). And because of tonnage limitations, the material can be only so thick. This varies, depending on your punch press and tooling, but typically it is up to about 0.118 in.

A punch press isn’t a press brake, but for the right application, it can perform like one.

Programming Strategies

When you bend on a punch press, your programming options abound. Traditionally, you program the forming sequence at a point where it won’t interfere with any other part. This usually means you’re forming near the end of a nest’s punching sequence, after most or all of the flat-part punching is completed.

Figure 4

This bending tool on the punch press resembles the hold-down tool on a panel bender. The tool descends to the programmed height and remains stationary during forming. Underneath the sheet, the V die (which looks a bit like Pac-Man) rotates to create the desired bend angle. The maximum angle of bend is usually 90 degrees.

At this point you may decide to bend all the flanges in a part at once. You cut the profile, leaving tabs connected to the nest to ensure part stability; bend the flange; then perform the final punching to cut the tabs and release the part so it can slide down the chute. This strategy can work well if you want to evacuate the formed part from the nest as soon as possible to avoid collisions with the tools.

Alternatively, you can punch the profiles (minus the material for the tabs) on multiple parts—say, all the parts in one row—form the bends, then send them all down the chute with the final punches that cut the tabs. This strategy reduces the number of tool changes and so can reduce the cycle time, but it works only if there’s no danger of interference between the flanges and the tooling.

Figure 5

In this bending tool setup for a punch press, the lower die rotates to fold the workpiece against a stationary upper punch, and the die’s degree of rotation determines the bend angle.

Tabs keep the part stable during bending, but where exactly you put those tabs, their width, how many, and how they’re cut depend on the flange geometries. Some pieces may call for only a few or even just one tab at a flat section of the part. Other times the bending operation itself can break the tabs. This can be useful when bump bending. During such a sequence, the microtabs holding the part in place break, and after the last bump, the part breaks free and slides down the chute.

Programming also needs to take into account how exactly these parts slide down the chute. For example, if a large, heavy part with a high flange slides down the chute incorrectly, its landing may be rough enough to change its bend angles slightly; or it may land on other formed parts with enough force to change their bend angles. You can overcome these problems by making changes to the program.

Software, the final piece of the puzzle, can automate the task of determining the punch and bend sequences.

Software Makes a Difference

It’s possible to program all these variables manually, but it can be complicated and time-consuming. There are plenty of details to consider, including which way to rotate the bend tool (the tool set rotates 360 degrees to align with the programmed bend lines); how to position and sequence everything to avoid interference; and which width of bending tool to use, depending on which tool you have in your library and the bend length you need. In more challenging cases, manually programming may not be very efficient, and it actually may take you less time to form the flanges on the press brake, especially if those parts are heading to the brake anyway for a few remaining bends.

This is where the final piece of the puzzle comes into play: software that can automate the task of determining the punch and bend sequences. With such software, you can feed the 3-D model of the part you want to bend on the punch press to the software, and it will unfold the part and suggest strategies to punch and bend it, based on the tools available on the machine. The offline program works similarly to offline bend programming for press brakes. It sees the interference points, knows just how the tool needs to rotate, and sequences it in an efficient way. As a programmer, you can either accept the software’s recommendation or tweak it manually to suit your needs.

More Options, Greater Throughput

Besides welding, bending remains one of the most common bottlenecks in the fab shop, which is why shortening or eliminating the bending operation makes so much sense. Tweaking a design so it can be formed on a punch press—be it a slightly shorter flange height, a different bend location, or anything else—can help reduce part costs in a dramatic way.

A punch press won’t be able to form every part, of course, but it can help relieve the bending bottleneck. A punch press isn’t a press brake, but for the right application, it can perform like one.

Dan Caprio is punching product sales manager at LVD Strippit, 12975 Clarence Center Road, Akron, NY 14001, 716-542-4511,

www.lvdgroup.com

.