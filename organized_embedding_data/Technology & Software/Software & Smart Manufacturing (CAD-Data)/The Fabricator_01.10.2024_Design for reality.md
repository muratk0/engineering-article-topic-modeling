# Design for reality

[TARİH: 01.10.2024 The Fabricator]

Tech Talk

How smarter CAD tools can bridge the gap between engineers and manufacturers

Caleb Chamberlain

E

ngineering is all about constraints and trade-offs. For any given problem, there’s an infinite universe of possible solutions. Some are elegant, simple, and inexpensive. Others are, well, less so. If your job is to manufacture things designed by engineers, you probably know what I’m talking about. It’s easy to design parts that are almost impossible to make, and an engineer might not fully understand the manufacturing technology.

That shouldn’t be surprising. Most university programs don’t teach the nitty-gritty details of how things are made, especially in rapidly evolving industries. I earned a master’s degree in electrical engineering in 2011. My thesis, titled "System Identification, State Estimation, and Control of Unmanned Aerial Robots," sounds arcane and maybe impressive. But after graduating, I knew nothing about some pretty basic stuff, like how to design a printed circuit board or even how to source components. My classes didn’t teach me what a voltage regulator was or that I could buy one from DigiKey. It simply wasn’t part of the curriculum.

Every year, universities produce a new batch of students who don’t know how to make things. That was true for me in electronics, and it’s true for engineers in metal fabrication. Very few students graduate understanding the ins and outs of CNC laser, plasma, or waterjet cutters. Even fewer understand how a press brake or panel bender works. And all bets are off when it comes to complex, custom-tooled stamping operations.

A browser-based simulation tells customers whether we can make their parts on our press brake and tooling.

Despite the jokes, engineers tend to be pretty smart. They learn fast. But every year, a new group of graduates enters the workforce without having yet learned the practical art of metal fabrication. Often, it’s the shop owners who provide this education: "We’d love to make this for you, but it’s literally impossible." It happens often enough to perpetuate the stereotype, at least.

The problem is complicated because CAD software lets you model anything you want, whether it’s manufacturable or not. CAD is the canvas. Why would it restrict you to a particular set of tools or technologies? It doesn’t make sense for generic CAD software to dictate what can be manufactured.

The result is often inefficient. Designers and engineers create things that look great in theory, but manufacturing constraints, tolerance limitations, and even material availability create friction when it comes to actually producing a design. Ask me how I know!

A Better Way?

There really has to be a better way. We live in the age of the internet, where the sum of human knowledge is immediately available to anyone with a web browser. Yet CAD software often remains disconnected from practical manufacturing considerations, like whether you can make metal origami on a press brake.

To be fair, CAD and CAM often come in pairs. Popular software frequently has plugins that allow numerical code to be generated directly from the CAD software. Autodesk’s Fusion 360, for example, integrates these features into the platform. It’s impressive: Designers can generate and visualize toolpaths for 5-axis machining within the same software used to design the parts. This provides incredible insight into how a part needs to be fixtured and produced. But when it comes to machine-agnostic software that does the same for sheet metal, the choices are likely few and far between, even nonexistent. For some reason, sheet metal seems to get short shrift.

Despite the jokes, engineers tend to be pretty smart. They learn fast. But every year, a new group of graduates enters the workforce without having yet learned the practical art of metal fabrication.

At our shop, we’ve taken some early steps to improve this workflow for our customers. We aren’t integrated with CAD software, but we’ve made bending simulations accessible directly in the web browser. Customers upload 3D models, and our platform automatically unfolds the parts to create a flat pattern. It then places the part on our brake and tools, adjusts bend radii where needed, and informs the customer whether we can make it. If we can’t, the system shows our customers why.

The system helps our customers, but it’s not as efficient or powerful as it could be. First, it’s limited. There’s much more you can do with sheet metal than our bending-only tool allows, and even in the realm of flat bending, there is a huge range of tools and machines that we don’t have. If we can’t make it, it doesn’t mean someone else can’t.

Second, it’s inefficient. Customers must design, download, upload, test, and repeat. It might beat doing the same by exchanging emails over several days, but it’s still time-consuming. Ideally, engineers could design sheet metal in a manufacturing-first platform: modeled features would be tested against tools and machines automatically, with design feedback available instantaneously, or at least as fast as it takes the DFM to run.

Imagine how cool that would be. As an engineer, I’d love to send a design out and have confidence that it’s manufacturable and that I’ll be able to get it quickly and at a reasonable cost. As a shop owner, I’d love to see manufacturable designs appear in the schedule without lengthy, inefficient quoting and design review processes.

Press Brake FUNCH TOOLS

Capacity to 12GA Stainless

3″ Leuve Tool

$850

3″/4″/6″ in Stook

DEALERS WANTED

www.punchtools.com

Tel:

604.521.6444 •

Toll Free:

1.800.668.4996 •

Fax:

604.521.3143

Website:

www.punchtools.com

•

Email:

sales@punchtools.com

Proudly Made in Canada by Punch Tools

What About Existing Platforms?

Manufacturing brokers simplify the ordering process in some ways. They use software to automate quoting, perform limited manufacturability checks, and connect buyers with manufacturers. That technology has come a long way, and it’s pretty cool, but DFM is often two steps removed from design.

First, engineers might not have a file to send until a design is near completion, and even then, it takes time to export and upload a file to an online quoting platform. By then, some design decisions might be difficult to reverse. Second, and more importantly, DFM is often performed using heuristics and rules of thumb. It sort of has to be, because brokers don’t aggregate highly detailed lists of shops’ machines and tooling. It might say, "this flange is kind of small," but it can’t say, "the smallest die that can produce this bend requires a flange that’s ⅛ in. or larger," or, similarly, "this flange needs to be ⅛ in. shorter so that it doesn’t collide with the punch."

Today, an impossible part might eventually be fixed, but only after days of iteration to exchange the required information. Software could do it instantly. A day after placing an order, a customer might have a part in hand instead of an email explaining why it can’t be made. There’s so much opportunity here.

A Heavy Lift

I have this utopian vision of a world where perfect manufacturing-first CAD exists, is widely used, and connects seamlessly with manufacturers without losing information. Forget prints. Forget impossible designs. The perfect system would consider manufacturability from the outset, encode design requirements using industry-standard methods, and fully describe specifications without ambiguity.

Getting there would be difficult, to say the least. Entrenched software providers benefit from network effects, where every new user makes every other user’s license more valuable (because more people can receive your CAD-native files). Beyond network effects, there are extraordinary switching costs. Years of training, existing designs, and institutional inertia make switching difficult. And, of course, CAD is complicated. The technology itself is a cornered resource.

Even so, if such software existed, everyone who used it would have a superpower. Would product companies benefit if their design cycles were shortened by a factor of 10? I’d think so.

Caleb Chamberlain

is co-founder of OSH Cut,

www.oshcut.com

, and co-host of Next-Gen Metal Fab, FMA’s newest podcast. Look for new episodes at

www.thefabricator.com/podcast/channel/next-gen-metal-fab

or wherever you get your podcasts.

Bend Better.

The strongest, most reliable bending rolls on the market—featuring unlimited capacities and CNC options.

C12 CHANNEL

Learn more about the quality, speed, and performance of a SweBend bending roll.

TrilogyMachinery.com

/ 888.988.7655