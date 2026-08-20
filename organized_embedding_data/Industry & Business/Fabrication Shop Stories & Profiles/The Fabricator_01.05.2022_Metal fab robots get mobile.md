# Metal fab robots get mobile

[TARİH: 01.05.2022 The Fabricator]

How automation can move to where it’s needed

By

Tim Heston

A mobile fabrication cell works with a small electric press brake to form a variety of small parts. Mid Atlantic Machinery Automation LLC

"C

onstantly looking in the rearview mirror can make it difficult to look at future improvement. The key questions are, ‘What will happen and what can we do about it?’ [Data that answers] those questions can become incredibly powerful."

That was Michael Schoenhals, director of operational excellence at Riverview, Fla.-based BlueGrace Logistics, who presented at this year’s MODEX, the material handling and supply chain show held in Atlanta in March. BlueGrace uses predictive analytics (which attempts to predict what will happen) and prescriptive analytics (which shows what to do about it) to coordinate resources in what remains a fragmented shipping business.

Its seminar was almost full, and probably for a good reason. Since the pandemic’s beginnings the logistics industry has endured numerous whipsaw moves in supply and demand, and the material handling business—plagued with labor shortages, both in the warehouse and in the cab of a semi—is looking for new ways to navigate them. The same could be said for metal fabricators farther up the supply chain.

To solve the problem, both industries are turning more toward automation. And to solve specific problems, both might arrive at a technological fork in the road of sorts. One path leads to integrated automation in which information flows seamlessly between machines, robots, and mechanized systems. The other path represents another approach that, at first glance, might seem counterintuitive. Even so, one day it might help fabricators and warehouse managers alike automate new kinds of applications.

That approach effectively decouples automation from the machine. Instead of integrating with the machine in a traditional sense, the automation "operates" machines—plural. In essence, robots are becoming cross-trained, and a mix of technologies, from deep-learning software to 3D-printed robot grippers, are making it happen.

Breaking Down Barriers to Automation

Flexible manufacturing systems have given metal fabricators agile forms of automation. Material shuttles between cutting and bending, with brief and sometimes nearly instant tool changes, allowing for kitbased production—for the right product, industry segment, and customer mix, of course. Sometimes, though, the application simply doesn’t suit the automation technology. Regardless, advances in robotics are making systems smarter, and in doing so, they’re helping to break down those traditional barriers to automation.

"Sensing technology will be extremely important going forward, and not just vision. Other types of sensors need to be put on the robot, including tactile sensing, which is very important."

So said Dan Popa, PhD, director of the Louisville Automation and Robotics Research Institute at the University of Louisville, during a MODEX roundtable on automation. "This allows the robot to be aware A mobile fabrication cell works with a small electric press brake to form a variety of small parts. Mid Atlantic Machinery Automation LLC of what’s going on in the workcell." He added that in the future we will see workpiece data cover not just geometric but also "physical information, including texture, payloads, load distribution, and friction coefficients."

Popa described evolving tactile sensors (including so-called "fingertip sensing"). Combined with deep learning and data-sharing with other automation, such sensing will work together to effectively train robots.

Such training could apply not just to a specific task but instead to perform a variety of tasks, both simple and complex, which in turn are helping to decouple the robot from the machine.

Need a Gripper? Print One

Josh Mayse has years of experience operating and integrating sheet metal machinery, including robotic cells. As vice president of Mid Atlantic Machinery Automation LLC, a Mid Atlantic Machinery subsidiary launched in August 2021, he began developing robotic bending cells by purchasing grippers off -the-shelf. "It took a lot of planning just to make one 90-degree bend," he said. "I knew I needed a new approach. So I turned to additive manufacturing."

He started experimenting with an inexpensive PLA printer, then upgraded to a system that could print carbon-nylon fiber. "We started printing individual gripper heads, but some heads took as long as 45 hours to print. That wasn’t practical for someone who needs to change-out jobs over and over. So I thought, could we design a kind of ‘build-a-gripper’ system? That’s when we came up with a modular approach."

The top two modular gripper bases are for small and medium parts;

is for large parts. These bases feature mounting points (in orange) that can be customized and 3D printed for the application. Onto these, fabricators can mount suctions or magnets in a variety of configurations. The gripper bases for small parts also include a pincher for handling small components.

Mid Atlantic Machinery Automation LLC

Mayse developed an aluminum-extruded endeffector base with pockets and holes that accepted T-nuts. On this he designed areas for custom mounts that could be 3D printed quickly and hold the desired array of suction cups and magnets. The bases designed for small and medium parts incorporate partpinching capability as well.

In effect, the system gives fabricators a base onto which shops can create an array of different gripper configurations. The system has different-sized gripper heads, one for small and medium parts, another for large parts. "From all this, we can very quickly and easily create any gripper configuration an application would use … and it turns out the gripper system works for a lot of things besides press brake tending."

Mid Atlantic offers this gripping system with its Mobile Fabrication Cell, which incorporates a Universal Robots (UR) cobot; a modular part cart (which incorporates pins from which the robot can pick accurately positioned and squared part blanks); and a machine interface that uses a Siemens PLC and a SICK safety controller and area scanners. (Cobots might be forcelimited, but they can still cause harm wielding sheet metal parts.) According to company literature, the configuration allows the system to be "reconfigured to run nearly any fabrication process." For instance, the robot can be set up to run a press brake, then be wheeled to feed parts into a flat-part deburring machine.

Simplified Programming

Designing a flexible gripping system is great, and so is a system that can work with various machines on the floor. But its use would be limited if it took operators forever to program.

Here, Mayse said, is where the system’s programming template comes into play. Templates exist for a variety of machines, the most complex of which is, of course, the press brake. At this point, the template handles parts with up to 10 bends, and can incorporate variables like material clamp point (when the descending punch first contacts the workpiece and secures it in place) as well as dwells of the ram, which can become important when a brake uses automatic angle correction.

Using the template, the operator teaches waypoints, then inserts standard commands like "vacuum release" and "toggle ram to set backgauges for bend." The template carries programmers through initial part grasping to palletizing the completed piece.

The program also accommodates safeguards, including the ability to leave factory-installed point-of-operation protection active. Because the system uses a cobot, a robot cell doesn’t require a safety cage. That said, it still requires safeguarding, and the programming accounts for those requirements. As Mayse explained, "Settings configured in the collaborative robot template allow the robot to be configured for different applications."

One robot (among many) is on display at the MODEX show, held in Atlanta in March. The material handling industry faces many of the same challenges metal fabricators face, the greatest being the acute labor shortage.

According to the company, a simple part can take about 15 minutes to program. Complex parts can take more time, but Mayse added that he is developing an offline bend programming and simulation system that could further streamline programming.

Separate Sandboxes

The Mobile Fabrication Cell’s current programming template operates using a decoupled approach. That is, the robot programming itself stands apart from the actual press brake program, be it created at the machine or offline.

"Basically, the system creates robot code," he said.

"You still use your press brake software to create the bending program." The code incorporates positioning and timing complexities created by odd part shapes and ram dwells, but it’s not intimately tied to the brake itself.

This, Mayse said, overcomes several challenges.

First, it allows the robot to move from one machine to another without high levels of integration. Second, it prevents service-issue complications. In a past life, Mayse worked at manufacturers that integrated automation systems, then found he had to deal with finger-pointing when problems arose. The machine OEM would point to the integrator who would then finger-point back to the machine OEM.

"When we install a system, we don’t touch a wire [on the machine]," Mayse said. "We take every opportunity to ensure the automation and machine remain separate."

The Potential of Decoupling

Back at MODEX, Schoenhals spoke of predictive and prescriptive models to best use transportation resources and adapt to a supply chain that’s demanding ever-more agility. Travel up the supply chain, and you’ll see an industry struggling to find labor and making every attempt to automate. But automating isn’t always easy, considering how variable consumer demand can be.

One barrier blocking these efforts is the expected return on investment (ROI). This barrier, though, isn’t as high as it was. For many applications, automation isn’t as costly as it used to be. And even if the price tag is sky high, the acute labor shortage is now factoring heavily into the equation.

"The labor shortage is changing the ROI calculations," said Dean Terrell, senior vice president of research and development at Material Handling Systems Inc., during a MODEX presentation. "End users are now considering the cost of not being able to staff their operations, and what that lost productivity is costing them."

Another barrier is flexibility. An agile supply chain requires fabricators who can reconfigure their operations at the drop of a hat. Many automated cells can of course accomplish this today. Again, legacy automated systems offer quick and sometimes even nearly instantaneous changeover, and so can be a great fit for a variety of part mixes. Such systems have helped transform the modern fabrication operation, and they aren’t likely to go away.

Regardless, some fabricators feel that investing in process-specific automation doesn’t always make sense. They want robots to move where needed, not be anchored to a single machine or cell. Decoupling the automation from the machine might be one way to make this kind of flexible automation a reality.

A modular part cart uses tall locating pins to stack, present, and position blanks for bending. The robot and part cart sit on wheeled bases so that they can be moved where needed.

Mid Atlantic Machinery Automation LLC

Senior Editor

Tim Heston

can be reached at

timh@thefabricator.com

.

Mid Atlantic Machinery,

www.midatlanticmachinery.com

MODEX,

www.modexshow.com

Universal Robots,

www.universal-robots.com