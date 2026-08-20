# Pipe welding autonomously

[TARİH: 01.05.2022 The Fabricator]

How AI makes autonomous pipe welding a reality

By

Tim Heston

A welding gun on the end of a cobot arm welds pipe in the 1G position.

"F

ull-penetration, single-sized pipe welding is something that I have avoided automating for my entire career, starting in the early 1980s, because the requirement for adaptive control is so high."

So said Dan Allford, president of ARC Specialties, a Houston-based automated systems and process development firm. "That’s why, anyone who has come to us with a full-penetration, single-sided joint, I insist on a J prep. When you run a J prep, you run a zero root opening, and zero is repeatable. But as soon as you go to a V prep, then you have a variable root opening, and automating that application becomes really challenging."

This began to change three years ago when Allford saw three technologies maturing. The first was the cobot, which allowed pipe welding automation to work near people. The second was affordable 2D laser scanning that could scan and map a joint. And the third was advanced waveform short-circuit transfer gas metal arc welding (GMAW).

When it comes to pipe welding, advanced waveform short-circuit transfer creates a "soft" pool that in recent years have allowed pipe welders to bridge highly variable gaps. "A human can, in an instant, adapt to the changing gap by observing the width and changing his travel speed and oscillation width," Allford said. "That’s all well and good, but machines can’t do that until they have the ability to detect the [root-gap] width and react to it. That’s where laser scanning came in as well as artificial intelligence, meaning the system learns on the fly. In this case, we’re using the CPU to determine what the best welding parameters are for any given joint dimension."

Conventional short-circuit GMAW isn’t a process of choice for the root of a pipe weld. That’s mainly because of the way the short circuit behaves. It’s erratic, occurring at inconsistent intervals and at varying levels of intensity. Maneuvering the welding gun at the root is a bit like navigating a boat through choppy waters, trying to minimize splashes of molten metal up the joint side wall that could create cold lap. In short, the process works against the welder who, more likely than not, would prefer to be wielding a gas tungsten arc torch. Advanced waveform short-circuit GMAW, on the other hand, controls the short circuit and reduces the current to control the metal transfer. That gives the welder much better control over the weld pool.

On the other hand, the process also has very low penetration and low dilution characteristics. "That’s why it’s one of the few processes not prequalified [for code-level pipe welding] by the American Welding Society," Allford said. "So our preference is to use it only when we need to use it." This includes that critical root pass.

Today the company has implemented a system—with AIPW, or Artificial Intelligence Pipe Welder—that welds pipes in 1G, with tacks placed randomly around the circumference. It consists of a cobot arm from Universal Robots, and a Miller Regulated Metal Deposition (RMD) welding power source. It can handle anything from a 1/16- to a 3/16-in. gap and can handle high-low variation (that slight mismatch between the two lands of the V groove) up to 3/32 in. Thus far, the system has been used in pipe diameters up to 24 in. and in walls between 0.25 and 0.5 in. thick.

"So far we’ve been welding standard carbon steel [ASTM] A106 pipe," Allford said, "but the concept should apply to all types of materials."

In most setups the tacks have been feathered, meaning there’s a smooth transition between the tack and sidewall, but they don’t have to be feathered. If a tack is large, the system can start with advancedwaveform short-circuit, switch quickly to pulsedspray GMAW over the large tack (offering greater penetration and fill), then switch back once the welding gun clears the tack and is welding the root.

A laser scans a pipe weld joint to detect changes in root opening and other geometry variations.

Once the laser scanner maps the entire joint, the CPU calculates how to handle the variation. It starts on the tack near the smallest root opening. Because there’s a smaller gap at the starting point (which in pipe welding is also the ending point), the gun can travel with less oscillation and at a higher speed. This means at the end of the cycle, when the pool is large and fluid, the weld has less chance of melting through. The weld starts at the root with a subtle weave with a sinusoidal shape (there’s not much space for a pronounced weave at the root). But starting at the hot pass, the system can start a weaving action at an angle, pointing the weld at the weld toes of the previous pass. This in effect emulates the action of a manual pipe welder "walking the cup" to ensure good penetration and sidewall wetting characteristics, creating a smooth transition between the weld and base metal. After the root, the system then switches to pulsedspray GMAW for the hot and fill passes.

At the heart of it all is interpolation, the act of relating the data from the laser scanner with the physical attributes of the weld joint. This includes the root opening and overall size of the V groove as well as the location, size, and nature (feathered or not) of the tack.

"We had to correlate all this," said Jim walker, welding technologist at ARC Specialties. "I think that was likely the most challenging part of the entire project."

Specifically, the team needed to develop a set of weld parameters as a baseline to correlate what works for a specific root opening. Such interpolation could be looked at as navigation points along a pipe joint’s map. As the laser scanner captures the joint map, the AI-based system knows that certain joint characteristics—

this

root opening,

that

groove volume, these kinds of weld tacks—correlate to a specific combination of weld parameters. The most critical parameters are oscillation amplitude (weave width) and shape (sinusoidal versus walk-the-cup).

"We have different welding schedules for each root opening," Walker explained. "Right now, the only parameters that change are the oscillation width, so the robot can continue to bridge the gap correctly, and the travel speed, so your filler-metal volumetric deposition remains constant. But we’ve designed it so you can also change the wire feed, voltage, and arc control if needed. So far, though, we haven’t found a need for it."

All this sets the stage for autonomous welding. An operator fixtures a tacked pipe into a rotating fixture. The laser scans the joint, the CPU calculates the variations and required process adaptations, after which the cobot starts welding unattended, with no operator intervention from root to cap.

Jumping Into 5G

The cobot setup works in 1G, the most ubiquitous position in pipe welding, in which the pipe rotates on a positioner and the welding gun remains stationary. But what about situations in which the pipe is still horizontal but can’t rotate? What about welding in 5G?

In recent months ARC Specialties has been working with Bug-O Systems’ mechanized bug to develop fully autonomous 5G pipe welding. It hopes to start commercializing the system within the next year.

A setup in ARC Specialties’ welding lab involves a gun mounted to a Bug-O mechanized welding machine. During the hot and fill passes, the gun can oscillate along a pitch axis, which allows it to move in a way that aims the gun at the toe of the previous weld pass, producing the same result as a manual welder walking the cup.

At the heart of this autonomous pipe welding technology is interpolation, the act of relating the data from the laser scanner with the physical attributes of the weld joint. This includes the root opening and overall size of the V groove as well as the location, size, and nature (feathered or not) of the tacks.

The current setups involve two bugs, each welding half the circumference of a large-diameter pipe. (According to Walker, a similar system could be designed for a smaller-diameter pipe with a single bug traveling the entire pipe circumference.) As with the 1G system, a laser scanner maps the joint geometry. A similar concept of interpolation occurs, but it’s taken a step further. Not only must the system adapt to changes in gap width and joint geometry, but it also must account for the constantly changing relationship between the welding gun and weld joint.

"Now we’re basically welding in all positions every revolution," Allford said. "We’re optimizing the parameters not only for the joint but for gravity too."

The system welds downhill and maintains a slight backhand gun angle. As the bug reaches the 3 o’clock position, the travel accelerates slightly to account for gravity. The torch on the bug can move in a standard weave and also, like its 1G counterpart, in a walk-thecup fashion. It does this by adjusting a new axis of motion on the bug—what Allford called the "pitch axis." In essence, the axis allows the gun to change pitch so that, during the hot and cap passes, it can oscillate and aim toward the toes of the previous weld passes.

"We’re working with three different welding parameter sets for the same root opening," Walker said, explaining that one set of parameters works between the 12 and 2 o’clock position; another set for between 2 and 4 o’clock, and still another for between 4 and 6 o’clock.

The fixturing might be different in 5G. In 1G a tacked pipe rotates on a positioner. In 5G the pipe could be tacked, be clamped and aligned internally, or have both tacks and internal clamping. Regardless, the basic concept behind the interpolation logic would apply: If the root opening and overall joint geometry is

this

at

that

position on the pipe circumference, then these welding parameters would apply.

Evolution of Pipe Welding Automation

Such interpolations effectively move automation a few steps closer to behaving just as a skilled pipe welder would.

If a root opening narrows, then I need to change my weave and weld travel speed by a certain amount

.

That essentially creates the bedrock for autonomous welding, the kind that operators needn’t observe. They can set up the system, then move on to a job that, say, requires 6G pipe welding (pipe inclined at 45 degrees) or another application that would be cost-prohibitive to automate.

With labor shortages so acute, few argue about automation stealing jobs. The world needs more pipe welders. Recruitment is one way to get there, but so is automation, especially when it augments the value of each pipe welder. Pipe welders starting their careers today will likely retire from a very different industry, one that blends manual craft with autonomous welding technologies—those that can run stringers, can weave, and can even (at least in its own way) walk the cup.

Senior Editor

Tim Heston

can be reached at

timh@thefabricator.com

.

ARC Specialties,

www.arcspecialties.com

Bug-O Systems,

www.bugo.com

Miller Electric,

www.millerwelds.com

Universal Robots,

www.universal-robots.com