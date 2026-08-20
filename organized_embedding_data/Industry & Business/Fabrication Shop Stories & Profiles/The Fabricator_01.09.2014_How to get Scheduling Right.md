# How to get Scheduling Right

[TARİH: 01.09.2014 The Fabricator]

Improvement Insights

Detangling the fur ball in high-mix, low-volume operations

Dick Kallage

is principal of KDC & Associates Ltd.,

rkallage@kdcconsultants.com

.

L

ast month I showed how something that should be a deterministic process, in this case scheduling, can devolve into a mess—a fur ball. In a deterministic process, you can accurately determine the outputs by the inputs. ERP/MRP systems that have scheduling embedded in them rely on that deterministic nature: Set the parameters, provide the input, and out pops a sequence of activities and a start time. If the parameters were right, then everything will come out “on schedule.”

But too often this isn’t what happens. Instead of on-time delivery (OTD) rates of more than 99 percent, many custom fabricators seem to be stuck between 85 and 88 percent, according to the annual

Financial Ratios & Operational Benchmarking

survey results from the Fabricators & Manufacturers Association International

®

. The question is, why? On occasion there may be some trouble in calculating the OTD rate itself, and sometimes OTD problems emerge from a schedule change a customer demands that isn’t realistically achievable. I believe that. So let’s then arbitrarily wash out the low-end results and stipulate that the “real” OTD average is 90 percent.

Since this means that one order out of 10 will be late, 90 percent is far from being good enough, and is light years away from being world-class. By the way, “good enough” means that the customers are in a state of more or less constant irritation with you, but not so much as to drive them to the expense and risk of replacing you. Yet.

I strongly believe that OTD performance is one of the two most important issues regarding a fabricator’s ability to retain an existing customer and grow with them. The other is quality. Once a customer has decided that your OTD performance is continually unsatisfactory, you basically are on your way out. And once that process starts, there is not much you can do in the short term to reverse it. So smart companies attack this issue—as if their very life is threatened—

before

the OTD problem gets to this state. And they work on it continually.

Scheduling and Software

First, assess the scheduling process itself. Is it sound? Are the people engaged in the process capable and well-trained? In some cases, the root causes of OTD problems are indeed in the process itself and/or poor training. Can this be maddening? Yes. Is it the

major

factor? Not usually.

The major issue usually is complexity of the process itself, as required by an ERP/MRP system. Complexity breeds errors. Some older systems are so unwieldy and cumbersome that the best description one can give them is just plain cruel. They may have many screens, lots of interconnected pages, and no visual indicators of time buckets in the operations and their loading.

They may be lacking visual indicators of time buckets in the operations and their loading, as well as

visual

indicators of an order’s progress, either on the scheduler’s screen or on the shop floor, where it’s most useful. Scheduling and production control become the sole point of knowledge about what’s going on, and even that is iffy. Screens of older systems have that DOS feel and appearance, which can be agony to everyone but computer science majors or hacker types. This all creates steep learning curves.

If some or all of these symptoms are present in your scheduling process, I really recommend replacing or upgrading it, if for no other reason than retaining your sanity. The goal should be that

anyone

in the company should be able to look at a visual display and see where every order is in the process, what’s next, and what’s coming.

You will be amazed how something that simple eliminates a lot of the fur ball and the waste associated with it. Consider one of the parts of the fur ball waste: the production meetings. Half the time is spent on resolving where the hell the orders are (in a four- or five-operation process, for heaven’s sake), and another quarter of the time is spent on translating screen shots of the system’s description of the current state that is in a format that resembles the phone book.

Scheduling in a high-mix operation can be inherently complex due to the number of products and variation in the operations’ times. But the tools used should not be complex, nor should the learning curve involved in using those tools. At least two-thirds of the companies I work with have systems that are truly frightening. While they are technically correct and complete, they actually perpetuate fur balls because of their complexity. Remember this: The dudes who actually wrote these old systems had to make them very general, and they have probably never set foot inside a custom fab shop.

Incorrect Parameters

As practically unsuitable as some scheduling and control systems can be (they usually do give the right answers, however), the major issues regarding scheduling and OTD are related to the

parameters

that determine what the output of the system (the actual schedule and completion-date prediction) actually is. These parameters are generally

system-independent

.

What are these parameters? Usually they consist of:

• The routing—the sequence of operations each product or subassembly goes through from start to completion.

• The per-piece time it takes in each of the operations for each of the products. This must include changeover and move times.

• The available or realizable capacity of each operation, including operator availability; uptime available (time spent adding value); realizable rates (derived from actual machine-specific rates and/or labor standards); the work times available per shift; the number of shifts; and, in general, the yield (good parts as a percent of all parts made in the operation). You may recognize this as overall equipment effectiveness (OEE) plus available time.

• The calendar days of operation. From these the system can place the order into a time “bucket,” be it an hour, day, or week. As the job flows from operation to operation and time bucket to time bucket, the system predicts when the order will be complete. If this prediction is wrong, then one or more of the parameters related to the order was wrong.

This should be your real starting point for fixing scheduling and OTD

.

We’re assuming here that scheduling problems aren’t isolated, “one-off” deals. If they were, your OTD would be in the very high 90 percent range. Also, it’s safe to assume that your routings and calendar days are right. This leaves one last area: errors in the estimated time it takes for one or more operations and/or your actual capacity estimate. When you are operating close to capacity, an error in underestimating time or overestimating capacity not only affects the current job, but also the ones behind it.

To fix scheduling and OTD problems, fix the parameters. If the estimated times for a given operation were in error or are overly optimistic, make them more realistic. You can keep the “targets” the same, but

targets should not have any part in actual scheduling

. Many companies do not update parameters in the system based on actual results. This means that not only is the current order schedule tanked, but so are the future ones. Ergo, you get stuck with an unsatisfactory OTD performance.

Looking at the capacity parameter, you’ll see that a lot of things affect it, including search times, counting times, moves, material and labor availability, and machine failure. Of all of the parameters I see that are suspect in the scheduling system, the biggest is uptime. The amount of available time used for actual value-adding is simply less than what was input into the system.

I rarely see a case, as measured over a number of jobs, in which the actual uptime was higher than planned. The only exception is when the planner/scheduler got sick of bad results and put in an arbitrary buffer. Rarely was the adjustment to uptime (capacity) related to actual measurement and detailed observation. The second-biggest contributor to the error, though it’s usually a distant second, is the rate at which a machine or person can produce. This often comes from using ideal, “spec” machine rates that are often not obtainable or sustainable.

The real skill in scheduling is getting the parameters right. To do this you have to be realistic, but not so conservative as to input parameters based on truly bad “one-off” results. To get scheduling right, you need to find out what is really happening in the operations—and you can’t do it simply by looking at computer screens.

Dick Kallage is principal of KDC & Associates Ltd., 522 S. Northwest Highway, Suite UL-8, Barrington, IL 60010, 847-525-6109,

www.kdcconsultants.com

. Kallage serves on the Management Advisory Council of the Fabricators & Manufacturers Association International

®

and helps lead FMA’s LeanFab Workshop & Tours, metal fabrication seminars dedicated to continuous improvement. For more information, visit

www.fmanet.org/training

or call 888-394-4362.