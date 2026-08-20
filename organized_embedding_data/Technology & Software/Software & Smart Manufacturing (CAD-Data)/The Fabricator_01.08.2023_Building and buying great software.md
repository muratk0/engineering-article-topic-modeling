# Building and buying great software

[TARİH: 01.08.2023 The Fabricator]

Tech Talk

How

Healthcare.gov

’s failed rollout informs software development and purchasing

By

Caleb Chamberlain

For more content from Caleb Chamberlain, visit

www.thefabricator.com/author/caleb-chamberlain

.

S

oftware is becoming ever more relevant and critical for the modern fab shop. Whether you are developing code in-house or shopping for a third-party tool, it’s important to understand what you are looking for. That can be difficult without having a deep understanding of how software is made.

Healthcare.gov

represents an easily accessible case study on the risks of software design. It launched 10 years ago and immediately landed with a thud. It was so slow and glitchy that as few as 1% of interested people were able to enroll in the first week. The web design failed to deliver on the absolute basics, with poor workflows and glitchy user interfaces. To top it off, health insurance providers were provided inaccurate information by the site, making it difficult or even impossible to correctly handle enrollments.

Stress tests that should have explored expected user volume were wholly inadequate. A day before launch, it was found that the site became too slow with only 1,100 concurrent users. The expected user count was 50,000 to 60,000. If that wasn’t bad enough, the actual simultaneous user count soared to 250,000 within the first week, over 200 times the number of users that pre-release stress tests indicated the site could handle. In retrospect, one wonders why the stress tests were performed at all. Their clear failure did nothing to change the release timeline.

The project didn’t stumble for lack of budget. It was originally estimated to cost $93.7 million, a staggering sum even if the project didn’t go over budget. But the estimates were wildly incorrect. Before completion, the total cost rose to a jaw-dropping, tear-inducing $1.7 billion, almost 20 times higher than estimated.

Healthcare.gov

works great in 2023, but at launch it was perhaps the most spectacular, expensive, and public software fiasco in history. While much of the complexity surrounding

Healthcare.gov

’s rollout was unavoidable, we can use its botched rollout to explore what makes software projects succeed or fail. Its failures might provide insight into how you might build your own in-house software team. It might also provide insight into what to look for when buying third-party software.

Proximity: Go to Gemba

In a previous article, I wrote about how Southwest Airlines fell apart during the holidays in 2022. In a nutshell, the company relied on decades-old software that made it extremely difficult to handle scheduling interruptions. Workers understood the problem, but company executives—insulated from the daily operational pain—failed for decades to invest in new infrastructure. That failure combined with a winter storm and high seasonal demand caused the entire company to grind to a halt, stranding tens of thousands of people the week of Christmas. Southwest itself estimates that the disaster ultimately will cost the company almost $1 billion. That extraordinary expense might have been avoided if the decision-makers were close enough to the operational problems to understand the urgency.

The lesson there is that good software is developed by teams with proximity. Good proximity implies two things: first, that the software team is intimately familiar with the pain that it is trying to solve; second, developers have proximity to the results produced by their software. Put another way, a team with good proximity understands the pain, and then uses its own software tool to alleviate it. If the software misses the target, or is glitchy or difficult to use, the developers should be the first ones to find out.

This is one area where the

Healthcare.gov

project certainly failed. Developers might have understood the problems their website was designed to solve, but the parent contractor operated out of Canada, not the United States, the country

Healthcare.gov

serves. Different components of the full system were also farmed out to many subcontractors, none of whom would have owned the full application. Even if developers understood the pain the software was intended to solve, the end-to-end user experience would have been firmly outside any individual software developer’s control.

One contractor, for example, handled authentication systems exclusively. If registration and authentication were slow or broken (and they were), whose fault was it? The user-experience designers? The database? The engineers handling the server infrastructure? The web application developers? Or all of them together? Every single subgroup might have been inside a different company. Figuring out the core issue, communicating it, and getting a fix into production would have been difficult even if the problem was well understood.

None of this should be surprising for a fabricator. Proximity is just another way to say, go to the

gemba

. In some ways, software development isn’t all that different from continuous improvement in manufacturing.

Rapid Iteration: Plan, Do, Check, Act

Imagine that you’ve been tasked with building a new manufacturing line from scratch, using new equipment, in an industry vertical that your company has never served before. You have a huge budget, so you should be able to make it work. But there is one major caveat: You only get one try to make everything perfect. From the start, you must select the equipment, the factory layout, and the number of people; what their training looks like and how they’ll be trained; and how much work-in-process and finished goods to keep on hand. After you finish planning, you’re locked in. You can’t change the design.

What a project that would be. Not only is it impossible to predict in advance the problems and inefficiencies in a new industry, but the entire design process— all in advance, without changes—flies in the face of the plan, do, check, act (PDCA) cycle that manufacturers have learned to apply continually. It wouldn’t make sense to approach manufacturing that way.

It also doesn’t make sense for software, yet that’s precisely how

Healthcare.gov

was developed. The entire system was designed in advance, by committee, in a process that took months. Then meticulously crafted Gantt charts were created, showing how long each element would take to develop, culminating ultimately in final testing and release. But as any manufacturer might guess, schedules are impossible to predict and even more impossible to follow.

In manufacturing, the continuous improvement process is often guided by the PDCA cycle. We

plan

a production change, which is designed as an experiment; then we

do

, implementing the change to conduct the experiment. But we don’t stop there. Once a change is made, we

check

the outcome to ensure that it had the desired effect. Finally, we act on that information, adjusting plans based on what was learned.

This process is iterative, meant to be applied continuously and consistently. This couldn’t be more different than a waterfall software development process, where the entire project is designed upfront in a specifications document hundreds of pages long. Instead, PDCA would call for relatively small software changes, made quickly, and then deployed and fully tested before moving on to the next step.

Healthcare.gov

wasn’t tested end to end until days before release, at which point changes were impossible to make before launch.

Limited Scope, Clear Vision

Two of the most impactful software creations in the world, Git and Linux, were originally created by one brilliant developer: Linus Torvalds. Git is a versioncontrol system that is used heavily by virtually every software team, and Linux is a computer operating system. Chances are great that most of the software you use was developed with the help of Git. And if you own any modern CNC equipment, it is likely powered by Linux under the hood.

After Torvalds got the ball rolling, many others contributed (and continue to contribute) to both these tools. Even so, it’s compelling to me that one brilliant visionary can have such a large impact. Torvalds understood the need, envisioned the solution, and made it happen.

It’s natural that the more stakeholders there are, and the higher the software complexity, the more difficult it is to design a system that perfectly solves a problem. Again, consider

Healthcare.gov

. By any measure, the project was impossibly complicated. It’s been estimated that at least 47 different private contractors worked on it. The fact that 47 is an estimate is telling—nobody even knows how many companies helped write the system! Companies that did work on it have been accused of gross incompetence and corruption. And the overall effort was coordinated by a government department with no experience in software development, to say nothing of a project this size.

Contrast that with Torvalds’ development of Linux and Git. They couldn’t be more different. On one end of the spectrum, we have one brilliant guy with a vision, solving a clear problem, at functionally zero cost. On the other end, we have software designed by committee, involving thousands of stakeholders, with apparently unlimited budget, implemented by at least 47 companies collectively employing hundreds of people, and all managed by a government organization with no software development experience.

In fairness, writing the bones of Linux was a very different kind of project. Linux isn’t simple, but it’s complicated in a more quantifiable way than the cat-herding project

Healthcare.gov

must have been. I don’t envy the managers and engineers that had to make it work.

Where to Go From Here

The lesson is that a project is more likely to succeed brilliantly if it can be implemented by a small team of smart and focused people who understand the problem intimately, have a clear vision of the solution, and can iterate quickly. If your company is developing software in-house, this lesson can and should be applied to your own development teams. But internal software development is a major commitment, and one that might not always make sense.

For those purchasing software, it might not be as immediately obvious how the software was developed. But there are signs. Software vendors that specifically serve your industry vertical (that is, metal manufacturers) are probably more likely to have a solution that fits your needs, because they can limit scope and maintain good proximity. All other things being equal, software probably isn’t going to be as good a fit if it was designed to serve tens of thousands of companies across every industry.

You might also explore how often software updates are released, and how developers receive and act on user feedback. The way a software team connects with customers can have a huge impact on the software’s value to your business.

Whether you build or buy, software is an indispensable part of the modern fab shop. It enables incredible efficiency and improved quality of life. But the past is riddled with incomprehensibly expensive software disasters like

Healthcare.gov

. Navigating that reality can be tricky, but you’ll start a step ahead if you favor software designed for manufacturers, by manufacturers, with relatively small teams who make changes quickly and test them personally.

Caleb Chamberlain

is CEO and co-founder of Orem, Utah-based OSH Cut,

www.oshcut.com

.

MADE IN THE USA

WILA Tooling

Trusted quality since 1932. As from 2024, our world class quality products are proudly manufactured in our new Louisville, kentucky facility.

With the compliments of the Press Brake Productivity people.

GROW YOUR BUSINESS WITH WILA