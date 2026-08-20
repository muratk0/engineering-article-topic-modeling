# AI is better than you think

[TARİH: 01.02.2026 The Fabricator]

Tech Talk

And manufacturers will reap the benefits

THEFABRICATOR.COM

› AUTHOR › CALEB-CHAMBERLAIN

A

bout this time last year, I sat down with an AI agent and created a new app from scratch in about an hour. I didn’t write a single line of code myself. Instead, I talked to a computer. It understood me. And it wrote and deployed an app that we still use to manage credit onboarding at OSH Cut, my fabrication company. It was mind-blowing, sort of like waking up and realizing that we live in a science fiction novel.

Nobody truly knows where AI is headed. People say that it’s overhyped; that the quest for artificial general intelligence, or AGI, is doomed to fail. Perhaps they are right. Perhaps the AI bubble is about to pop, mirroring the famous dot-com crash of 2000. That’s possible, but even if it’s true, frontier AI models are already good enough to change the world. They’ll only get better from here.

HOW USEFUL IS AI, REALLY?

It’s been a year since I wrote and deployed that app, but as impressive as it was, it didn’t transform how we develop code at OSH Cut. We still have five full-time software engineers, and we are hiring more. My custom "vibe-coded" app from a year ago is still useful, but it doesn’t touch our core, foundational business logic. Our most foundational systems are homegrown and human-designed, and to be honest, I haven’t used AI to build another app directly since then.

So, is AI really all that world-changing and powerful? Last year, an MIT study found that inside enterprises, AI initiatives are falling flat. From the report, "Despite $30 to $40 billion in enterprise investment into GenAI, this report uncovers a surprising result in that 95% of organizations are getting zero return." Another organization, called METR (pronounced "meter"), similarly found that in early 2025, experienced developers actually coded more slowly when using AI, not faster.

EVIDENCE YOU CAN’T IGNORE

Much of the supporting evidence for an AI revolution is anecdotal. For example, Jaana Dogan, a principal engineer at Google, recently gained viral attention on X (formerly Twitter) when she posted, "I’m not joking and this isn’t funny. We have been trying to build distributed agent orchestrators at Google since last year. There are various options, not everyone is aligned… I gave Claude Code a description of the problem, it generated what we built last year in an hour." Claude Code is an AI coding agent developed by Anthropic.

Dogan later followed up, "It’s not perfect and I’m iterating on it, but this is where we are right now. If you are skeptical of coding agents, try it on a domain you are already an expert of. Build something complex from scratch where you can be the judge of the artifacts."

Thousands have reported similar experiences, and of course many have reported the opposite. So, what gives? Are AI agents really poised to change the software world, as many senior developers seem to think? Or do early studies prove that it’s all hype?

This is tough to answer because the state of the art is changing so quickly. If you tried using a coding agent a month ago, your perception of AI’s capabilities is already out of date. The biggest, best-capitalized, most powerful companies on the planet are all in on this race, sprinting at a pace that makes even early adopters struggle to stay informed. As fast as things are changing, a study that lags the state of the art by 6 to 12 months isn’t particularly useful. As transformational as the technology promises to be, it seems short-sighted to say, "Over the last six months, it hasn’t had a measurable impact; therefore, it probably won’t."

BUBBLES AND BUSTS

In the 1990s, early internet hype propelled massive speculation that was untethered to reality. Businesses famously raised massive capital rounds having nothing but a website. At the time, well-grounded investors like Warren Buffet cautioned that the market was overpriced. They were right. The bubble burst in 2000, destroying more than $5 trillion in market value in less than two years.

But here’s the thing: The internet still changed the world. It changed how people spend their free time, how businesses operate and interact, how consumers buy, how people communicate. It enabled new business models. It transformed how engineers design products. Today, it continues to transform the manufacturing supply chain. And ironically, the internet enabled today’s AI boom by putting the sum of human knowledge on the web.

It seems in retrospect that the dot-com bubble was predictable. Even so, there was something in the air back then. People might not have known exactly how the internet would change the world, only that it would, and they were 100% correct. I’d argue that this is what drove the dot-com bubble in the first place. When a new technology smacks you in the face and turns your world upside down, you know things are never going to be the same again.

AI is like that. When an AI agent can basically duplicate a year of a team’s work at a company like Google in one hour, you have to admit that something big is happening, even if you can’t quite put your finger on what it’s going to be. Maybe there is a bubble, maybe not. Does it matter?

A NEW ERA FOR SOFTWARE

For my part, I can see how AI will likely affect my manufacturing business in 2026 and beyond. When I used an AI agent to write an app last year, I was floored, but I also was a little concerned. We had invested millions of dollars into our custom, in-house software. It’s our cornered resource, a tool that makes us unique. If AI democratizes access to bespoke in-house software tools like ours, what would it do to my business? Worse, we designed our software stack from the ground up outside of AI. Would our preexisting code and infrastructure put us at a disadvantage as AI-first manufacturing startups sprint ahead?

Today, I’m less concerned. As frontier models have improved, so have the tools to integrate and use them. Our code is increasingly informed and accelerated by AI systems. The results look promising.

For example, we are seeing AI take an increasingly active role in our code reviews and deployments. It can be a little tricky to explain outside the software ecosystem, but I think this is important, so I’ll do my best. When writing software, it’s extremely common to use special software called a repository, or "repo," to keep track of changes and integrate them safely into production code. Perhaps the most common repository is called Git, a program originally developed by Linus Torvalds (the same Linus who wrote the original Linux kernel).

At OSH Cut, we use Git through an online service called GitHub, owned by Microsoft. It just so happens that Microsoft is deeply invested in AI, and it’s integrating its CoPilot AI product into GitHub in astounding ways. Today, when we write new code, we can ask CoPilot to review it at the click of a button. It reviews, leaves comments, and even requests changes. It’s not uncommon for AI to discover bugs in our code that our developers missed during normal review processes. This is huge because it in-tegrates into our existing software systems seamlessly and quickly. CoPilot understands our pre-AI code and helps us deploy changes with fewer errors.

But it can do so much more. We can create tasks (or "issues") on GitHub that describe observed bugs in our code or in new design features. Then we can ask CoPilot to fix them. The AI creates a repository "branch," a safe environment where it can make changes without touching production code. Then it makes code changes, implements features, and finally creates a "pull request" for human and AI review. Paired with continuous integration automation (another feature of GitHub), AI now can accept an issue, make changes to our existing code, write new code, deploy it to a test server, and perform end-to-end tests to make sure it works.

In other words, we can ask an AI to implement a new feature, wait an hour, then visit a fully functioning, safely isolated test site to see how it did. AI doesn’t touch production until the code is reviewed and the functionality is tested, just like working with a human developer.

One of our senior developers recently used this capability to develop a new interactive map for our management software, showing where our orders ship across the U.S. AI was able to get very close on its first try. With some minor review and iteration, we gained an amazing visualization of the regional distribution of our shipped orders. It condensed a multiday project into just a couple hours.

What’s truly remarkable about this is that it bolts on seamlessly to our existing software and infrastructure. In 2025, I was amazed that I could talk to an AI agent and build an app, but it was limited to a tightly controlled environment without a pre-existing code base. Less than a year later, that same agentic power is accessible in the context of existing code!

WINDS OF CHANGE

Experienced software developers will understand how massive this promises to be. Software projects are endless. New users create feature requests, new features create bugs, scope grows without bound. Every week, we triage new incoming issues, deciding what will go into development and what will go into the backlog. The backlog is where feature requests go to die, and it never shrinks; it only grows. But what if an AI agent could take issues from the backlog and work on them, only asking for input when its changes are finished and tested?

I don’t expect AI to take over high-level systems design and feature planning anytime soon—certainly not in 2026. But in just one year, I’ve seen AI become useful inside our multimillion-line code base. That’s not something I expected to see.

In general, I think we can see the direction the wind is blowing. We might not know where this is going to take us.

We don’t know what kinds of ups and downs we’ll see along the way. But it’s safe to say that it’ll change everything.

CALEB CHAMBERLAIN

Caleb Chamberlain

is co-founder of OSH Cut,

www.oshcut.com

. He also is featured in FMA’s "Next-Gen Metal Fab Podcast." Look for new episodes at

www.thefabricator.com/podcast/channel/next-gen-metal-fab

or wherever you get your podcasts

.

Trusted by many American companies

Eagle Lasers is a leading manufacturer of high-quality fiber laser cutting systems and automation.

Top standards in efficiency.

Patented eVa cutting head with 2x larger lenses and 10x less glass replacement needs.

Polymer concrete body for the highest stability even at peak dynamic motion.

Eagle-manufactured linear motors on all axes for wear-free stability and precision.

Built-in conveyor belt transporter for higher quality cut parts and reduced downtime.

Accuracy, repeatability and new generation software for the highest quality cut.

eaglelasersusa.com