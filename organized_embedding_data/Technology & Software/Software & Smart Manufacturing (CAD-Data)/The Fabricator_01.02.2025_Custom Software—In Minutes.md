# Custom Software—In Minutes

[TARİH: 01.02.2025 The Fabricator]

Tech Talk

How AI is about to change the world

CALEB CHAMBERLAIN

I

just used an AI agent to write a custom app for my shop. It took less than two hours. I know, I know. AI is so hyped right now that it’s hard to hear the word and not cringe a little. But on a whim, I started tinkering with Replit, an AI agent coding service, and my world turned upside down. For the record, I don’t have any relationship at all with the company or its service, beyond having used it once to write an app.

Coding Has Changed Forever

I’ve been writing code for three decades. I started on an old IBM compatible 286 computer running DOS, and I’ve been doing it ever since. A lot has changed as hardware, new languages, and new computing paradigms have been introduced over the years. The internet, and then later the cloud, completely changed how modern software is written, deployed, purchased, and used, and all for the better.

But nothing in my entire coding career prepared me for the experience I had, conversationally chatting with an AI agent while it built a custom app for me. It blew my mind. I literally didn’t write a single line of code. I talked to a computer—just like I’d talk to a software developer—and it wrote the app. I clicked a few buttons and deployed it, and now I have a custom app that I use at my fab shop (OSH Cut) to help manage workflows.

To be clear, this isn’t a "no code" application. It wasn’t created with drag and drop block diagram features. It is literally a full stack web application built from the ground up, deployable with or without the Replit service, anywhere. I didn’t write the code, but I knew what I wanted, and I asked for it: a web app with a React front end, leveraging typescript; a NodeJS/Express back end implementing a REST application programming interface; and a MySQL database. For the noncoders in the room, those are the particular languages and architectures I wanted to use, since I’m familiar with them.

"Wait, Seriously?"

The process wasn’t perfect, but it was jaw-dropping anyway. When I first started tinkering, it was actually through an app on my phone. I typed in what I wanted, mostly believing it wouldn’t work, and it started churning away, building all the database tables and client and server code. A few minutes later it ran the first-pass app, right there on my phone. And it worked! Right there on my screen was the login page I asked for, nicely formatted, rendering well on my phone. I had a sort of, "Wait, seriously?" moment and jumped onto my desktop computer to dig deeper.

What followed was a two-hour dialog with a computer, during which it’d deploy the app, I’d ask for changes or describe bugs or awkward user interactions, and it’d fix them. We iterated until I had exactly the app I wanted, with a few simplifications here and there. Perhaps the best part is, the AI agent is right there on tap if I ever want to change or add features.

Not Perfect but Still Extraordinary

Occasionally, there were mild frustrations as the AI agent made changes and accidentally removed features I had asked for earlier. When that happened, I could navigate back to a previous "snapshot" and restore the old state and try again. And the agent had a lot of trouble implementing a nuanced multiuser permissions system.

While I might have gotten that working through our back-and-forth dialog eventually, I ultimately opted to have those more complex features removed. That process was almost as incredible as the rest of the experience. I said something like, "On second thought, let’s forget about sharing and user permissions. Please remove all client UI, APIs, and database tables that implement those features." It did. And it worked.

Naturally, I also could have just dug into the code and written the more complex stuff myself. In fact, the code was remarkably well structured, readable, and understandable. I expected a dreaded "spaghetti code" application, difficult to understand and impossible to maintain. But that wasn’t the case at all. Even so, at that point, it was almost a challenge to figure out if I could get it working without editing the code on my own.

Scaffolding and infrastructure for AI

Let’s face it, artificial intelligence really isn’t an apt name. In truth, it’s more like an "artificial assistant"—at least the technology’s current state seems to imply that. The more you train the assistant, the more it can do, and that amount seems to be expanding at light speed.

That said, humans need to know enough to train. Stories about AI really show how those artificial assistants can go on hyperdrive—if, that is, they have the right trainers and a good place to start. Caleb Chamberlain referred to the "scaffolding and infrastructure." AI can’t build something from nothing, at least not yet.

Impactful AI applications won’t replace human intelligence; they’ll augment it. AI can’t know a business better than the people who work there, especially those on the front lines. In fact, you could argue that AI will make skilled people better and the untrained and disengaged even less valuable than they already were—and perhaps even a bit dangerous. Chamberlain wouldn’t have gotten so much out of AI if he didn’t know a thing or two about software.

Similarly, AI won’t magically lead shops to operational excellence if managers and employees don’t have the basics down, both from a technological (do you really know how this laser works?) and a planning standpoint (do you really know how long this job takes?).

For the past few years, I’ve seen the metal fabrication business undergo a transformational shift. When companies experience a transformation in the market, you have winners and losers. At least at this point, I believe those who embrace the power of data and software—including the AI tools that make software so powerful—will be the winners.

For the record, I wrote this piece without AI assistance. Just for giggles, I typed "Write an article about AI in metal fabrication in the style of Tim Heston" in ChatGPT. I got this banger of a conclusion: "AI in precision sheet metal fabrication isn’t some far-off dream—it’s already happening, and its impact will be massive."

Dang, ChatGPT. Yeah, that sounds like me. Still, the whole article had no meat on the bone, no reporting, no scaffolding or infrastructure, and numerous (albeit correctable) inaccuracies. AI still can’t interview humans in an in-depth way, thank goodness. When that day comes, though, I can only hope I have the scaffolding and infrastructure to make the most out of it.

—Tim Heston, Senior Editor

nespix / iStock / Getty Images Plus

People seem to wonder what AI is good for, but the killer app is already here. AI is going to accelerate the pace of software development and improve accessibility by orders of magnitude—this year.

Even without writing code, though, knowing how to do it—and understanding what can go wrong—helped immensely. For example, at one point, a drag-drop feature wasn’t working correctly. I’d drag a card to a new column, and it would just go back to where it started without updating. A normal reaction might have been to tell the AI agent, "The dragdrop feature doesn’t work," and in fact I tried that just to see if it could fix it. Replit was unable to fix the issue with such vague instructions.

That’s not unlike working with a software developer. Saying "this feature doesn’t work" is nearly as helpful as saying "the internet is broken" (not very). In this case, I refreshed the page and found that the card did actually get moved in the database, but that the user interface didn’t show the state change without reloading the page. Aha. A simple state-management issue, then.

So, I told Replit that the client UI probably wasn’t getting the new state, and voila, it found the problem and fixed it. That workflow, and many others like it, might make using an agentic AI frustrating in its current state.

There are lots of AI agent services out there, and Replit is the only one I’ve tried. It may not be the best—I don’t know. But the company has set up the AI with a bunch of code so that it can write, deploy, test, check results, and iterate, all on its own. It rarely got code perfectly on the first try. But because it could see the results and try again, it tended to work surprisingly well. Staggeringly well. I use my new, custom-designed app daily.

"Computer, Engage"

I don’t know if I can emphasize enough how incredible this is. You can have a conversation with a computer and have it write, debug, iterate, and deploy a full-stack web application, deployable anywhere, in minutes! Engaging a third-party development firm to make the same product might have cost $20,000 a month of development. It’s pure insanity.

Those who follow my column will know that we at OSH Cut write our own software and effectively automate the ordering process. We’ve written code to automate bidding, scheduling, purchasing, and even program our lasers and press brakes. We own the "full stack," as it were. That has allowed us to carve out a unique niche in the industry. We have a lot of fun, but we spend a lot of money on software. In the last six years, we’ve invested over $2 million in ongoing development, and we have a lot more to do.

This experience with AI bent my mind. If AI, paired with great scaffolding and infrastructure, can accelerate development like this, what could my highly skilled software team accomplish in the next few years? I’m keen to figure it out, because AI is rocket fuel for software development. People seem to wonder what it’s good for, but the killer app is already here. AI is going to accelerate the pace of software development and improve accessibility by orders of magnitude—this year.

Just last year, I wrote that perhaps someday AI would enable everyone to be a programmer. Your machine operators could talk to the computer and write custom apps to improve their workflow. It’d become normal for shops to write their own software, perfectly fit to their specific needs.

When I wrote it, I believed it—but I didn’t believe it, if you know what I mean. Not in a bone-deep, "this is going to change everything" kind of way. Well, that has changed. If AI is already this capable, then the next decade is going to be a wild ride indeed.

Caleb Chamberlain

is co-founder of OSH Cut,

www.oshcut.com

. He is also featured in FMA’s Next-Gen Metal Fab Podcast. Look for new episodes at

www.thefabricator.com/podcast/channel/next-gen-metal-fab

or wherever you get your podcasts.

Electric Press Brakes Electric Hardware Insertion Machines Electric Tapping/Countersinking Machines Press Brake Retrofits

Your Trusted Partner in Press Brake Retrofits Has Been Crowing…

Automec, Inc. - Waltham. MA

781-893-3403 |

sales@automec.com

|

www.automec.com