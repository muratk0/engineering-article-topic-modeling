# What should we work on right now?

[TARİH: 01.04.2023 The Fabricator]

Tech Talk

The impossibly complicated reality of shop scheduling

By

Caleb Chamberlain

For more content from Caleb Chamberlain, visit

www.thefabricator.com/author/caleb-chamberlain

.

Caleb Chamberlain

is CEO and co-founder of Orem, Utahbased OSH Cut,

www.oshcut.com

.

M

anufacturing is complicated. I’ve said that before, but it bears repeating. Aside from quality, supply chain, personnel, compliance, and hosts of other complexities, scheduling alone is complicated in the "almost impossible to get right" kind of way. Scheduling is a problem that a computer scientist would call "np-hard," which literally means "non-deterministic polynomial-time hard." That’s a mouthful, but more colloquially it means a computer could spend the age of the universe trying possibilities and not finish.

Unfathomable Number of Possibilities

Why is it so difficult? It really boils down to the sheer number of possible combinations. Consider how many ways just 10 work orders could be organized and released to production. The total is 10 factorial, or 3.6

million

possible permutations. What about 100 work orders? They could be sequenced in in 93 × 10156 unique ways. That’s 93

with 156 zeroes

, a number so huge it beggars imagination, far more than the number of atoms on earth. Even if a computer could simulate a million possibilities per second, it would take many, many times longer than the estimated heat death of the universe to explore every possible permutation.

It gets worse. It’s not just a question of what work order to produce and when, but how it might be combined with other jobs. Multiple jobs can be nested together on common material, and then those jobs all trickle down to other processes downstream, which also have decisions to make. Decisions across many branching paths in production can cause suboptimal changeovers, unexpected surges of demand upstream and downstream, sensitivity to labor allocation, scrapped parts late in the process, rushed requeues, and scores of unpredictable outcomes.

Worst of all, even the best plans fall apart in the complex uncertainty of a manufacturing process. Even if a computer could arrive at a perfect scheduling solution, it might be rendered useless 10 minutes later when the situation changes.

Enter Heuristics

Of course, nobody approaches scheduling this way. We might prioritize work orders by due date and adjust a little if needed. Nesting judgment calls also can be based on part availability, extra shift time, due dates, and remaining sheet area. These kinds of decisions are called

heuristics

, rules of thumb that avoid the sheer impossibility of brute-forcing the scheduling problem. There is surely a golden solution hidden in the infinite sea of scheduling possibilities, but heuristics often get us close enough.

As complex as it can be to simulate and predict outcomes, scheduling optimization still boils down to a remarkably simple question:

What should I work on right now?

Hidden beneath that innocent question is an ocean of possibility, each option branching into an infinite selection of new possibilities with consequences that can be difficult or impossible to foresee. That becomes more and more true for high-mix operations that manufacture high volumes of everchanging, diverse sets of parts.

Managing Through Uncertainty

All this complexity can be managed in two ways: first, by structuring manufacturing processes in a way that facilitates consistency and predictability; second, by implementing scheduling processes in ways that maximize value.

The first option, optimizing manufacturing processes, is an interesting way to look at lean manufacturing. Lean manufacturing constrains the production environment in ways that make scheduling easier. A manufacturing process that is optimized around onepiece flow creates flexibility: Tooling changeovers are fast, parts flow predictably through production, and built-in quality is enforced (because if it isn’t, the line stops). Less work-in-process (WIP) inventory means less confusion, fewer decisions to make in each process, and more predictable throughput. That ideally means any part can be released to production at any time, regardless of the current state of the production floor. Parts should make their way through production predictably and efficiently even if changeovers are required.

REAL WORK HORSES

FROM TENNESSEE • MADE IN USA

Over 40 years of experience with 3 generations working in the business.

Built in USA with American and global components.

30 gauge to 3″ thick, 1′ to 26′ wide.

Custom and built to order options available.

Expanded facility with many popular/standard machines in stock.

We are a dedicated business specializing in customer service and lasting customer relations.

From complete custom forming cells to many popular/standard machines In stock.

Waldemar Design & Machine LLC

224 Pierpont Street

Petersburg, WV 26847

606-787-8474

drisser@wdmrolls.com

wdmrolls.com

Contact us direct, or contact your favorite machine tool distributor and ask about WDM Machine Tools.

3 & 4 Roll Hydraulic Double Pinch Plate Bending Machines • Initial Pinch Sheet & Plate Bending Rolls Cone Rolling Machines • Bending Systems & Complete Forming Cells

Casper1774Studio/ iStock/Getty Images Plus

I’ve been asked if modern technology might make lean manufacturing obsolete. Does the era of big data, artificial intelligence, and hyper-powerful computing make lean practices irrelevant? I don’t think so. A lean operation is adaptable and flexible, and that simplifies scheduling dramatically.

Even so, scheduling remains a challenge. One-piece flow is a great ideal, but in practice, changeovers still require time. And in a sheet metal shop, nesting is critical for material efficiency.

Everything has a cost, and sometimes optimizing one process can be detrimental elsewhere. For example, if you were only concerned about laser efficiency above all else, it would always make sense to combine as many jobs on a nest as possible. A laser’s revenue-generating efficiency will naturally be governed by part cut time. Deck change, nozzle changes, sheet zeroing, rapid traverse times, and even sheet cuts represent wasted time. If that’s all we care about, it’s a no-brainer to always top off a sheet, even if that produces parts that aren’t due yet.

The tradeoff is that time is consumed immediately on jobs that aren’t a priority, and parts flow downstream and affect other processes. Parts cut weeks early might sit in buffers taking up space, causing confusion, getting lost, or becoming damaged. Alternatively, they could be pushed to completion early, again delaying higher-priority work or causing unnecessary tooling changes.

It Starts With Nesting

For a sheet metal shop, optimized nesting represents perhaps the most crucial element of scheduling. Most processes are fed by blanking, so choosing the right combination of parts implicitly guides the future state of all other processes in the shop. As we’ve seen, it’s possible to optimize one process to the detriment of another, so we need a way to measure the impact of nesting decisions globally, not just at the laser or punch.

What kinds of scheduling methods could we try? For starters, we might say "only nest parts due within the next eight hours, then process parts in the order they arrive downstream." We might run that, and then augment it on the next trial to always nest parts due soon, but top off the sheet if possible. More complexity could be added to avoid nesting parts that would contribute to backlogs, prioritize parts that would feed starving processes, or avoid nesting partial quantities that would require extra changeovers. Maybe a "triage mode" could be implemented to make different decisions if the shop is going to fall behind.

Measuring performance this way makes it easier to characterize complex tradeoffs. What’s the relative cost of performing a sheet cut and storing a remainder versus cutting a bunch of parts early and having them clutter the pipe? What’s the impact of scrapping small remainders instead of storing them and using them to cut small jobs later?

The Potential of Simulation

In my February 2023 article, I discussed the wasteful impact of topping off sheets, concluding that it might not make sense because of wasted capacity. But was I right? What is the real cost of wasted capacity, compared to the benefit of cutting extra parts so that we don’t have to interrupt the queue to recut a scrapped part?

These questions might ordinarily be difficult or impossible to answer, but a good simulation with a well-defined scoring function may provide interesting clarity. Such a simulator is currently in use and undergoing continued development at OSH Cut. In upcoming articles, I’ll describe our scoring functions, statistical models, simulator design, and, finally, our results. Stay tuned!