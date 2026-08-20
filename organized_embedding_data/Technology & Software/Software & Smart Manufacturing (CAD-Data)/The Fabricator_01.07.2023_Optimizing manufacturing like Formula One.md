# Optimizing manufacturing like Formula One

[TARİH: 01.07.2023 The Fabricator]

Tech Talk

How Monte Carlo simulations fuel better performance

By

Caleb Chamberlain

Tom Merton/iStock/Getty Images Plus

A

friend recently introduced me to Formula One racing. I’ve never followed racing motorsports in the past, but F1 might have converted me.

There’s natural appeal to seeing F1 cars scream down a track at over 200 miles per hour, but there’s also something incredible about the cars themselves. Each machine is the output of hundreds of millions of dollars in engineering, and each team employs hundreds of people. An F1 team is an enterprise dedicated to squeezing ever more performance out of their machines. F1 cars bristle with sensors. During a race, live telemetry is scrutinized, analyzed, and fed into simulations in real time to enable teams to make the best decisions.

As an engineer, I was surprised and delighted to learn that F1 teams regularly use statistical simulations to make tactical decisions before and during a race. How many pit stops should a team target in a race, and when? What tire compounds should be used? Should our driver attempt to overtake, or hang back? Multiple decisions, made in the moment, interact in complex ways to affect the race.

In the past, teams made intuitive judgment calls with inconsistent results. Now, analysts look at existing race conditions, run simulations, and produce recommendations that are accurate and specific. They might determine that a single pit stop enables a first-place finish, but it also increases the chances of a finish in seventh place or worse if something goes wrong. Meanwhile, two pit stops might make a first-place finish impossible, a third- or fourth-place finish likely, and a seventh-place finish or worse unlikely. Decisions can then be made based on how many points the team needs to earn compared to competitors, among other things.

When F1 teams used models and simulations to inform their tactical decisions, it made a difference. It didn’t take long until every team started doing it.

How is all this relevant to manufacturing? F1 teams exemplify how manufacturers can use data. We talk often about Industry 4.0, the next "industrial revolution." An Industry 4.0 shop is theoretically enabled by telemetry, cloud computing, artificial intelligence, and advanced automation. All these modern technologies are supposed to combine somehow to revolutionize the way we make things. How these technologies will change everything has often seemed (to me) vague and underwhelming.

I propose that manufacturers should be collecting data and using it in the way F1 teams do. Modern shops already collect extraordinary amounts of data. Let’s talk about what we should be doing with it.

Making Manufacturing Data Useful

In a previous article, I discussed the crazy complexity of production scheduling. Vast possibilities make it impossible to explore every possible scenario; even the fastest computers on the planet could spend the age of the universe exploring scenarios and never finish.

Instead, like F1 teams before the era of computing and simulation, shops make intuitive judgment calls. They might be imperfect and perhaps lead to inconsistent margins, lost bids, bottlenecks, increased work-in-process (WIP) times (that is, how long a work center takes to finish a job), or "brittle" workflows that result in late shipments when things go wrong.

If you take a step back and think through your manufacturing practices, you might find that many decisions are made based on rules of thumb. Perhaps you bid high to compensate for uncertainty, or you extend quoted lead times to give production extra slack. Somewhere along the line, you’ll have decided how much raw material and WIP inventory to hold. And many times throughout a shift, every production operation must decide what to produce next. Each of these decisions ripple out to affect the entire production line, yet the decision process is rarely designed, analyzed, or simulated in detail.

There’s no getting around the need to make judgment calls. The challenge is to develop rules that can be applied consistently to produce the highest possible value and reduce waste across the entire operation.

Simulating the Believable

This is where data and modern computing can take over. Instead of guessing or using rules of thumb, we can use past data to build models describing virtually everything about a manufacturing operation: market demand, bid win rates, WIP times, sequencing, scrap rates, and so on. Then, those models can be used to simulate production outcomes.

For example, a statistical model for a process might say that WIP time is "normally distributed" like a bell curve, has a mean of five minutes, and a standard deviation of one minute. If that model is based on actual historical data, then you can run simulated trials to see how long it will take to finish any number of parts.

Each simulated trial draws a sample time from the distribution. Based on the statistical model, most simulated parts will take around five minutes to produce, but occasionally, a part might be simulated to take 10 or more minutes. Those events are unlikely but, just like in real life, they happen on occasion, and the model captures that if we simulate enough trials.

In real life, most models won’t be as clean and simple as the familiar bell curve. The beauty is that they don’t have to be. If models are based on real historical data, then abnormal shapes that don’t fit any analytical statistical model can still be simulated.

Scheduling With Monte Carlo

If we model the WIP time for every process required to make a part, then we can run trials from start to finish, generating a time for each production step. The total WIP time for a single part is just the sum of all the times required by each process along the way. And if we run a thousand trials, we’ll get brilliantly specific results:

80% of the time, it took one hour or less to make a part. But 15% of the time, it took up to 90 minutes, and 5% of the time it took two hours.

Finally, we can look back at all the simulated events in the production pipeline and see which combinations of events led to bad outcomes: "The part took two hours to make when bending and hardware insertion took longer than expected." The beauty of this kind of simulation is that it captures real behavior. The statistical models are derived from actual historical data, so if it happens in real life, it’ll happen in the simulation at the same frequency.

As more shops have access to great data, there will be increased pressure to make it useful. Fabricators have to squeeze more and more performance out of their operations to stay competitive, just like F1 teams do.

This is called a

Monte Carlo simulation

. It’s a tool that takes a complex process like manufacturing and, instead of trying to predict every possible outcome, it generates scenarios randomly using statistical models. It allows us to characterize impossibly complex scenarios by showing us what’s likely to happen, and what the stakes are if the worst happens. F1 teams use Monte Carlo simulations to predict race outcomes. Financial analysts use them to predict financial scenarios. Manufacturers should be using them to predict production outcomes.

For example, when it comes to promising a lead time, shops might look at the existing schedule and think, "We are pretty busy, so … maybe two weeks?" Or perhaps a directive flows down from management: "We are falling behind, so don’t promise a lead time faster than three weeks." In practice, that might help slow things down, but it could also have a whiplash effect, creating uneven production demand and complicating planning.

Instead, a Monte Carlo simulation can produce extraordinarily specific, actionable results. "If you take this job on a five-day lead, then there’s a 25% chance it’ll ship late and a 10% chance it’ll make something else late as well. On the other hand, if you promise a seven-day lead, then there’s only a 1% chance it’ll ship late, and a 0.5% chance that it’ll make something else ship late."

In practice, the simulator is just a computer program that takes a collection of orders (those in process and those being analyzed) and uses predefined rules to "manufacture" them, attempting to match reality as closely as possible. If the models are bad, then the simulation will be bad. Having good data is key.

It’s also important to describe the production environment fully. For instance, our example WIP model needs to be augmented with other factors, like tooling changeover, scheduling rules (what to make next), scrap rates, and so on. When the full simulation is fed with existing and proposed orders, we can see likely outcomes for the entire production process across all orders.

Better Data, Better Simulations, Better Scheduling

Manufacturing is so insanely complicated that any predictive model-based platform is doomed to be worthless the moment it hits the floor. There’s no such thing as "just sticking to the schedule." In contrast, a Monte Carlo simulation runs thousands of trials and says, "Hey, I failed to get everything out today 50% of the time, and here’s why." That kind of analysis not only informs scheduling decisions but also exposes areas of production that can drive the most improvement.

For example, a badly designed manufacturing process might have highly varying WIP time and scrap rates; the Monte Carlo simulation will expose that process as an unpredictable bottleneck. If you want to know what difference it might make to improve the process, you tighten up the statistical model (by, for example, giving it a tighter standard deviation so it’s more predictable) and rerun the simulation. You’ll see immediately how the change impacts overall production flow.

All this only scratches the surface. Building the simulation is tricky, but once you have it, the fun really begins. You can simulate, scrutinize, tweak, and explore any number of scheduling and nesting strategies to see how it affects the floor. Questions that are normally impossible to answer can be explored with remarkable detail.

I think this kind of simulation is inevitable. As more shops have access to great data, there will be increased pressure to make it useful. Fabricators have to squeeze more and more performance out of their operations to stay competitive, just like F1 teams do. And while I don’t believe that there’s a silver bullet to the scheduling problem, Monte Carlo is about as close as it gets.

For more content from

Caleb Chamberlain

, visit

www.thefabricator.com/author/caleb-chamberlain

.

Caleb Chamberlain

is CEO and co-founder of Orem, Utah-based OSH Cut,

www.oshcut.com

.

The EUROMAC Digibend Series… an unmatched versatile bending solution for your shop!

Bend, punch, cut and straighten any type of material.

Powerful, up to 3.1/4″ thick steel bars.

Accurate, for the most complex Copper / Busbar applications.

2D and 3D Graphic Visualization

Angle Control and Spring Back Management

Digisoft PC

Automatic calculation of bending angle and sequences

Automatic calculation of workpiece development

Tool and finished piece DXF importing

Touch Screen with Graphical Programming Integrated with Wifi

Comeq.com

sales@comeq.com

facebook.com/ComeqInc

@comeq_inc