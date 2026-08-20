# New to the robotic press brake?

[TARİH: 01.05.2026 The Fabricator]

Automation Strategy

Tips reveal the best path forward

By

Tim Heston

A robot places a bump-formed part on a pallet. Additional parts in the batch will nest neatly on top.

Images: SafanDarley North America

P

ress brake automation pushes robotics technology. Operating a brake requires some finesse; it isn’t a simple pick-andplace operation. Even so, the job can be repetitive, especially as part quantities rise, and good press brake operators are tough to find. The last thing you want is to consume a skilled person’s time with repetitive tasks, especially when the job is physically taxing. Few view the act of heaving unwieldy workpieces all day as an attractive career path.

Say you’ve decided to invest in bending automation. You’ve looked at alternatives, like folders and panel benders, and determined that, for your available budget, floor space, and mix of part geometries, a robotic press brake is the way to go. How should you move forward?

To find out, The Fabricator spoke with Mike Ruediger, senior robotics application engineer at SafanDarley North America, Waukesha, Wis., about some initial steps you can take when moving into the world of robotized bending.

ABOUT VOLUMES

"Not every part can be automated," Ruediger explained. "Automation works better if you have higher volumes."

He clarified that high volume doesn’t necessarily mean a bending cell requires large batches. Today’s technology can be set up for some sophisticated part flow strategies, including kit-based production. Imagine a brake with a staged setup and automated tool changes, simulated offline to minimize on-the-floor setup time. It could be capable of producing a kit of parts that flow directly to welding or assembly.

Automation also works well for a family of similar parts, like enclosures. Volumes for individual items might not be high, but you can adapt the program to handle a specified range of frequently ordered geometries.

That said, if you’re forming workpieces that you’ll never see again, robotic bending likely isn’t a good option. For prototyping, manual press brake operation is probably your best bet.

ABOUT PART SIZE

Press brake automation has become especially adept at handling the extremes of the part size spectrum, both the very small and the very large. As Ruediger explained, safety and ergonomics play big roles here.

Small workpieces introduce pinching risks, especially if you’re forming them on an older press brake without modern safety systems. Meanwhile, larger workpieces ramp up labor requirements and introduce a host of safety and ergonomic issues, not to mention quality concerns. Hoisting large panels all day, operators tire quickly, and as they do, they might not support the workpiece fully through the bend cycle. Gravity makes the panel sag during the bend, potentially throwing your bend repeatability out the window.

END EFFECTOR STRATEGY

Determining the best end effector collection depends on a shop’s mix of material, including what portion of the part mix is magnetic. "If you have a lot of aluminum parts, we’re limited to mechanical gripping [like clamping and suction cups] instead of magnets," Ruediger said.

The idea is to develop the most repeatable end effector strategy for the part mix. "If you have magnetic material [like carbon steel], you can use a magnetic end effector that can be excellent for picking single sheets from a stack." A magnet can be engaged as the robot approaches the stack, allowing sheets to be almost "sucked" off the stack. This makes picking multiple sheets less likely. (Robot cells can have air knives and gauges that measures sheet thickness, but having a magnetic end effector just adds another level of protection against double-part picking.)

Besides magnets, end effectors can have a combination of suction cups and mechanical clamps. Clamps grasp part edges, while suction cups can grasp workpieces at the center of mass, providing support when needed for large flanges as they swing upward during a bending cycle.

Workpiece surfaces matter here. Say a piece has an oily surface left over from an in-turret tapping operation. "We find that oily surfaces can create stronger vacuum when picking, because you’re not pulling air through the edges," Ruediger said. "The oil almost acts as a sealant [between the suction cup and metal surface]. However, sliding forces become an issue as the robot moves the part between bends."

The risk of part movement makes smooth robot motion important throughout the bend cycle—a key element robot programmers watch for when setting up and running a workpiece for the first time, regardless of the part’s surface condition. That said, the idea is to "engineer out" as many causes of process variation as possible, and smart end effector design can help minimize that variation.

Vacuum end effectors can be designed with specific vacuum zones, to accommodate holes and other part features. Some can work with the diamond patterns on tread plate. Meanwhile, custom designs can overcome unique handling challenges. Ruediger described one application where the robots used a "pin style" end effector. A group of pin pairs moved into extruded holes in a blank, then expanded to the hole edges to secure the workpiece to perform the bend cycle.

A bending robot riding on an overhead gantry forms a workpiece. Note the inverted tooling on the left, with the die on top and the punch on the bottom, allowing the robot to avoid flipping the part.

A robot lifts a piece from the reference table, confirming the part position before the bend sequence begins.

Bend programming and simulation—including stacking, robot movement, and automated tool changes—help optimize the bend process.

PARTS OFFLOADING

A formed part that isn’t easily stackable doesn’t rule out robotic bending entirely. Conveyors are always an option, especially for small, noncosmetically critical pieces that could slide or fall into a bin. Still, an unstackable part does introduce some part flow constraints.

Thankfully, modern software can sometimes make the seemingly unstackable stackable. It simulates how different parts can nest inside each other or be rotated slightly so one formed piece sits securely atop another. "You could have 20 different pieces in a kit," Ruediger said, adding that different pallet placement combinations could be simulated to accommodate process reliability (secure stacking, for instance) and the needs of downstream operations.

As parts are stacked securely, how can they be removed? How often will the fork truck need to move parts away from the cell? Ruediger said that bending cells today can be designed to accommodate both fork trucks and automated guided vehicles.

BLANK STACKING

You’ve determined that your formed parts can be stacked reliably. Now, what about part presentation? Blank stacking usually isn’t as challenging as parts offloading, but certain types of blanks can present issues, including punched blanks with existing forms. Embosses and similar forms can stack easily, but what about asymmetrical extruded holes and flanges?

These situations often mean the blanks stack in an offset or curved fashion, and as Ruediger explained, robotic bending cells today can pick from these kinds of stacks. "The robot comes in at an angle, and we anticipate the offsets made from extrusions and small flanges."

To ensure reliability often involves measuring the part dimensions to make sure one piece doesn’t catch on another. Robot movement could accommodate a one-material-thickness offset created by a flange, or a specific angle of the curved stack created when one blank with an extruded hole sits atop another. Once the robot knows the position, the program can briefly move in a direction that ensures the blank lifts cleanly away from potential snag points before lifting the part fully and continuing on its normal path.

ROBOT STYLE: FLOOR VERSUS OVERHEAD

A big benefit to the overhead gantry approach, Ruediger said, is that the arm can be quickly moved to the side, turning an automated press brake into a manual one. Robots traveling on an overhead gantry can handle parts in ways traditional pedestal robots can’t. This, combined with the fact the cell can become a manual system quickly, has made such robots a popular option.

Like anything, though, overhead robots have their tradeoffs. They sometimes can’t access certain areas without part interference. For instance, pedestal robots can do a better job at supporting large workpieces with long flanges.

Parts stacking can be another concern. An overhead robot can stack parts only so high, which in turn affects how often material handlers need to remove parts from the cell. Whether this is a benefit or concern, Ruediger said, depends on a plant’s overall part flow strategy, including available material handling resources.

EVERYTHING IN BETWEEN

Once you know the part can be lifted and stacked, you can next consider everything in between: handling and positioning parts between bends, as well as ensuring the robot knows where the part is in space.

The latter includes precise and sometimes redundant gauging. Most bending cells still have squaring, or reference, tables that allow the robot to confirm where a piece is before heading to the press brake to bend.

Sometimes, parts can be stacked in a tilted arrangement, effectively making the part-presentation pallet double as a squaring table. In these circumstances, the end effector vacuum doesn’t engage until the bellows behind the cups compress and the suction cups have firm contact—a subtlety that prevents any movement when the end effectors first grasp the blank.

That said, in many cases, the squaring table "acts as a kind of insurance," Ruediger said, "ensuring you have a repeatable, reliable process."

A reliable process is usually simpler, with fewer moves and trips to the regripping station. It can also involve supporting the workpiece throughout the bend cycle. A robot can also follow the punch as it retracts after bending—a helpful move if, say, a return flange traps a piece in a deep gooseneck punch. By rising with the ram, the robot keeps the part in contact with the punch until it clears the die, at which point the robot arm has the clearance it needs to remove the workpiece.

A robot moving upward with the punch represents just one of numerous strategies to help make robotic forming applicable to a greater variety of parts. Another example involves staging punches with a slight gap in between segments, allowing room for both long and short flanges and clearance for adjacent bends—no automatic tool change required. Automated tool change has made robotic bending more flexible than ever, but eliminating the tool change entirely while maintaining the same level of flexibility is even better.

For certain machines with the right toolholders and tools (specifically those with New Standard tangs), "you can do staged bending where the punch is on the lower toolholder and your die is on the upper toolholder," Ruediger explained. "This means that for certain parts, you don’t need to have the robot move out of the work envelope, flip the part, and move back into position. It just keeps the same orientation and transfers over to the next toolset."

START WITH PART REMOVAL

Today, some bending cells can be outfitted with Dutch hemming tables or even single-station hemming tools. Others use special tools like winged rotary dies that rotate as the punch descends (though they can’t yet be changed automatically). "The robot needs to follow the punch upward after every bend," Ruediger said. This clears the part away from the spring-loaded wing die, which would otherwise jostle the piece off the robot end effector as the ram retracts.

Robotic bending today can deal with large-radius bends, incremental (bump) bending, and more. A part might not look like a candidate for the bending robot, but in truth, the path toward a repeatable, reliable process might not be as arduous as you think.

This, Ruediger said, is why it can make sense to start your bending automation journey with the end in mind; that is, by considering your part removal options. If part quantities justify the effort and the completed parts can be removed reliably from the robot cell, bending automation becomes a real possibility.

Senior Editor

Tim Heston

can be reached at

theston@fmamfg.org

.

SafanDarley North America,

us.safandarley.com

NEW OPENING

OPEN HOUSE ON

JUNE 9-11

WARCOM USA INC.

by Westwood Metal Technologies

422 Ben Greene Ind. Park Rd, Elizabethtown, NC 28337

T. 336-482-5128 / 910-862-2688

MACHINES 100% MADE IN ITALY

www.warcomusa.com

|

sales@warcomusa.com