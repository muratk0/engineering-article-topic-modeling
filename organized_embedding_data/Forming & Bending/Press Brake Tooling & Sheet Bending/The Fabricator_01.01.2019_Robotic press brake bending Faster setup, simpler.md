# Robotic press brake bending: Faster setup, simpler programming

[TARİH: 01.01.2019 The Fabricator]

Here’s how

By Kate Bachman

» Fast programming of part and robot follows LVD’s 10-10 rule: 10 minutes for CAM generation of the bending and robot program and 10 minutes for setup and first-part generation.

Photo courtesy of LVD Strippit, Akron, N.Y.

T

he first generation of robotic press brakes were a marvel to behold. Their human-free achievements elicited oohs and aahs and prompted speculation as to the limits of what they could do and how much time and labor they might save.

Once the novelty waned, fabricators scrutinized their robotic bending operations to determine how much time they were actually saving. Programming was complicated and slow. The setup process required a great deal of supervision and vigilance.

Over the last few years, robotic press brake OEMs’ efforts have been focused on simplifying the programming and setup of the most recent generation of robots. Bystronic, Amada, and LVD Strippit weigh in on how they have done so.

1. How have you simplified the setup and programming of robotic press brake bending over the last three years?

LVD Press Brake Product Manager Steven Lucas:

We recently introduced a robotic bending cell with a high-speed electric press brake. Programming for this press brake cell is handled completely offline. There is no need to physically "teach" the machine setup or the bending of the first part. The advanced software can calculate a complete collision-free path and also manage the dynamics of the part on the gripper. Unlike the robotic press brakes of the past, this modern bending cell requires little input from the press brake operator and is much more flexible in handling different types of bending jobs (including short-run, high-mix jobs).

Bystronic Applications/Technical Trainer Seium Teshome:

The Mobile Bending Cell setup is quick and easy. With only three communication cables, power, and air—all of which are quick-connect—the robot can be attached and running in 15 minutes. The operator only needs to be concerned about a roughly close alignment and then lets the robot measure the precise location of the press brake on its own. Our robot programming is done offline so the press brake can continue to form parts while the next program is being made. Once the program is ready to test, positional corrections can be made directly at the press brake with no need to go back to the programming phase.

Amada America Assistant Product Manager Bending Robotics Derrick Flores, and Product Manager Bending Robotics Phillip Picardat:

Like most software from 10 to 15 years ago, our previous generation of software for programming robotic cells was clunky by today’s standards and not very user-friendly. We streamlined it by creating a linear process, so that an operator/programmer doesn’t need 15-plus years of experience to take a product from start to finish.

The software generates all the robot’s motions, so fabricators don’t really have to worry about programming paths. They just program the part to the robotic cell.

» LVD Strippit’s recently introduced Dyna-Cell robotic bending cell comprises a high-speed electric press brake and an industrial robot to automate the bending of small to medium-sized parts in varying batch sizes at bending speeds up to 1 inch (25 mm) per second.

Photo courtesy of LVD Strippit.

» The robot features a unique gripper designed and patented by LVD. The gripper fits part sizes from 1 by 3.9 in. (25 by 100 mm) up to 11.8 by 15.7 in. (300 by 400 mm). Its compact size allows it to handle small parts easily and to go between tool stations. Operators can make bends on three different sides of a part without regripping. Gripper suction cups are controlled via offline software and activated according to part size. Because one gripper fits all applications, production is continuous and uninterrupted.

Photo courtesy of LVD Strippit.

» Using Bystronic’s press brake software, programmers can tweak any tool position using either direct input or by adjusting the positive or negative direction while watching the robot’s position. This makes it quick and easy to adjust any position or orientation.

Image courtesy of Bystronic, Elgin, Ill.

» Once the parts are positioned on stations, aids can be used to quickly add motion, fix axis limits, and change robot arm configurations with Bystronic’s robotic press brake programming.

Image courtesy of Bystronic.

During programming, operators or engineers assign a tool and indicate where they want the manipulator to grasp the part and process it through the bending process. Next they pick a bend line and step through the stages of forming the part. The software walks them through where to place the part at each tooling stage, where to set the backgauges, and how to take the part off the press brake. It is basically a click-and-drag method.

Even though the Arcam programming system that imports 3D models from SolidWorks looks simplistic, it is extremely powerful internally. After all the bends are assigned, programmers generate the program. They say "bend" and the software generates all the motions of the robot and drives the program through the steps automatically, moving the robot to the next bend and forming the part through all the positions.

In the final stage, they indicate how the parts should be stacked on the pallet—whether they are interlocked or stacked one on top of the other, for example.

After the program has been compiled, a 3D simulation of the entire bending process is available to show every robotic movement that has been created—the press brake moving up and down, picking up the part, bending it, and unloading it. In terms of positioning, the programmer can zoom in to verify positioning within a millimeter. It can be checked, double-checked, and triple-checked before it even goes out on the floor. One of the newer features of the software allows programmers to change the line code in 3D mode to manipulate the robot as much as is needed. So if they’re not satisfied with the robot’s default motions, they can adjust them.

» 1. At the beginning of the programming, the tools are already staged in the press brake.

» 2. The part now has several bends assigned to the robot and the program now has an attribute tree associated with it.

» 3. Here the bend line has been selected by the programmer.

» 4. At this point the programmer can make adjustments to the backgauges and the part itself.

» 5. Here is an example of the simulation of the programmed parts, from pickup, through forming the part, all the way to dropping the completed part onto a pallet.

Images courtesy of Amada America, Buena Park, Calif.

2. How has that simplification expedited the process?

Teshome, Bystronic:

All of our robot programs start with a bending program from our BySoft 7 software. Once this is imported to the robot manager, the program automatically populates all of the bending motions as well as the communication and timing with the press brake. The only thing the programmer needs to take care of is positioning the parts at each station and creating motion to and from the press. To do this, they define a reference point on the part and use it to position it throughout the workcell. The new autoposition feature instantly creates multiple reference points on the part, and the next reference point button will allow fabricators to cycle through them.

Efforts have focused on simplifying the programming and setup of the most recent generation of robots.

Flores, Picardat, Amada:

Your engineering group can create the programs offline, or you can have the robot operator do the programming. It’s simple enough that he or she can program on the floor, which gives the operator ownership of the system.

Either way, the machine should be running while the programmer or the operator is making the next program. This reduces downtime.

One of the biggest concerns in dealing with automation is that it’s very complicated. Amada promotes operator ownership. We have found that human-machine interaction is integral to the success of automated bending. We strive to make operation simple, leaving the complicated processing to be done through automation. The use of our 3i control and customized hand box gives the operators ease of use without overwhelming them. That way, a less experienced operator who doesn’t necessarily understand all the bend theory but who understands what the final result should be has control. By giving operators access to the programming software and making it easier for them to program and run it, they can get it up and running as quickly as possible. That saves time.

Lucas, LVD:

With the robot positioning and manipulating the parts, the automated bending cell minimizes the time "from art to part." The bending cell also provides the flexibility to operate in stand-alone mode when batch sizes are too small to benefit from robot automation. The robot can be put in "park" position and the press brake can be used manually.

One goal is for fabricators to use the robotic bending cell during the night (if they operate just one shift) or second shift. This way, they can be producing parts when, typically, no one or a smaller crew is working. During manned hours, they can choose to operate the machine manually or with the robot. Calculating actual savings can be done simply by comparing how many parts are being produced.

3. How much time can a fabricator expect to save?

Flores, Picardat, Amada:

Our new-generation software provides at least a 50 percent time savings. It literally cuts the programming time in half.

The automatic tool changer is another big time saver, and the automatic gripper changer allows a quick changeover to a new job within one to three minutes. And so now, not only has programming time been greatly reduced, the physical press brake setup time has been reduced as well because the auto mode simulations display how the robot is going to move on the plant floor.

Lucas, LVD:

The bending cell we’ve introduced offers fast programming of the part and robot following a 10-10 rule: 10 minutes for CAM generation of the bending and robot program and 10 minutes for setup and first-part generation.

Teshome, Bystronic:

The Auto Position feature eliminates the need to manually define or change reference points, saving two or three minutes of trial and error at each station. For a part that requires the thickness measurement, referencing (squaring) station, and a couple regrips, the savings can really add up. Currently the time to program a part averages 10 to 15 minutes per bend.

In spring of 2019 we will have a new version of Robot Manager that will reduce that programming time to two to three minutes per bend. That means a seven-bend part could be programmed in 15 to 20 minutes.

Contributing Editor Kate Bachman can be reached at

kateb@thefabricator.com

.

Amada America Inc.,

www.amada.com/america

Bystronic Inc.,

www.bystronic.com

LVD Strippit,

www.lvdgroup.com/us