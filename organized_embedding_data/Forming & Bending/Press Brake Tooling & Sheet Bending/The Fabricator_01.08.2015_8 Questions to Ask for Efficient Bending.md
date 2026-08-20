# 8 Questions to Ask for Efficient Bending

[TARİH: 01.08.2015 The Fabricator]

It boils down to giving the right information to the right people at the right time

By Tim Heston, Senior Editor

Photo courtesy of Getty Images

W

alk on the shop floor and you can spot a master press brake technician at work. He’s in the zone, his gaze focused on the tooling setup in front of him. He can visualize just how a flat part folds up, or if he has an advanced machine, he refers to a 3-D simulation in the control. The setup may be expertly staged and sequenced to ensure the workpiece, tools, and backgauges don’t interfere with each other (see

Figure 1

).

Offline software has made setting up even the most complex staged bending arrangement more cost-effective and practical. In the past some setups would have taken even a seasoned expert hours to set up and calculate. Now software simulates the bend cycle, and the press brake expert tweaks and edits to avoid possible collisions, or perhaps changes the sequence to match a certain operator’s preference.

Danny Brown knows this procedure well (see

Figure 2

). As head programmer at Mobile, Ala.-based S&B Machine Co. Inc., he works with customers to improve manufacturability, and he also programs jobs to ensure the programs work best for the operators who will perform the work.

The nuts and bolts of brake setup are pretty straightforward. You review the drawing and determine the inside bend radius and forming method: air bending, bottoming, or coining. If air bending (and these days, you usually are), you determine if the inside bend radius is realistic; if the specified radius is less than a certain percentage of the material thickness, the radius really can’t be made with air bending. As Steve Benson, president of ASMA LLC (and columnist for this magazine) has reported, that inside bend radius minimum for carbon steel lies at about 63 percent of the material thickness. If it’s any smaller than that, the bend turns sharp and you start forming a crease along the bend line. If the bend isn’t realistic, it’s back to reviewing the print.

If the radius is possible, you calculate the appropriate die opening. In air bending the radius forms as a percentage of the die width (according to Benson, for mild steel it’s roughly 16 percent of the die width). You then check to see if the right punch radius and die width are available and ensure the setup is within the tonnage limits of the press brake. You choose the closest available tooling, calculate the bend deductions, and you’re on your way.

Software has automated a lot of these calculations, but it can’t change physics, nor does it innately know how one operator performs versus another. This is the realm of the press brake programmer, supervisor, and department manager. At S&B, that job entails getting the right information to the right people at the right time. Brown emphasized that the procedures that follow work for S&B, but they may not work for every company. Regardless, all of it really boils down to asking the right questions.

Figure 1

Offline bending software has made staged bending setups much easier to develop.

Photo courtesy of S&B Machine Co. Inc.

1. Is This the Latest Revision?

A part is sent to the floor and is cut on the laser or turret, and then comes a revision, which includes a new material thickness. "Of course, changes in thickness can change a lot of elements in a brake setup when it comes to maintaining accurate dimensions and angles," Brown said. "That has been one of the greatest problems we have faced, and we’ve done a lot to eliminate that, including management software, so we’re able to flag a print before it’s even brought to the press brake to ensure it’s the newest revision."

2. How Thick Is the Material—Really?

This revision issue brings up a pervasive problem: Thicknesses vary depending on the material’s origin (see

Figure 3

). When thousandths matter, such variation can really throw a wrench into an operation. If you’re coining (which S&B does often for aerospace customers), the tooling is designed so that the punch stamps into the material at a certain thickness. If you’re air bending, a different material thickness alters your bend deductions. When it comes to precision forming, material thickness changes everything.

3. Where Is This Material From?

In a perfect world, a shop would be full of brandnew press brakes with angle measurement and correction. But most shops have a combination of old and new equipment, and this includes the floor at S&B Machine.

The shop overcomes the material inconsistency problem through a kind of batching. It’s a practice you won’t find in any lean manufacturing manual, but the solution does overcome the problems caused by inconsistent materials, a fact of life for many precision sheet metal fabricators.

To ensure a consistent setup, the shop develops its flat pattern, then cuts and bends a sample off a

certain

lot of a

certain

material from a

certain mill

. Brown then creates a setup sheet based on that specific material. "Once we have the OK off that lot, the material is flagged on our turret punches, lasers, and waterjets, so we know it’s to be used for a certain job."

The laser operator sees that these parts are flagged and, if needed, ensures that they’re oriented so that the cut parts will have the proper grain direction for forming. The material then is separated and stored with the formed sample part on top. When the job is scheduled for the brake, a supervisor retrieves the material, signs off on it, and delivers it to the operator. As Brown explained, with the right tools on hand and the right material, setup usually doesn’t take long.

Admittedly, this flies in the face of common lean manufacturing practices that shun work-in-process (WIP). But as Brown explained, this adds predictability to precision work and, ultimately, shortens the overall manufacturing time—not just for the challenging jobs, but for everything.

The cost of a small WIP buffer is nothing compared to spending hours at the brake trying to redo a challenging setup, just because the material thickness or other characteristics are slightly off. The long setup time not only holds up the precision job at hand, but also other jobs in the queue.

4. What Happened Last Night?

Running multiple shifts can create communication problems. Before they leave, first-shift operators usually talk to the second shift techs, but what if they can’t for some reason? What if an operator leaves for vacation for a few days or calls in sick?

From this problem came S&B’s "Start-off Sheet," which is basically an operator’s log. The previous operator creates a log that describes the materials and setups used during the shift, as well as common problems experienced with the machine, tooling, or material.

"The shift operator will add a few notes in the morning and at lunchtime, then some closing notes [at the end of the shift]," Brown said. "Those closing notes describe the overall production of the day. D

id we have any problems bending parts? Did we have any part quality issues? Do we need extra setup pieces?"

All this information now is available when the next shift operator arrives.

5. How Many Setup Pieces?

Overproduction is a classic waste in lean, but underproduction can starve an operation. New press brake technology has helped reduce test pieces to near zero in some circumstances. But again, not every shop is full of new machines. Sometimes even the most seasoned operator needs a few more test pieces for a run, especially for a low-volume part that requires a special operation like bump bending.

If volumes were high enough, of course, the shop could invest in a custom tool, but at S&B, most jobs don’t fit into this category. So operators need to rely on the art of the bump bend—sometimes penetrating a little more on the first hit; a little less on the second; and tweaking it ever so slightly throughout, removing the workpiece to check the bend with a laser-cut template. If they overbend one hit, they often need to scrap that piece and start again.

Figure 2

Danny Brown, head programmer at Mobile, Ala.-based S&B Machine, grew up in the sheet metal business. His family’s shop merged with S&B at the beginning of 2014.

Photo courtesy of S&B Machine Co. Inc.

Figure 3

Material thickness, which can vary depending on the origin, can throw a wrench in a precision bending operation.

Photo courtesy of Getty Images

.

It’s tedious, exacting work. So for these and similar jobs, the brake technician may need more test pieces to get the setup right. As Brown explained, that information goes into the operator’s log. Recording the number of test pieces is a good reference for setup improvement over time. The fewer test pieces an operator needs to reliably produce a good part, the better.

6. Can the Formed Piece Be Welded?

S&B has ramped up its robotic welding significantly in recent years. Brown attributes the company’s success in welding automation to the precision of its upstream processes, including bending.

Manual welders can adjust when the gap dimension isn’t exactly as it should be. Robots (unless they have high-end weld monitoring features) usually can’t, so precision forming is a must. For some parts, the shop actually produces a second welding fixture for the brake technician to use in the forming department. After bending so many parts, the operator places a piece in the weld fixture to ensure everything is within spec.

"If it fits in the welding fixture," Brown said, "there’s not going to be an issue."

7. Are Operators Cross-trained?

At S&B, many laser and punch press operators are cross-trained to some extent on the press brake; similarly, brake operators are cross-trained on the laser and punch press. This training helps a punch press or laser operator know, say, when and why grain direction is important on certain parts, and why material thickness really matters. Brake operators learn about the challenges of nesting and material utilization, especially when parts need to be oriented a certain way to account for that grain direction.

"Because they’re cross-trained, they’re able to interpret what the other operators see," Brown said, which ultimately helps everyone communicate and collaborate to get the job done right.

8. How Complex Is the Setup?

If complex jobs aren’t documented well, even a proven setup can take a long time. For consistently run jobs with dedicated tooling and proven setups, Brown has put different-colored electrical tape on tooling—for instance, white electrical tape goes with one top punch and bottom die, red tape goes on another top punch and bottom die, and so on. He then takes a picture of the setup and places it in the job traveler and (if possible) loads the image into the control for the technician’s reference. The tooling for that job is kept on a specific cart (see

Figure 4

). When it comes time to set up, technicians refer to the image and make sure the tape colors line up for all the punches and dies in the staged setup.

Offline programming and simulation, combined with new brakes with sophisticated backgauging, has made developing complicated staged setups a lot easier. This sounds like a no-brainer, especially if a machine aids the operator through the sequence with, for example, a 3-D simulation on the control, lights above the tooling showing which bend is next, or a foot pedal that slides below the next tool set in the bend sequence.

Just because a part can be staged-bent on one press brake doesn’t mean it has to be. Danny Brown, head programmer at S&B Machine, puts himself in the operator’s shoes and asks, How taxing will it be to form this up in one setup?

Figure 4

S&B organizes tools for consistent jobs on mobile carts.

Photo courtesy of S&B Machine Co. Inc.

But not every machine has an aid like a moving foot pedal or 3-D simulation. And even if a machine does show a simulation on the control, performing a complex bending sequence dozens or hundreds of times during a shift takes almost Zen-like concentration. Even a seasoned operator’s mind can wander.

Brown put it simply: "We try not to overwhelm the operator."

He empathizes because he’s been there. He grew up in his family’s sheet metal shop, Mobile Sheet Metal, which merged with S&B Machine at the beginning of last year. He’s worked with press brakes old and new, and he’s written out bend calculations with pencil in hand. "I’ve run everything from old mechanicals to precision hydraulics."

Much of Brown’s job involves working with customers on design for manufacturability (DFM), and a lot of that includes changes to errorproof the operation as much as possible. If it’s difficult to tell which way a flange should be bent, could the flat piece have visual cues? For instance, does a hole pattern need to be perfectly symmetrical, or can the hole pattern be slightly different on one side? This may allow the operator to compare the piece to the drawing to ensure that, yes, this particular flange needs to be bent this particular direction.

But DFM can’t errorproof everything, and this is where the human element comes into play. When planning for jobs, Brown tries to match operator strengths to the type of job. If an operator excels at maintaining concentration throughout a large stage bending operation, he programs a job as a multistep stage bend, allowing the part to be formed complete in one setup.

When such a job arrives at the brake, though, Brown makes sure the area is free of distractions, like loud radios and fans. Some technicians may wear safety headsets not only for ear protection, but also to minimize surrounding noise. In short, Brown makes sure the operator can get in the zone and stay there.

But as Brown has found, just because a part can be stage-bent on one press brake doesn’t mean it has to be. He puts himself in the operators’ shoes and asks, How taxing will it be to form this up in one setup? After several dozen pieces, even the best operators can trip up and, say, bend a flange in the wrong direction.

Here, Brown makes a judgment call and sometimes chooses to split one complex setup into two or more operations. Those setups could be on the same machine or, if the schedule allows for it, split between two or more press brakes. When you look at just the cycle time, it of course takes longer to form the part complete over multiple setups. But with one complex setup, a brake operator may be more prone to make more mistakes, which can force the laser or turret technicians to cut additional flat blanks. That costs more both in time and materials.

Using two or more simple setups on the brake makes things a lot easier for operators, which means they’re more likely to produce more good parts in less time. When you think about press brake efficiency, that is what truly matters.

Senior Editor Tim Heston can be reached at

timh@thefabricator.com

.

S&B Machine Co. Inc., 820 Blackburn Drive, Mobile, AL 36608, 251-633-4443,

www.sandbmachine.com