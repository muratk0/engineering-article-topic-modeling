# A New Way to Automate Bending

[TARİH: 01.02.2017 The Fabricator]

How one shop uses collaborative robotics for repetitive press brake work

By Tim Heston

Baxter, a collaborative robot from Rethink Robotics, retrieves a blank to be formed from an adjacent bin.

P

ress brake operators form various parts, many of them complex. But then there are those few long-running jobs that require operators to bend one small, simple part after another—for hours on end.

The order helps the company’s cash flow, but it certainly doesn’t help morale in the bending department. The job is still too small for building a tool and running it on a stamping press, so bending operators must resign themselves to stand or sit by a brake to form bracket after bracket. It’s not a fun way to spend one’s time.

This has its opportunity costs, because having bending gurus spending hours on such mundane work doesn’t make the best use of their talents. And quite often these jobs involve small parts, which puts operators’ fingers close to pinch points between the punch and die.

It’s a common conundrum, one sometimes solved by using specialized press brake automation, with robots designed to handle one small part after another. But Atlas Manufacturing, a precision sheet metal fabricator in Minneapolis, took a different approach. It chose to adapt a kind of automation not usually associated with press brakes: collaborative robotics.

Collaborative Forming

Such robots have gotten a fair amount of attention in recent years. They have a compelling story behind them, and not just because many of them have anthropomorphic traits, with two "arms" and a screen with "eyes" observing their surroundings (though technically it’s the set of cameras above and behind the screen doing the observing).

The robot and operator collaborate, hence the term for the technology. The system uses what’s known as behavior-based robotics. In a typical robot programming scenario, a worker may use a teach pendant to program a specific path. With a behavioral-based system, a programmer shows the robot the task at hand by, say, moving the end of the arm to simulate the action. The robot takes that instruction and, working from data coming from a variety of sensors, "looks" at its surroundings and "decides" the best path to take.

Like a human, the robot actually stops if it touches an unexpected obstruction, and it also can slow its operation if it sees that a person is nearby. The robot can do this not only because of the sensors it uses, but also because of its mechanical design; the joints aren’t rigid, but give a little bit. All this means that the automation doesn’t need to have conventional hard guarding around it.

For safety, the automated cell uses a high-density light curtain that mutes only when the punch tip is 0.050 in. above the die, just enough to accommodate the material thickness.

Still, collaborative robots do have several drawbacks that have kept them out of much of the metal fabrication arena, especially when early generations of the technology came on the market.

"We saw the technology when it was first released, and we thought it looked very slow and clunky," said Zach Zurbey, Atlas’ continuous improvement leader. "Then as the technology progressed, we saw the updated systems, and it became quicker, more agile, and repeatable."

So the company took the plunge and invested in a collaborative robot, a Baxter from Rethink Robotics (

www.rethinkrobotics.com

). With the robot in-house, the improvement team (including a summer software engineering intern) began looking for applications. As Zurbey recalled, "I basically told him to figure out how to use [the robot], and then teach it to me." This was a good litmus test of sorts.

Zurbey figured that if an intern new to manufacturing could figure out the technology, so could most employees at the plant. That intern—Cole Soffa, an engineering student from the University of Wisconsin-Madison—also happened to come to the task with no preconceptions.

"Still, I’m not going to pretend there wasn’t a learning curve," Zurbey added. "But if you have someone there to walk you through it, it goes a lot quicker."

After a summer of analysis, Zurbey and his intern found a potential application in the press brake department. The shop had just landed an order that, among other, more complicated components, required a large number of simple brackets. The fabricator had already sent out quotes to various stamping houses, and it turned out that Atlas could punch and form these brackets for less money. But it would also tie up talented operators for hours. Now they don’t have to; they instead "collaborate" with a robot.

Zurbey and his team dove into collaborative robotics knowing its limitations. Such robots have limited payload capacity. They also have low positioning accuracy, at least when compared to some other types of industrial automation. It’s not prohibitively low for most applications, but in precision sheet metal fabrication, it can be a limiting factor. The trick at Atlas was to find ways to overcome these limitations. And by August 2015, that’s just what the fabricator did.

A Very Human Robot

"We actually took advantage of the robot’s inaccuracy," Zurbey said. "Because the robot is not absolutely perfect as to where it puts things, it’s really important to understand how you can leverage that."

As the fabricator has now discovered, if you put a collaborative robot in front of a press brake, it in many ways behaves like a human. Most conventional industrial robots in front of a press brake need some signal that says that the part they’re holding has come in contact with the backgauge. Atlas’ collaborative robot, on the other hand, acts as a human would. It can sense when the part it’s holding has hit the backgauge, at which point it stops.

The company also designed a pneumatic frontgauge that presses the blank against the backgauge to keep it steady as the punch contacts the metal and begins to bend. The frontgauge effectively "helps" the robot apply the required force until the bending cycle commences.

When the robot was first integrated, the team didn’t use a frontgauge. "We did have some success," Zurbey recalled, "but it did open up more opportunities for failure.

"The frontgauge gives us a much larger landing pad to put that part down," Zurbey continued, explaining that jobs require the robot to place the part only within 0.5 inch, a wide window in the industrial automation arena. "A common industrial robot will do the same thing every time. [A collaborative robot] might not do the same thing every time. So we’ve built accuracy inherently into the process, and the frontgauge really helps out with that."

Like a human, a collaborative robot actually stops if it touches an unexpected obstruction and can slow its operation if it "sees" a person is nearby.

Zurbey conceded that using a frontgauge does limit part geometries the cell can produce. It cannot, for instance, produce a part with a downflange in certain orientations. For example, the robot can’t bend a flange upward and then flip the part over for the second bend without that previously bent flange colliding with the frontgauge.

Camera sensors feed the robot information about the surrounding area, allowing the system to react as necessary.

The team kept tooling setups as simple as possible, using sectionalized punches and a single (nonsectionalized) four-way die. If the next job needs a larger or smaller V opening, the operator just rotates the bottom die 90 degrees.

The single die means that the plane in which forming occurs does not change. This makes it so the frontgauge does not have to change in height from job to job. Moreover, the width of the frontgauge is as wide as the tool in front of it. "So as long as the [down-flange] is to the outside of the part," Zurbey said, "you can still avoid a collision with the frontgauge."

This is where the robot’s "feeling" capability comes into play as well. In several situations, the robot can "feel" the down-flange make contact with the side of the frontgauge, using it as a guide to position the part perfectly for the second or third bend.

Since the cell went live in August 2015, the shop has limited it to parts that have three or fewer bends. In forming, every bend affects another bend, and the more bends there are, the more complex the operation becomes. One small change on the first bend can snowball into major changes to the fourth and fifth. And because of the robot’s payload capacity limitations, the cell is also limited to parts that weigh less than 4 pounds. The tooling setup also limits bend widths to 16 in.

Because the robot observes its surroundings and "feels" as it reaches a surface, the pick-and-place points need not be absolutely precise. This can be a benefit when picking up or stacking parts or blanks that have embossments or other forms made on the punch press.

As long as the part fits within those parameters, the only other limiting factor is the capability of the press brake and tooling. The brake can form 90-degree, acute, and open bends, but it cannot form parts that require sectionalized dies.

The robot looks human and, in many ways, acts the part. A person isn’t programmed, but trained—and, Zurbey said, the same goes for the collaborative robot. Operators "train" Baxter by physically moving its arms through the motions, from picking up the flat blank to manipulating it through the bending sequence and stacking the finished parts.

The team also implemented an idle step in the robot training, when the robot pulls back and the press brake itself takes over. This step also ensures that the forming operation is safe to commence and that the light curtains aren’t blocked.

"We put an extra layer of safety by using very high-resolution light curtains on this press brake," Zurbey said. "It’s an extra layer of safety we need, because the press brake is going down on its own. The light curtain does mute as if a real operator were there, but it doesn’t mute until the [punch] is only 0.050 in. above the material. The main reason for the mute is to ensure the part that’s forming doesn’t trip the light curtain."

Forming of a part commences after Baxter places the part on the frontgauge table and the pneumatic gauge pushes the part against the backgauge.

Because the robot observes its surroundings and "feels" as it reaches a surface, the pick-and-place points need not be absolutely precise. This can be a benefit when picking up or stacking parts or blanks that have embossments or other forms made on the punch press.

And Baxter is doing a lot of picking and placing in this application. The typical batch size is about 1,000. "But these are small parts," Zurbey said. "That might be only one or two 5- by 10-foot sheets coming off our punches."

Still, the company does have the flexibility to run smaller lot sizes, particularly for repeat jobs. The technician simply calls up the previous program, places the batch in the right position, and ensures the tooling setup is correct. After that, the cell is good to go.

The system is not integrated into the press brake control itself, however, which means the technician needs to call up the program on the press brake CNC and separately select the program on the robot controller. Zurbey said that this is mainly because the robot works with an older press brake with a text-based CNC.

This shows how collaborative robotics may open up automation to new areas of the fabrication floor. After all, the cell automates the forming of small parts with just a few bends, and these components don’t require the most sophisticated press brake in the world.

Today one of the company’s best press brake operators, along with running his own parts, also trains Baxter, programs the robot’s press brake at the machine, and performs the initial tooling setup. Operators on other shifts have been trained to monitor and, if needed, restart Baxter if the operation runs out of parts or something unexpected occurs.

"They all have seen the benefit," Zurbey said, "because we’ve taken a lot of the tedious, monotonous work away from them. Our operators are highly skilled, and they can work on a lot of complicated jobs."

Considering this, why subject these people to long days bending one boring bracket after another? As Zurbey put it, "To bend simple brackets for 10 hours is really a waste of their time."

Senior Editor Tim Heston can be reached at

timh@thefabricator.com

. Photos courtesy of Atlas Manufacturing, 612-331-2566,

www.atlasmfg.com

.