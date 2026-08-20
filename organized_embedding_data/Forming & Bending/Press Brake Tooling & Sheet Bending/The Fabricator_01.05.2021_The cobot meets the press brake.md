# The cobot meets the press brake

[TARİH: 01.05.2021 The Fabricator]

Collaborative robotics uncovers new opportunities in bending automation

By

Joe Campbell and Craig Zoberis

FIGURE 1 Protective fencing is often, but not always, required on cobot-based press brake applications, as shown here. By deploying a UR10 cobot on press brake unloading tasks, Montreal, Canada-based Etalex replaced eight hours of manual labor with one hour of manual inspection per day.

Universal Robots

M

anual press brake operation often involves repetitive, unergonomic work that requires intense concentration and carries real risk of injury, made even worse without modern, properly designed and integrated safeguarding. At the same time, chronic labor shortages and problems with labor retention, especially for entry-level press brake roles, remain a perennial challenge. Driven by all these factors, many metal fabricators continue to be enthusiastic adopters of press brake automation. And in recent years especially, their enthusiasm has turned toward collaborative robotics (see

Figure 1

).

Deloitte’s 2018 Global Human Capital Trends found that more than half of U.S. manufacturers are redesigning their workforce architecture around robots and that machine tending is one of the most popular tasks for automation. Meanwhile, cobots are now the fastest-growing segment of the industrial robot sector, according to the International Federation of Robotics.

Top-of-the-line cobots provide a pose repeatability as tight as ±0.03 mm. They can work with legacy equipment and can even be mounted on a wheeled cart, a pedestal, or a mobile robot platform. This means you can deploy your cobot on one press brake in the morning and, as production orders change, move it to a different machine in the afternoon.

An investment in collaborative automation can complement and enhance your existing press brake investments. Moreover, cobot leasing and robotsas-a-service programs further reduce the financial risks.

Like anything else, though, a cobot investment shouldn’t be made on a whim. To that end, let’s take a look at some basic factors to consider if you’re thinking about automating press brake tasks with a cobot.

Find the Efficiency Sweet Spot

For most press brake applications, and depending on your cobot’s specs, you will aim to set your cobot at around 80% of maximum payload and reach, though this number can vary by as much as 10%, depending on the application and the weight of the materials being handled.

Generally speaking, though, that 80% figure should help you maximize the tradeoff between speed of operation and the lifespan of your cobot. Also remember that your cobot is available 24/7, as is your press brake, which opens the possibility of around-the-clock production.

Handshaking

In principle, integrating your cobot with a press brake is no different than integrating with any other machine. You want to know the status of the machine, whether it’s open or closed, and whether it’s safe to enter.

Depending on your configuration and the cobot brand you’re working with, handshaking between the robot and a press brake typically is a straightforward process via the cobot and machine I/O. The physical connection usually requires either a simple cable or an additional interface control box, depending on the robot-to-machine interface configuration of the press brake’s control system.

However, strict safety regulations apply to press brake deployments, so don’t underestimate the challenge. It is important to include a professionally engineered control system incorporating an industrial protocol that makes it safe to operate the two systems as one. In particular, the emergency stops on either the cobot or the press brake must be capable of safely shutting the entire system down. This includes shutting down both the cobot and press brake simultaneously.

FIGURE 2 Two cobots mounted on a 7th axis tend to a pair of press brakes. Humans regularly enter the workspace, arriving in forklifts to deliver parts for the cobots. When this happens, the cobot comes to a halt. Note that fencing (yellow uprights) is required for safety compliance.

Fusion OEM

FIGURE 3 This bird’s-eye view of the deployment in Figure 2 shows how making use of a 7th axis can greatly increase the potential reach of a cobot by enabling it to move around in front of the press brakes.

Fusion OEM

Here is where a professional robot integrator can help. An integrator that understands Robotic Industries Association (RIA) standards for cobot safety to meet OSHA industrial standards (ANSI/RIA TR15.806-2018 and ANSI/RIA R15.06-2012, specifically) will be able to determine whether your system complies with applicable safety regulations and guide you through any steps you’ll need to take to ensure compliance.

Part Gripping and Positioning Strategies

You need to determine clear picking and gripping points on a part that will allow the robot to present the part to the press brake without getting in the way of the tooling. Consequently, many deployments will require a repositioning station— a fixture that the robot uses to change the angle at which it grips the part.

In a typical deployment, the cobot will take the part, such as a blank metal channel-type part, and present it to the press brake. The press brake actuates, forming the required bend. The cobot then picks up the part, sets it down on the repositioning station, reorients its gripper, and picks up the part again for the next part of the process.

Choosing a cobot with a deep ecosystem of supporting hardware and soft-ware peripherals will broaden your gripper options. For instance, some grippers for cobot-based press brake applications can rotate 360 degrees, which eliminates the need for repositioning stations.

Safety Considerations

For many companies, one of the main attractions of collaborative robots is that following a risk assessment, it is possible to deploy your cobot without fencing or guards. Combined with their small footprint, this makes for very flexible deployments.

This typically is not the case in press brake applications, however, because of strict OSHA requirements, the nature of the materials being handled, and best practice in metal forming facilities. Following a risk assessment, you likely will find that your deployment requires additional safety features, such as light curtains and even fencing.

Cobot experts advise companies deploying cobots to start small and build on that knowledge over time before tackling more complicated projects. Choose a simple application with extremely low risk, the correct advice goes, and work from there. While this holds true for press brake applications, given the safety considerations involved and the additional safety measures likely to be required, press brake applications are slightly more complex than typical cobot deployments from the outset.

Your cobot’s built-in safety features will enable you to program it to stop moving when a human comes into direct contact with it. Or, as is more common in press brake scenarios, a device such as a light curtain is used to tell the cobot to stop or slow down as soon as a human enters the workspace. This occurs in setups where, for instance, operators enter the area to deliver and stack metal parts for their cobot to pick up. When the operator has left the workspace, the cobot will resume operations, ensuring a safe working environment.

ADVANCED LASER APPLICATIONS WORKSHOP

JUNE 1-3, 2021

Immerse Yourself in the World of Industrial Laser Applications

No matter where you are in the world, get up to date on the latest advancements and applications for lasers in the automotive, aerospace, agriculture, and general fabrication sectors.

Learn more |

fmamfg.org/alaw

| 888-394-4362

ATTEND IN-PERSON OR VIRTUALLY

Consider leaving space in the workcell between the cobot and the press brake so that a human operator can enter the cell and take manual control, if required. In such scenarios, you will make use of your cobot’s built-in safety features too.

Note that safety features vary depending on the cobot, so make sure to do your due diligence, including reaching out to the manufacturer or integrator directly. A risk assessment is compulsory. Additional safety steps are likely, so factor this into your deployment planning.

Payload Capacity and Part Geometry

When it comes to payload capacity, press brake automation is no different than any other material handling application, with the fundamentals of payload being based on the combined weight of the part and your gripper.

Payload capacity usually is defined as a given weight, but there are constraints about where that weight can be located. Some press brake applications, such as those involving large metal blanks, will require you to consider part geometry. The challenge with large sheet metal parts is that their weight is distributed across the whole envelope of the part. This creates

moment arm

(that is, the length between a joint axis and the line of force acting on the joint), which, in turn, will affect the cobot’s actual payload. So, larger parts must be handled carefully, with consideration being given to the effects of moment arm on payload capacity. Software associated with some cobot brands can take care of all these calculations. User-friendly pendant interfaces are a big plus too.

Note there are multiple ways to portray payload on a spec sheet. Some payload numbers assume that the payload will be held in place some distance off the mounting plate. This accounts for the space taken up by the adapter ring and gripper and matches how cobots are deployed in real-world applications.

Other specs assume that the payload will be right up on the mounting plate

without

accounting for the distance that the gripper is going to occupy. It’s as if you had bolted a 10- to 20-lb. weight directly to the end of the robot, which just doesn’t happen in the real world. This can throw off your calculations.

Batch Versus Kit-based Production

Consider a scenario in which you have an assembly made up of four pieces. Batch assembly involves fabricating a set number of each part in turn and then sending them on for assembly. Kit production involves making one of each piece, sending that kit on for assembly, and then starting the process over.

Generally, the amount of flexibility required to perform kit manufacturing is significantly higher than in batch production. In some cases, kit manufacturing is completely manageable, especially if the pieces aren’t overly complex and you can use the same gripper. But if you can’t use the same gripper, then a tool changer might be required.

In such cases, your cobot might have a bank of grippers for handling different parts. The downside is that tool changing adds to cycle time. Overall, tool changing for batch manufacturing is manageable, whereas tool changing for kit manufacturing will slow the process down.

Part Flow and Cobot Mobility

Two of the main attractions of collaborative robots are in their mobility and the ease with which they can be deployed and redeployed on various tasks. In this sense, think of cobots as versatile automation platforms that can handle a wide variety of applications, from inspection and assembly to finishing and material handling.

Traditional press brake automation typically involves a hard floor-mounted robot that’s placed in front of a machine. To maintain productivity and utilization, you have to keep running appropriate parts on that robot/machine combination. Cobots are more mobile.

Consider a cobot mounted on a simple mobile platform. You can wheel your cobot up to the press brake and program it to handle a set number of parts. If the next batch is run on another machine, you simply roll the robot over and run the program for that machine. For the ultimate in mobility, consider implementing cobots that are compatible with mobile robot platforms.

Programming a Job

Some cobot brands offer application kits that bring together all the hardware and software needed to perform specific applications. To simplify the programming and deployment process even further, look for cobots with hand-guided programming capabilities, as this is a very intuitive way to program. Also look for cobot systems that provide userfriendly pendant interfaces.

Using Multiple Cobots at Once

It’s possible to use two or more collaborative robots at once, such as when tending to two press brakes in the same workspace. Here, you’re looking for cobots that are 7th-axis-friendly, as this can massively increase the robot’s work envelope (see

Figures 2

and

3

). Another popular configuration for multiple cobots features one robot loading the press brake and the other palletizing the finished parts

A Collaborative Future

Analyst firm Emergen Research forecasts that cobot sales will climb to $9.3 billion by 2027, up from $0.7 billion in 2019. The RIA predicts that cobot sale revenues will account for 34% of the overall industrial robot market by 2025.

Expect to see these trends continue, driven by labor shortages, safety concerns, and the compelling business case for cobots. Additionally, watch out for a significant expansion of the number and type of peripherals and software designed for cobots, a trend that will create exciting new possibilities for cobot-based press brake automation.

Joe Campbell

is senior manager of applications development at Universal Robots, 5430 Data Court, Ste. 300, Ann Arbor, MI 48108, 844-462-6268,

www.universalrobots.com

. Craig Zoberis is president of Fusion OEM, 6951 High Grove Blvd., Burr Ridge, IL 60527, 866-952-9020,

www.fusionoem.com

.

THE TUNGSTEN ELECTRODE EXPERTS

DGP has been industry leader in tungsten and tungsten preparation since 1992. Visit our website to buy online from stock with same day shipping or call us for a free consultation today.

ARC SABER

TUNGSTEN STORAGE

REPLACEMENT

DIAMOND GRINDING WHEELS

WELDING

TORCHES & PARTS

RAW TUNGSTEN

INCLUDING NEW DGP TRI-MIX

PIRANHA

TUNGSTEN GRINDERS

PRE & RE-GROUND

TUNGSTEN ELECTRODES

MONSTER

TIC NOZZLE KITS

diamondground.com

2651 Lavery Court • Newbury Park, CA • 91320 • 805,498.3837 •

sales@diamondground.com