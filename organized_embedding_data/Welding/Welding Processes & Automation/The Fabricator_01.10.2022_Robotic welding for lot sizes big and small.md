# Robotic welding for lot sizes big and small

[TARİH: 01.10.2022 The Fabricator]

Texas fabricator automates vessel welding and cutting

By

Jim Berge

Petrosmith’s new robotic system is set up to weld fireboxes.

W

hen first introduced in the late ’70s and early ’80s, robotic welding was seen as a panacea for welding high-volume, repeatable products. It didn’t take long before all the "low-hanging fruit" was picked, and robots were branded as effective only for high-volume applications.

A lot has changed in the past several years. I had the privilege of working with Petrosmith after the installation of their new robotic cutting and welding system, to help them get into full production, optimize their cutting and welding processes, and provide some hands-on practical training.

Petrosmith is a manufacturer of surface production equipment for the oil and gas industry. By nature, this business is a low-volume/high-mix environment. To automate the welding and cutting process in welded vessel parts, the robot system must have some innovative features to allow efficient welding of lot sizes as small as one.

Enter Cloos Robotic Welding and Autocam, a German soft ware company that provides soft ware allowing CAD-based "automated" programming. Autocam provides a soft ware called Moses that can automatically generate robot programs from CAD drawings for plasma cutting and welding.

Automating Labor-intensive Processes

Petrosmith was looking to enhance its manufacturing capabilities and automate certain labor-intensive welding processes to address bottlenecks in vessel manufacturing. As Mike Duffy, president of Petrosmith, Abilene, Texas, explained, "Petrosmith wanted to bring additional value to our vessel operation, and adding robotic automation is a great way to differentiate ourselves from many of our competitors and address production constraints in our head fabrication area. Adding the robotic cell has allowed us to quickly weld small lot sizes for our custom vessel operation, as well as make repeatable, high-quality head weldments for use in some of the other more standardized vessel designs."

Justin Hammond, vessel operations manager at Petrosmith, also understood that although employees may sometimes be concerned about the arrival of automation, there really is no need for concern.

"It is always the first question when employees hear about robotic/automation implementation into their environment. This is the same thing for Petrosmith. Our goal was not to reduce headcount, but rather focus on reallocation of resources to other parts of the operations where their skills could be better utilized," Hammond said.

Cloos provided a robotic system, including a 6-axis robot; a cutting table for cutting the heads; a 2-axis tilt and rotate positioner for welding components to the heads; a single, flexible fixture to locate and hold a variety of heads during welding; and the Moses soft ware package. It’s all integrated in a single, flexible system. The robot has a tool changer and can automatically change, as needed, between three tools: a single-wire welding torch, a tandem welding torch, and a 400-amp Hypertherm high-definition plasma torch.

The soft ware package contains a library of the physical components that will be welded, including the vessel heads, flanges, manways, and couplings, all in .dwg CAD format. The programmer begins by importing a CAD model of the head into Moses (see

Figure 1

). He then locates and defines all the holes to be cut according to dimensions from the part prints. Then, Moses calculates all the cutting paths and provides a complete robot program, which is ready to download to the robot to start cutting.

THERMA-TRON-X, INC.

Industrial Paint Finishing Systems

Your Best Finish Starts With Us!

Paint Finishing Systems Material Handling Innovations Turn-Key Solutions Water and Wastewater Treatment Equipment

www.ttxinc.com

|

sales@ttxinc.com

New and improved for more efficient and safer beveling

Get an edge on beveling!

Portable and stationary machines for burr-free weld prep.

– Milling performance increased by 30% or more with patent pending booster technology

– New patent pending spring technology increases insert life and worker safety

Start to finish solutions for increased productivity

859.331.8770

www.saarusa.com

FIGURE 1

A head with flanges is programmed for welding.

FIGURE 2

A multipass editor in software shows a two-layer, three-pass weld template.

FIGURE 3

This bevel-cut axial hole on a sloped part of the vessel head was made with a high-definition plasma-cutting robot. Cutting this manually would have been extremely time-consuming.

FIGURE 4

A typical robotic weld on a manway/flange.

The same is true for welding. The parts to be welded to the head are added to the CAD model that was developed for cutting. Then, the programming software calculates the welding paths complete with multipass welds where necessary, touch sensing, through-arc tracking commands, and everything else needed to generate the robot program. No post-editing is necessary.

The programming software provides the ability to develop templates for different types of welds. For example, some heavy-walled heads will have groove welds around the flanges, so the robot must first fill in the groove, often a multipass weld, before welding the fillet weld on top of the groove, which is also a multipass weld. Templates save a lot of programming time: For example, an entire three-pass groove weld can be stored in a template and quickly assigned to a particular weld.

These templates (see

Figure 2

) can include the variety of torch angles needed for each pass and can allow for unique situations, such as the different welding torch angles needed to weld around flanges that are close to one another or are on the steep part of the head.

To account for part tolerances, the robot searches for the beginning of the weld so it can strike the arc in the correct place, then uses real-time tracking to keep the weld in the joint the entire length of the weld. While tracking the first pass, the robot stores the actual position of the root pass. The subsequent passes are then offset to the desired distance from the root pass, which ensures the weld is placed correctly every time, even if the actual weld position varies in space.

In the cutting module, the programming software provides for axial cuts (cuts where the flange or coupling will be parallel to the centerline of the vessel) or radial cuts (where the flange will be perpendicular to the surface of the head). It also allows for beveled cuts to provide for a groove weld, and the bevel angle is freely programmable. This beveling operation is a huge advantage for both part quality and cycle time. Imagine manually laying out, cutting, and beveling an axial hole on the sloped part of the vessel head (see

Figure 3

). Not only does this require a very skilled layout technician, but it is also quite time consuming. With the robot, it takes about a minute to actually search for and make the cut.

The machine also marks the parts in low-amperage plasma marking mode to facilitate proper clocking of the head when it is manually located and tacked onto the vessel. As in welding, a touch-sense probe touches and locates the surface of the part before cutting to ensure the proper stand-off height when piercing. Then height sensing takes over during the cut to keep the stand-off height consistent throughout the entire cut.

After the holes are cut, the various parts are manually tacked in place, and a backing pass is manually welded inside the head. Then the tacked head is placed in the welding fixture, and the robot automatically drops off the plasma torch, picks up the welding torch, and performs all of the weld passes on the outside of the head.

As of this writing, the company uses the system for production parts, running many of them in automatic mode, but there are still many parts yet to be programmed. Once the software generates the part program, it can save it both on the robot’s hard drive and on the PC connected to the robot via ethernet and reused when needed. Even though many of Petrosmith’s products are low volume, many vessel types are repeatable so the programs generated will often be used again in the future.

Programs can be generated from a library of standard parts, and this programming can be done offline while the robot remains in production. Flanges, manways, couplings, and vessel heads have industry-standard designs. As such, these CAD drawings can be used as standard features, which Moses uses to build individual weldments and to calculate robot paths. The programming software also can optimize the position of the welds to assure the best weld quality (see

Figure 4

).

SIMPLE. VERSATILE. EFFECTIVE.

Mayfran’s

shuffle conveyors

can help you seize big operational benefits in any scrap application.

Backed by our lifetime service commitment trust us to delver a solution that lasts for the long haul.

Contact us at

INFO@MAYFRAN.COM

or visit us at

MAYIRM.COM

.

LARGE FORMAT LASER CUTTER & ENGRAVER

Metal, Acrylic/Plastic, Wood, Foam, & More

MADE IN USA

OPTIFLEX

VISIT Us D

BOOTH #B8919

I also worked with the Petrosmith team to add parts to the robot’s repertoire. We designed and built two welding fixtures in-house for locating large manways (flanges in the 18- to 24-in. dia. range) and fireboxes. These programs are written manually on the teach pendant the "old-fashioned" way since the programs are relatively simple and straightforward. The ROI was very good for these parts. A typical firebox takes four to five hours to weld manually, and about half an hour to weld with the robot. Of course, part fit-up, gap sizes, and repeatability are a challenge, and Petrosmith had to work on fine-tuning parts tolerances for robotic welding. But this is common in virtually every robotic welding application.

When first introduced in the late ’70s and early ’80s, robotic welding was seen as a panacea for welding high-volume, repeatable products. It didn’t take long before all the "lowhanging fruit" was picked, and robots were branded as effective only for high-volume applications. A lot has changed in the past several years, and robotic welding at Petrosmith is a prime example. Its vessel manufacturing has a robotic system with innovative features that allow efficient welding of lot sizes as small as one.

Software Is Key

The key to the whole process, and the technology that allows lot sizes of one, is the software. While the robot is actively welding or cutting, the programmer can be working on the next program on a PC. The key to extracting a favorable ROI from a robot system is to keep it cutting or welding. That’s the only time it’s making money. By programming the next part while the robot is actively running production, the ROI is optimized.

One goal of many robot users is to assign relatively unskilled labor to the robot, thinking that the robot will run perfectly as long as someone is there to simply load and unload parts. This may be true in some instances, but in many situations the robot operator should be more than just a button pusher. There are many applications that require an experienced welder to run the robot. This person may have to do more complex tasks such as post-weld inspection and repair, changing certain welding parameters as allowed, and simply recognizing when there is some kind of problem.

The right software can change the story somewhat. The welding parameters are proven and template-driven, so the operator actually loading and unloading parts does not necessarily need to be an experienced welder. That said, the programmer certainly needs to have experience in robotic programming and welding.

The hardware and the software can be scaled up to include complete vessels. Indeed, some companies in the U.S. use this same combination of hardware and software for cutting and welding complete vessels, welding the heads, flanges, and manways to the vessels themselves, and welding heads to vessels with girth welds.

Often, the girth welds use a tandem process with two wires welding simultaneously and controlled by two separate welding machines. This provides very high deposition rates, fast welding speeds, and lower overall heat input, which can be a big advantage in ASME code welding of vessels.

For other industries with very low lot sizes and very high mix environments, which are not based on industry-standard CAD components, the software Petrosmith used may or may not be the best solution. However, the industry is ever evolving, and there may be a robotic solution just for you.

Jim Berge

is owner of Berge Robotics LLC, 970-222-1753,

www.bergerobotics.com

.

Autocam, autocam.eu CLOOS,

www.cloos.com

Petrosmith,

petrosmith.com

Drill All Day, Every Day

HM0920 Mag Drill

2.313″ Diameter x 3″ Depth

Hidden Meter Cord

3 Speed - 250 / 450 / 700 RPM

Use HSS or Carbide Cutters

100% Hougen Reliability

Available Accessories

Two Year Warranty

Visit us at FABTECH Booth #B8657

800428-7811 SERVICE • INTEGRITY • RELIABILITY

HOUGEN.COM

PRECISION. CONTROL. SUPPORT.

THE NEW STANDARD IN FIBER LASER CUTTING.

The FiberPro

®

combines the industry-leading KOIKE design and manufacturing with the breakthrough KatanaT’1 controller. Fitted with superior drive control components for greater precision and smoother motion throughout the entire cutting range, we’ve eliminated the need for most secondary operations.

FiberPro brings high-quality output, improved productivity and performance beyond any other machine in its price range.

Heading to FABTECH in November? Visit

Booth #BC15515

to learn more.

SIMPLY BETTER BUILT

Laser | Plasma | Oxy-Fuel | Waterjet