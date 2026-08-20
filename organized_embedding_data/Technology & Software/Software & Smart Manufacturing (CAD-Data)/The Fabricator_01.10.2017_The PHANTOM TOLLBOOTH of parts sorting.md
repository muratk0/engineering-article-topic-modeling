# The PHANTOM TOLLBOOTH of parts sorting

[TARİH: 01.10.2017 The Fabricator]

How to stop paying tolls on the part velocity highway

By Paul Blizel and Ben Blizel

W

hen you get right down to it, efficient manufacturing is all about part velocity. Simply stated, part velocity is the time required to process a part from start to finish. As velocity increases, so do billable finished goods.

This differs from traditional accounting methods in which work centers are measured individually and rolled up to create a value-added cost per part. Those who invested in new, faster equipment and automation have learned that increasing speed and expanding production hours do

not

guarantee increased part velocity. They have discovered

latency

on their shop floor.

Part velocity, sometimes referred to as

through-put

, can be defined with a simple formula:

Performance Capacity Latency = Velocity

. To determine productivity, enterprise resource planning (ERP) systems and their shop floor data collection systems normally measure only performance and capacity. But when time is introduced into the equation, shop floor latency becomes as important as the other variables.

Latency is best described as non-value-added time required between value-adding work centers. For instance, a laser cannot cut parts until an operator has loaded material, downloaded an NC file, and pushed the cycle-start button. A brake press cannot bend parts until the parts arrive from the laser.

Think of latency as a tollbooth between work centers: Every job will stop to pay the toll; the only question is for how long.

Hidden in Plain Sight

Until time was included in computing productivity, latency hid in plain sight on the shop floor and was accepted as an unavoidable cost of doing business. Reducing latency is not like normal process improvements. Some of it is fixed and can’t be changed; shuttle time for a laser pallet changer is a good example. But some latency is not fixed; it varies based on external variables and can be reduced through better process management. Decreasing it in one place can increase it elsewhere if the improvement does not take the entire production process into account.

Consider the evolution from stand-alone lasers to flexible manufacturing systems (FMS). The actual cutting processes are about the same speed, yet the FMS normally cuts more parts in the same time period. Both stand-alone lasers and FMSs require the same latency to produce parts, but the FMS operates automatically, eliminating the variability within the work center. The time it takes an operator to retrieve a job, load material, and hit the cycle-start button is replaced with a shorter and repetitive automatic process, resulting in more parts.

Because this latency occurs within a measured work center, the ERP system captures the increased productivity, and automation shows a clear benefit to the company. But those gains can be short-lived, because once parts pass out of the laser cell, they enter the part sorting department, where latency is directly affected by a change in part velocity.

The Black Hole of Part Sorting

In part sorting and processing, flat sheet metal parts are pulled from the nest, sorted, stacked, reported, and transferred to the next operation. Because all this occurs manually, a small change in part flow from the lasers can affect sorting time significantly. For instance, if the laser presents a single sheet containing one part, handling time is minimal and latency is relatively low. But if the laser presents nested sheets containing many jobs, latency spikes. Instead of "one part-one pallet," the handler needs to juggle many different parts and pallets. This requires more time and instructions.

To further complicate matters, the nested parts typically span several sheets, making individual part cut time secondary to the total time required for the entire nest package. Although some parts finish sooner, they sit idle because the handler is busy with other jobs and unable to move finished jobs until the entire nest is complete.

Automation compounds the problem; not only are more parts cut during normal operating hours, the FMS continues cutting in an unattended mode and stacks nested sheets onto large unload pallets for later retrieval and sorting. When the lights are turned back on, part handlers are faced with more parts flowing from the laser cell, along with the need to process multiple stacks of cut parts from the unattended operation.

As parts flow faster than part sorters can handle them, a backlog accumulates. Management will not be made aware of this latency until downstream operations report missing jobs. Management was expecting more parts out the door but instead has more work-in-process (WIP) and delays.

To deal with the backlog, managers move the part processors to a larger dedicated area and add more workers to handle the influx. While these steps help free the bottleneck, they do not fix the problem: The part sorting and processing area is a "black hole" in enterprise resource planning. Management relies on the ERP system to track work and make production decisions to maintain part velocity. But inside the part sorting and processing department, other documentation and tribal knowledge are used to process jobs.

ERP systems operate on a "single job-single machine" basis; a single job is scheduled at a specific work center and time, allowing the ERP system to monitor and control production. For this to work at laser cutting and part sorting, jobs need to be split up and run individually, something rarely seen anymore because of low material utilization.

Instead, the ERP system passes production requirements to the nesting system where multiple jobs are merged together to form production kits. While these kits use material effectively and reduce programming time, they also make part sorting much more challenging.

When production kits are released to the shop floor, the ERP job traveler is replaced with nesting system paperwork to assist in the pulling and sorting process. Unfortunately, this documentation does not include enough details to allow a handler to recognize the value of each part. For example, a hot job holding up the assembly line should be processed as quickly as possible. But the handler is not made aware of this and handles all parts the same, meaning jobs finish in a random order. To expedite work, a planner or coordinator is assigned to instruct the workers on priorities and production changes.

This process creates a simple bridge between management and the part handlers, but it’s still a one-way street that lacks feedback. Managers will not know if their production requests were successfully executed until the ERP system takes control at the next operation, further increasing cost and complexity on the shop floor.

Machine tool manufacturers understand the difficulties with part sorting and offer automated part handling systems to increase velocity. Options range from automated pick-and-place systems to conveyor lines. While pick-and-place part sorting is fully automatic, conveyors automatically transfer cut sheets to employees who remove parts manually.

The pick-and-place system, like laser automation, replaces variable latency with a defined

takt

time and has been shown to significantly outperform manual sorting and processing. But this level of automation comes at a cost of some flexibility; not every part or material is suitable for automated handling. Conveyor lines are more flexible and cost-effective, but run the risk of inconsistent part flow because employees ultimately control part flow and adherence to the production plan.

If a pick-and-place system isn’t suitable for an application, why does conveyor system automation improve it when it is still a semimanual process? Simply put, the conveyor converts part handling from traditional batch processing to single-sheet/single-part production flow. Workers handle each sheet as it is cut rather than waiting for the full production kit to finish before beginning the sorting process. This means that as each job is finished it can move downstream, increasing part velocity.

Such production flow "compresses" part handling time by overlapping cutting and sorting, allowing each to occur concurrently. These conveyor lines reduce latency but are limited by the handlers who can idle the line if they do not keep pace with production flow. In other words, equipment can increase part velocity, but only if the part handlers let it happen.

A Unified System

One way to manage velocity in part sorting involves implementing a unified system that integrates important information from both the ERP and nesting systems. It provides the nesting system with job requirements; the ERP with the status of production kits; and the part sorting area with reliable, up-to-date sorting information.

For such a unified system to be implemented, the ERP needs to have an open system that can share real-time information as opposed to simple data dumps. The nesting software must also be able to receive job requests from the ERP system and provide production kit information back to the system in real time.

When implemented, these changes will set the stage for gains in velocity not only within part sorting and processing, but in other downstream operations. This includes material handlers who will proactively move jobs rather than just respond to an after-the-fact request to move parts.

This unified system looks and acts differently than typical manual sorting and processing with paperwork. First, the part sorting area itself is smaller and closer to the laser cutting equipment. Because flow is based on management priorities instead of the typical first-in, first-out method, fewer workers can handle parts in an orderly manner. NC programming forgoes massive multisheet nested production kits in favor of smaller, "bite-size" production kits that balance time, material utilization, and priority as opposed to just material yield.

Automating the shop floor involves much more than machinery. Automation begins at the front door, when an order arrives, and knowledge is as important as equipment.

These smaller production kits shrink production time into smaller blocks and allow management to commit to many small blocks of production. At the same time, managers can change the schedule as necessary without directly involving the NC programming department. Fewer open jobs require fewer pallets and less labor. So rather than appearing to be a chaotic beehive, part sorting is more subdued, resembling other managed work centers.

The single biggest improvement can be seen in handling unplanned hot jobs. Because management controls the process, part handlers no longer hunt down parts located within stacks of cut sheets. Instead, the job can be easily inserted in the schedule along with special instructions.

The part handler must know only two things about each part: what it is and where it goes. All logistics about priorities and hot jobs do not involve the handler. Handlers just pull parts and sort them according to the instructions provided.

Because every part on every sheet is known as it passes down the conveyor, jobs flow down conveyor lines best suited to handle unique parts, such as large, heavy workpieces or parts that require special handling.

As the cut sheets move down the conveyor line, the system displays color-coded sorting diagrams and special instructions to allow fast and accurate part sorting, even when jobs have been rescheduled or diverted. This flexibility allows hot jobs to be processed like any other, greatly reducing confusion and lost time.

Transferring jobs downstream also operates under the unified management system. Just like the part handlers, forklift operators receive all necessary information to pick up and deliver jobs effectively, further reining in latency. Taken to the extreme, automatic guided vehicles can be dispatched to pick up and deliver jobs to their next operation. Because management is instructing workers, ERP job travelers are optional, replaced with a simple move ticket that contains only the information needed for workers to do their jobs effectively.

Automation Begins With Knowledge

Automating the shop floor involves much more than machinery. Automation begins at the front door, when an order arrives, and knowledge is as important as equipment.

Adding time into the productivity and profitability equation requires rethinking the entire shop floor. While automation demonstrates impressive gains, an overlooked gatekeeper may be lurking in the dark, waiting to add more time back into the formula. Search out those tollbooths and look for a way to incorporate them under management’s umbrella.

The adage "knowledge is power and power sets you free" is spot-on. This is true for management, because the increased visibility pays dividends not only in the primary work center, but throughout the shop.

And it is especially true of shop workers. Traditionally, they spend most of their days reacting to change, which creates a very disruptive work environment. When part sorting becomes automated, though, their day changes dramatically.

They must learn to "let go" and allow the system to make primary decisions. In return, their job is simplified and focused on just one thing: sorting parts. Armed with the right information, these workers can be proactive, experience less stress, and boost throughout—all at the same time.

Paul Blizel is vice president, automation division, and Ben Blizel is director of technical services at Ncell Systems Inc., 952-746-5125,

www.ncell.com

.