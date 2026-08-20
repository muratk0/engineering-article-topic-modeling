# Avoid automation’s biggest pothole

[TARİH: 01.10.2021 The Fabricator]

Automation requires a highly stable, capable process

By

Paul Neblock

Vitalii Petrushenko/iStock/Getty Images Plus

S

o many manufacturers struggle to automate seemingly straightforward operations only to spend months debugging and eventually throwing their hands up in despair. They eventually remove the automation, often spurring a string of disputes with automation suppliers. In almost all cases, failure can be traced back to part-to-part variability or a lack of process stability, neither of which are the automation provider’s responsibility.

In the industry’s fever to automate, organizations are making some fundamental mistakes that result in significant process delays, cost overruns, and sometimes outright failure. They end up producing nonconforming parts or losing production throughput from frequent machine faults. In these cases, automation can actually have a

net negative impact

on productivity and costs. Even worse, project-specific failures cast automation in an unnecessarily bad light with management such that subsequent projects are rejected.

Fabricators can avoid this scenario by taking steps to identify, understand, and reduce what remains the biggest technical reason for project failure: process variability.

What Is Process Variability?

Part-to-part dimensional variation, the most commonly overlooked and important risk factor for any automation project, involves two components. The first is

process capability

. Do the parts conform to print specifications 100% of the time? A process capability study provides a snapshot of this capability and is measured as Cpk, a process capability index that identifies the ratio between the print specifications and natural process variability.

The second component is

process stability

. Does the process remain relatively stable over time? Every process has some natural variability, as shown in the normal distributions in

Figure 1

. If the process centerline in that distribution shifts over time, does it still yield 100% conforming parts? Unless they provide a turnkey cell or operation, automation providers typically hold the fabricator responsible for process stability.

Deep-draw Case Study

Consider a process in which coil-fed, leveled, cut-to-length blanks are deepdrawn and trimmed. Specifically, blanks are cut to length in-house from preslit coils and positioned for loading into a two-station draw and trim press with appropriate lubrication.

The first station has in-die blank-detection sensors that alert the operator of misfeeds and prevent actuation if a blank isn’t seated properly. The second station has in-die sensors that detect if the formed part is properly seated before trimming. This includes trim splitting and ejection so that the finished part can be reliably removed and placed on an exit conveyor.

A press operator loads each blank into the press, actuates the lubrication system, and moves the part manually between drawing and trimming stations to a basket for finished parts. The scrap is sectioned in the trim die and falls away to a conveyor.

FIGURE 1 A stable, capable process has narrow parameter distributions that all occur well within the process specification limits.

FIGURE 2 The focus steps, outlined in red, look seemingly straightforward to automate—but not without process stability and capability.

In front of the press is a safety curtain with a fast interlock. Still, the company wants to automate the process for productivity and safety reasons. Operating the press is very demanding work, and business is increasing.

On the surface, this might look like a straightforward pick-and-place automation project. An automated system could precisely place blanks into a die, move the drawn part from the die once ejected, then place it in the trim station (see

Figure 2

). It could then remove the finished part from the trim die and place it on an outgoing conveyor. With the proper interfaces between robotics, the sensors, and press controls, this project should ramp up without a hitch—right?

What Could Possibly Go Wrong?

Drawn parts need to be accurate and consistent. Misformed parts might stick in the dies and become scrap. And if automated, such mishaps might cause faults that shut down the operation. For this reason, the company needs to assess the drawing process itself for capability and stability.

Planning for automation requires a keen eye for failure modes:

What can and will go wrong?

This is the essence of excessive process variability that manifests itself in automation that alarms-out frequently, producing excessive scrap and diminishing throughput.

Three Steps to Reducing Variability

A three-step process has proven quite successful to minimize such process variability and roadblocks to automation: (1) observe, (2) analyze, then (3) plan and implement.

1. Closely observe the manufacturing process and collect data.

A team assigns one draw and trim die set as A and another B. The performance of die set A should match die set B. That’s the ideal, at least. To uncover the reality, a team observes the die set performance over multiple days and shifts. Figure 3 details their findings.

2. Analyze the data and observations to identify areas of risk.

The team reviews the data collected, identifies and ranks the areas of risk, and conducts root cause analysis to understand the causes of process variability. Process failure mode and effect analysis (PFMEA) can be a good tool to organize this. A simpler version might look like the table shown in

Figure 4.

3. Plan and implement actions to reduce variability.

The team works with others in the organization to implement corrective actions to significantly reduce, if not eliminate, the process variability identified (see

Figure 5

). They also closely monitor these improvements and their impact, lest process variability raise its ugly head weeks or months later.

Next Steps Toward Automation

The disciplines of lean manufacturing and fundamental process controls (use of statistical process control, capability studies) help improve manual operations, but they become even

more

important in an automated environment. Once implemented in the manual environment, the transition toward automation can begin in earnest.

Screen Automation Providers.

Automation providers are in the business of developing, designing, building, and implementing automated cells. They are not in the business of mitigating process variability and risks. In fact, they expect their customers to have a handle on both. The best providers will spend time on-site, observe the operation, and thoroughly identify risks. Still, do not rely on the automation provider to do this work for you.

If the automation provider is integrating a turnkey cell, include in the contract the specific testing required at the factory and during commissioning to approve the project. Together with the provider, closely review the operation, including part location and workholding, to ensure they grasp the entire process, not just the automation.

Some automation companies will want to sell complex vision systems and in-process inspection devices. Be wary of these and focus first on obtaining and maintaining a very capable process. Inspection devices must be calibrated and maintained, and they add cost and cycle time. If these devices end up producing false signal after false signal, they might end up being turned off anyway.

Write a Request for Quote With a Two-stage Approval Process.

Include process run-off steps in your contracts, one at the automation supplier’s facility before shipment and one at your factory upon commissioning and before final payment. Be sure to document this two-stage approval while soliciting bids so the automation providers can plan for and include the cost and time in their bid documents. Tie progress payments for each step to the completion of each stage, and clearly define approval requirements, such as specific cycle times and desired uptime.

FIGURE 3 Before automating, a team observes the process and identifies variabilities.

FIGURE 4 A manufacturer might choose to organize its data using process failure mode and effect analysis. Or, as shown here, it can simply chart the risks and their severities.

FIGURE 5 Once an operation identifies issues, it should document and implement corrective actions.

Conduct In-depth Automation Concept Reviews.

Review the proposed automation concepts closely with prospective suppliers. Ask them to walk the team through each station, the proposed concept, and underlying assumptions.

Also, walk through the failure modes your team has identified and with the automation firm, and ask how their proposed solution would address each one. Finally, ask their design team about their concerns about the application. Good designers will have good questions.

Provide Representative Parts for Automation Development and Approvals.

After you have tightened up process controls and reduced process variability, provide the selected automation supplier with parts from a number of lots or production runs to use in debugging the equipment at its own facility. The automation supplier will use these during the first approval stage, so avoid sending only the best of the best parts as this will only cause more issues during the second approval stage on-site.

Automation by itself cannot make the unreliable reliable, especially when the parts entering the automated system aren’t consistent.

Detect Variability Early

Fabricators increasingly turn to automation and smart technologies to address critical labor and skills shortages across the nation. And the pace of automation is increasing, thanks to high demand and reshoring trends in supply chain management. Still, automation by itself cannot make the unreliable reliable, especially when the parts entering the automated system aren’t consistent.

Uncover process variability

early

in a project so it can be eliminated rather than detected during commissioning. Successful automation is always based on stable, capable processes. Successful fabricators understand this and do the hard work to understand their processes, stabilize them, reduce variability— and

only then

automate.

Paul Neblock

is a partner with APEX Management Partners LLC, 6537 State Road 252, Martinsville, IN 46151, 847-558-9008,

www.apexmanagementpartners.net

.

THREE PIECE CUTTER KITS

Available for Carbide or "12,000-Series" Cutters

Grab one of 20 new kits today!

800 426 7818 SERVICE • INTEGRITY • RELIABILITY

HDUGEM.COM

the fabricator’s TECHNOLOGY SHOWCASE

Compact Direct Energy Deposition Head

Laser Mechanisms’ FiberWELD

®

DHc is a compact high power, laser wire direct energy deposition head for processing macro-scale industrial and aerospace component. Engineered for high duty cycle production applications, FiberWELD

®

, DHc features both direct-cooled reflective optics and transmissive optics, back reflection protection and wire feed. The head’s advanced optical design permits filler wire to be fed directly into the beam path - right into the center of the melt pool. This allows the deposition process to have total directional independence. In addition, FiberWELD

®

DHc’s protective cover glass extends the life of internal optics. Primary applications include additive manufacturing, cladding and HLAW.

www.lasermech.com

603-402-3055

Automated Layout Technology™

"It easily doubles our output - no mistakes"

Plant Manager- Papp Iron Works

The first automated marking machine created specifically for the layout of commercial handrails, stair stringers and so much more utilizing your stee detailer’s dxf files.

Cut fabrication time by more than 50%

Ensure the highest level of accuracy

Boost your profit margins!

Lay out complex geometry in seconds

Designed to replace your existing fabrication table

"The guys love it. They jumped right in on it and have been working to make the most use of it. Great purchase."

Nat Killpatrick • Basden Steel Corporation

"I think it’s fair to say that this machine continues to exceed our expectations. We are very happy with it."

Chief Operating Officer • Koenig Iron Works

Visit

AUTOMATEDLAYOUT.COM

for a Quote