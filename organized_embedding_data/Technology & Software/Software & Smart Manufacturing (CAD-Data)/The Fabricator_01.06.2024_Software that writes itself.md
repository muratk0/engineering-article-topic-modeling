# Software that writes itself

[TARİH: 01.06.2024 The Fabricator]

Tech Talk

How a fabricator uses AI to accelerate software development

Caleb Chamberlain

Userba011d64_201/ iStock / Getty Images Plus

I’m proud that our software team has such great proximity to the floor, but imagine if operators could just have a conversation with the computer and spin out a new software tweak on the spot?

F

ive years ago, OSH Cut was basically a two-person company. We had a 3-kW flatbed laser, and our office was a card table in a corner of the warehouse. I finished most of our initial quoting, inventory, and order management software there. I’d write code, take a break to fulfill an order, then get back to it. My brother Jacom was still in school and working part time elsewhere, so he’d take breaks and come help me load the laser or ship parts.

Those days were interesting and exciting. I like to say I’m an engineer first, businessman second. Writing software was my jam. But it was also stressful. I was pulling cash out of my home loan to fund the business month to month, we didn’t really know how to market our online sheet metal service, and we were learning how the industry worked as we went.

We’ve changed since then. With 50 employees, a new 53,000-sq.-ft. shop, and a wider variety of services (including laser tube cutting as of this year), I’ve spent less and less time writing software.

That’s fine. Our software team is filled with the most intelligent, innovative people I’ve met. I used to think I was smart, but I feel like I’m playing catch-up whenever I’m in a room with these guys. They are better than fine without me getting in and breaking tests and deployment workflows.

Even so, we have some major software projects in the works that’ll transform how we do business. Our future growth is bottlenecked behind a handful of tools that are in the home stretches, so a couple weeks ago I rearranged my schedule so that I could spend two or three days a week moving the ball down the field. It’s been a blast.

AI Gives a Big Assist

After being only peripherally involved for so long, I was amazed at how much our technology has changed since I was pounding away five years ago, writing code for our MVP (that’s software-speak for minimum viable product). Within a couple days, I jumped on Slack and gushed to our chief technology officer. "It’s like our software writes itself!"

There’s some hyperbole in there, but not as much as you might think. We now use a combination of technologies that makes it easier than ever to write new software. In isolation, none of these technologies would make that big of a difference. Put together, they increase our software development pace tenfold. It’s a lot like automation on the fabrication floor, except the machines are software tools and design patterns, and the product is the software instead of a piece of metal.

It’d take a lot of explanation to paint the full picture, and it gets pretty technical. For those interested, our team moved the vast majority of our codebase from Javascript to Typescript; they integrated continuous test and deployment automation for new code; they built an internal library of components for easy reuse; they designed and integrated a powerful data model for our web apps to make it easy to grab data from our servers and to receive asynchronous updates; they built models on the back end to make it easy to add APIs (application programming interfaces) and new database tables; and finally, we plugged into Github’s Copilot LLM, which aids the team as we write new code.

With all these innovations and tools, it takes far less effort now to write new software. For example, our team recently built a new task management system and had it running in production within a single week. I said that it was heroic, and it was. But it also wouldn’t have been possible if the team hadn’t put all the building blocks in place over the preceding years.

Coding, Then and Now

Now that I’m in the weeds again, I can’t help but notice how different it is, especially using AI to help write code quickly. I can type a comment in code—something like, "Retrieve all open work orders that contain this part from the database." I press enter, wait half a second, and Copilot fills in all the code needed to do exactly that, using our existing code as a model. It doesn’t always get it right. I’d say it’s perfect maybe 40% of the time. So instead of trying to remember which database function to call, I just describe what I need to do, watch the computer do it, then fix the glitches if there are any.

This is where Typescript comes in handy. For the uninitiated, Typescript is basically an extension of Javascript. Javascript is the language developers use to run code in web browsers. Any modern web app and even most web pages are powered by Javascript. The language has come a long way since I first dabbled in web development in the early 1990s, but even so, it’s a loose, forgiving, unopinionated kind of language. It’s really easy to write really bad code in Javascript. So, Microsoft came along in 2012 and released Typescript, which adds tighter rules to make sure developers don’t make certain kinds of mistakes. It "transpiles" down to Javascript that browsers know how to run, but developers get some guide rails to make code easier to write. When Copilot writes a section of code, the development environment uses Typescript and Intellisense to immediately highlight problems. You can then tell Copilot what the problem is and ask for a fix, or just fix it yourself.

In a way, developing in this new environment is like supervising the computer while it does the work. You do the high-level thinking and architectural design, then work hand in hand with AI to implement it. There’s something jaw-dropping about watching the computer reach into our in-house component library and say, more or less, "I see what you are trying to do; check out this really handy component one of your developers built." It’s bonkers, like we’re living in a sci-fi novel.

Everyone Will Be a Programmer

Jensen Huang, the CEO of the AI chip company NVidia, recently said, "It is our job to create computing technology such that nobody has to program and that the programming language is human. Everybody in the world is now a programmer."

Having just witnessed my own coding workflow transform overnight, I think he might be right. Oh, we aren’t there yet. Copilot makes a lot of dumb mistakes, and in some respects it’s basically a really fancy autocomplete tool. And there are enough moving pieces in our tech stack that it does take real skill to make anything and deploy it into production. There’s a steep learning curve, but remember, AI is in its infancy. Imagine an AI coder that’s twice as good. Or 100 times as good. At what point will we stop needing to be writing code at all? "Everybody in the world is now a programmer." Imagine how that might be.

At OSH Cut, we write perfect-fit tools to support our own manufacturing operation and our customers. In an industry that isn’t really on the leading edge of software tech, that does make us unique. But I think that eventually, and maybe soon, every shop may be able to do the same thing without having to sink millions of dollars into development. It’s extremely common at OSH Cut for our shop workers to walk into the office and talk to the software team about glitches or ideas for software improvements. Our software team often does the reverse, working on the floor to understand how our software is used in practice.

I’m proud that our software team has such great proximity to the floor, but imagine if operators could just have a conversation with the computer and spin out a new software tweak on the spot?

Hey computer, in this work order view, can you add the order due date to the right sidebar, and highlight it red if the order is late or at risk of being late?

That kind of capability might add a whole new level of meaning to the phrase "skilled operator." Meanwhile, our developers will be free to work on other software challenges to improve our service.

It remains to be seen whether AI will live up to this promise. Some think that making models bigger will solve most of its current limitations; others think scale will just make AI better at making mistakes that seem all the more believable. Nobody really knows. Whatever happens next, technologies like AI have already transformed the way we write software at OSH Cut. I’m optimistic that it’ll only get better.

Caleb Chamberlain

is CEO at OSH Cut,

www.oshcut.com

.

Look out for The Fabricator Podcast featuring Chamberlain in conversation with

Dan Davis

and

Tim Heston

, available at

thefabricator.com/podcast

.

"THE MITSUBISHI LASER IS OUR WORKHORSE AT OLYMPIC STEEL"

Si Cha

Olympic Steel

Plant Manager Fabrication Division Buford, Georgia

Scan to learn more

With the latest in artificial intelligence (AI) and gas reduction technology, the new GX-F ADVANCED Series of two-dimensional fiber lasers delivers more power while using less nitrogen.

Artificial intelligence is a branch of computer science that automates intelligent behavior and machine learning. This means the machine itself can learn from data and adjust performance without human intervention.

For more info, visit

mcmachinery.com