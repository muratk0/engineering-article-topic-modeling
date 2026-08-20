# The secrets of scheduling sequentially

[TARİH: 01.06.2017 The Fabricator]

Chief Concerns

How sequential manufacturing works in custom fabrication

I

magine you’re waiting in line at Disneyland’s Space Mountain. The sign at the back of the line says "30-minute wait from this point." That’s reasonable, so you get in the queue. And you wait 30 minutes. Then 40. Then 50—and finally, at long last, you get on the ride. You’re fuming. You just spent 50 minutes staring at the person’s head in front of you. What took so long?

What was the holdup?

The ride operations supervisor—deep inside Space Mountain, invisible to you—wasn’t having a good day. First, he had to stop the ride unexpectedly for five minutes to allow a passenger with health issues to get off. Second, he had to deal with a big group of riders who

all

had Fast Passes, which they got in advance (and paid more for) to guarantee a set time to ride. These riders were given a 30-minute window, and it turned out that nearly

all

Fast Pass holders for that window arrived at nearly the same time. The result: A bottleneck that sent ripples throughout the system, forcing everyone else without a Fast Pass to wait 20 minutes longer than expected.

This illustrates a classic problem in custom fabrication. Like riders reading the wait-time sign at Space Mountain, fab shop customers are given a certain delivery date when they place an order. Like the ride shutting down for a few minutes, a machine breaks or setups take longer than expected. Then the expedites happen (the Fast Pass holders arrive) as we bend over backward to try to meet customer demand. We can handle a few Fast Pass holders, but if they all arrive at the same time (which, of course, they usually do), chaos ensues. Overtime mounts, and we deliver jobs late.

We could extend lead times, and we could even turn some of the Fast Pass holders away. And in many cases, "just saying no" is the right thing to do. But we hesitate, knowing that competitors will probably say "yes." Moreover, many of us operate with a "we’ll do what it takes to get it done" mentality. After all, it’s how we’ve grown our businesses into what they are today.

Eventually, though, being late about 15 percent of the time becomes the new normal. We often just throw up our hands and think that late deliveries are a fact of life in custom fabrication. We can’t avoid unpredictability in high-product-mix operations, particularly when we need to deal with such

unreasonable

customer demands, so we continue with ad-hoc scheduling methods that work about 85 percent of the time.

At Ace Metal Crafts, a custom stainless steel fabricator near Chicago, we found that late deliveries are indeed avoidable. We now schedule through our ERP software using a method called

sequential manufacturing

. This focuses not on machine utilization, but instead on

job velocity

: how long a job takes to make it through the plant. When people stand in line—be they a regular rider or a Fast Pass holder—they know that the posted wait time (delivery date) is almost always met.

Our on-time delivery is better than 95 percent, and people aren’t breaking a sweat to make it happen. How? They receive and fabricate jobs in the right sequence.

Not So Simple

Waiting in line at Space Mountain is more like lowproduct-mix assembly than high-product-mix custom fabrication. The ride takes a set amount of time, it follows one track, and no one gets out of line. It’s like one or just a few products progressing on an assembly line based on a single

takt

time.

We as custom fabricators process thousands of different parts, each requiring different processing times, resources, and routings. One piece is cut on the laser and then goes to deburring, then forming, then

back

to deburring and weld prep, then finally to welding. Another piece is cut with a saw, goes to weld prep, then right to welding and assembly. Yet another piece arrives from an outside supplier. The challenge is for all parts to arrive in welding and assembly at the same time, in sequence.

What prevents this from happening? At Ace, it was all the wasted setups and teardowns, what’s called

context switching

. A welder would have several jobs on his schedule. As he finished setting up the first job, a material handler arrived with an expedited job. So the welder had to tear down and set up again to push the rush job on through.

The welder couldn’t see what was coming; he had no idea that an expedite was in the pipeline. That was a relatively easy fix. We now have monitors posted at every department, showing what jobs are arriving when. But just having a screen and posting the schedule doesn’t solve the root causes. Sure, it makes things visual, which is important, but it doesn’t magically make the right parts appear at the welder’s workstation at the right time.

To that end, we had to rethink how jobs were released to the floor. We needed to start with the operation in which multiple parts need to arrive at the same time. For us, that was usually welding or assembly. We then work backward from there.

To make sure parts arrived in welding when needed, two elements needed to be in place. First, we needed accurate processing times. Second, we needed to schedule sequentially and resist batching jobs together for better material utilization or easier setups.

Estimated Versus Actual Processing Times

Workers report actual job cycle times continually. This works because it’s easy and seamless, and people are given the tools to make it happen. Usually it’s just a matter of scanning a bar code on a part. Operators aren’t waiting in line to clock in a job at a computer terminal. The time measurement involves not just the machine cycle time, but also the material handling time. Even if the laser flies through a nest, we still need to account for the time people spend sorting parts and delivering them to the next operation.

Note that we’re a custom fabricator, so estimating processing times is an imperfect science, especially for new jobs. But the more data we have, the more we can adjust and perfect those estimated processing times.

Most important, our visual system now signals us when a job is taking longer than expected. When a welder starts a job, he scans the bar code and the clock starts ticking. I now can look up at a screen and see that a job is getting close to being late. Once the job is over the time allotted, it turns bright red.

As a team leader, I can see the problem as it occurs and then allocate resources to correct it—assign more welders, involve engineering, whatever the welder needs to catch up. We do this to avoid delaying parts from being sent downstream.

This relates to another core issue: We need the right skilled people and the right equipment available at the right time. If that doesn’t happen, chances are a job will take longer than expected. But because we’re tracking cycle times, we can catch the problem as it happens and make necessary adjustments to help. This helps us continually perfect a foundational part of the job shop business model: Knowing that when an order hits, we have the available capacity to meet the due date.

Admittedly, all this has a certain "Big Brother" aspect that can be difficult for some. A company must have a trusting culture for this to work. Operators are being timed not to punish them for falling behind, but so they can get the help they need when they need it—ideally, before a job is late.

People also need to know that timing operations is essential to everyone’s success. In fact, it helps us all avoid the chaos and reduce stress—no tearing down setups, no context switching, no unexpected late nights. In short, it makes everyone’s job easier

and

more enjoyable, and it makes the company more successful. That’s a healthy combination.

Material and Machine Utilization

Because we manufacture all parts needed for an assembly in sequence, we no longer look further out into the schedule just to fill out a nest. This would increase work-in-process and make an already complex part-flow situation even more complex.

At the same time, we’re a stainless steel shop; our material isn’t cheap, so we still need high material utilization. This means we’ve needed to become experts in changeovers and remnant management. A laser might run 30 different grades or thicknesses of stainless

every day

. We’ve perfected our changeover procedures so that we get a good part the first time.

When programmers run out of pieces that fit on a nest, they stop. The machine cuts what’s needed and an operator prints out a bar code label and places it on the remnant. Remnants are stored near the machine for later use and organized by material gauge and grade for quick retrieval. When a new job arrives to be nested, the software first checks for remnants before it places parts on a fresh sheet.

We also now take a different approach to machine setups. Years ago we’d group like jobs together to increase machine uptime and reduce the number of changeovers we had during the shift. This increased uptime and made traditional efficiency metrics look great, but in doing so, we slowed part velocity. A brake operator would spend an extra hour bending parts that weren’t needed immediately. Meanwhile, the parts that welders needed sat in queue waiting to be formed.

Ultimately, the longer it took for parts to flow through the plant, the greater it cost us. Part velocity is what matters. Sure, excessive downtime on a machine can cause part flow velocity to slow, but so can a lot of other things, like flooding the floor with work that’s not needed immediately.

To fabricate sequentially, we needed to become setup experts. Sure, by changing over a brake five times in an hour we’ll have less machine uptime, but we’ll have

higher

part-flow velocity because we’ll be forming everything the welder needs as soon as possible.

We do use a little common sense here. If, say, we have three jobs on the schedule for the press brake operator, and two have nearly identical setups, we’ll schedule those two back-to-back. But all three of these jobs need to be shipped at similar times. We never bend more parts than needed (to have parts for the next time the job is ordered) or bend another job that’s due a week later, just to save a little on setup.

The Role of Software

A final element to all this is the scheduling software. We use our scheduling module in our enterprise resource planning (ERP) system. In truth, if we were sequential manufacturing in a low-product-mix assembly line situation, the act of scheduling would be far simpler. We’d balance the line, schedule sequentially based on the established

takt

time, and that would be that.

But we don’t have consistent

takt

times, nor do jobs flow in a linear path. Routings bring parts to multiple shared resources at various times, with various manufacturing steps—laser cutting, sawing, deburring—happening at different times (technically called

concurrent sub-jobs

). All these pieces need to be sequenced to arrive in welding and assembly at nearly the same time. We need to calculate all this while factoring in the hundreds of other jobs in the system.

For us, this is where advanced software has really helped. As long as we feed the right data into the scheduling system, it will help us schedule jobs so that they all arrive at welding and final assembly at the right time.

Because we’re running sequentially, the software times orders so that they’re released to the floor when we know we’ll have

everything

we need to finish the job. If we release before that, there’s a greater chance that a job could arrive at welding or assembly before purchased components are available.

Keith Stout points to the shop status board and notices jobs that may need attention.

Photo courtesy of Ace Metal Crafts

.

The leadership team reviews the schedule during its morning huddle.

Photo courtesy of Ace Metal Crafts

.

This allows us to fulfill our promises. Quite often, after analyzing our capacity and bottlenecks, we see that we won’t be able to meet a customer’s requested delivery date, but all we need is one or two extra days. Before accepting the job, we call the customer and request two extra days, and customers almost always agree. If they need the job sooner, they may go elsewhere, but that’s fine. In the long run, losing a little bit of work is better than having to overpromise and underdeliver.

Scheduling isn’t perfect, and this is again where those monitors on the floor play an important role. If an operation has a long cycle time, like a machining job, software automatically sends an email alert when it’s, say, 70 percent through the operation. At that point team leaders check with the operator to see if the job is on track. This helps us be proactive.

And if a job is late, team leaders see the problem and respond immediately by providing the resources to free the bottleneck. Ultimately, software helps us all lend a hand when people need it most, before things snowball into larger problems.

Getting From Point A to B

The industry uses all sorts of technical-sounding terms: finite capacity scheduling, infinite capacity scheduling, and more. We use a form of backward scheduling, which takes the due date and schedules processes backward: e.g., shipping, packaging, assembly, grinding and polishing, welding, weld prep, bending, deburring, and cutting.

People will debate the validity of the various scheduling methods. But from our perspective, technical terms don’t really matter. We just want to get a job from point A to B, from raw stock to the shipping dock, in the least amount of time possible.

During the past two years our on-time delivery has improved from 89 percent to 95 percent. And our velocity has increased tremendously. We measure velocity by comparing

actual

time to the

estimated

manufacturing time that’s planned for in the schedule. If they are the same, the measurement is a 1-to-1 ratio, or 1.0.

Two years ago, we averaged 2.75, meaning the actual time was more than double the estimated time. Today we’re at 0.87, meaning that the actual time is less than the estimated time. Sequential manufacturing has helped us get there.

For more information about

The FABRICATOR’s

Leadership Summit and FMA Annual Meeting, visit

www.fmanet.org/annualmeeting

.

Editor’s Note: The following article is based on "Improving on-time delivery with sequential manufacturing," presented at the FMA Annual Meeting, Feb. 24-26, 2016, by Keith Stout, vice president of operations, Ace Metal Crafts,

www.acemetal.com

. Stout spoke as a user representative of ECi Software Solutions,

www.ecisolutions.com