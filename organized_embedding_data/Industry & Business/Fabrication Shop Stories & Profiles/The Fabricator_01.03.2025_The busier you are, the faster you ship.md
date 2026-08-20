# The busier you are, the faster you ship

[TARİH: 01.03.2025 The Fabricator]

Tech Talk

Why operating at scale lets fabricators ship faster

CALEB CHAMBERLAIN

As daily average demand grows, excess capacity required for rapid fulfillment drops.

S

everal years ago, I needed a custom sheet metal part, so I shared my models and prints with local fabricators. I had limited success. While most shops were responsive, everyone was busy. Lead times were measured in weeks, even though my job was relatively small. One shop confided, "We used to offer rapid turnaround for prototypes, but we just got too busy with production, and we can’t do that anymore."

I think that’s a common story. When manufacturers are busy, lead times grow. This outcome feels natural. If you go to the grocery store just before Thanksgiving, you’ll line up at the checkout. If you go to an airport in the middle of the day, you’ll wait in security. And if your local fabricator is booked, you’ll have to wait.

Get in Line

Queues are a fact of life, and it’s really a shame. It means as demand grows, customers have a worse experience. Nobody likes waiting in line. Yet a healthy backlog is in some ways desirable for manufacturers. It’s nice to know that you’ll keep your people busy for the next several weeks. It’s great for the shop, but less so for the customer.

This uneasy tension between manufacturers and customers creates a sort of balance. Shops might be reluctant to expand capacity, since it’s expensive. But customers may opt to go elsewhere if the wait is too long, and of course shops will want to grow when they can. There’s a sort of steady-state dynamic that, at least from the customer’s perspective, keeps lead times mediocre but not insane.

All other things being equal, people of course prefer immediacy. Some fabricators (including my company, OSH Cut) enable rapid service by charging more for it. The "pay for speed" strategy isn’t just a gimmick. It’s an important tool for controlling the cost of excess capacity. If you have weeks to turn orders around, you can level production backward so that you only need enough capacity to handle average demand. But if you want to turn orders around quickly, you need enough excess capacity to deal with peak demand at all times.

That gets expensive. So instead of trying to fulfill everything fast, you maintain some excess capacity and limit access by charging more for speed.

The Power of Scale

That works fine, but here’s the exciting caveat: the bigger you get, the less excess capacity you need, and therefore the less you have to charge for speed. That’s true for large and small jobs alike. The enabling factor is a magical property of the statistics of random arrivals.

Random arrivals are often best modeled with what’s called a Poisson distribution. Think of car arrivals at a stoplight, for example. If at a given time of day cars arrive independently and at a steady average rate, the Poisson distribution helps us predict the likelihood that we’ll see zero, one, two, or more cars over a certain time period.

For our purposes, a key property of the Poisson distribution is how its standard deviation—the "volatility" of arrivals, so to speak—changes as the average grows. The standard deviation of a Poisson distribution is always equal to the square root of the mean. In other words, the larger the average grows, the less volatility there is as a percentage of the average.

This is magical for an on-demand manufacturer, because as demand increases (more orders per day on average), less excess capacity is required to fulfill peak demand quickly. It works out that a Poisson distribution isn’t a perfect match, because not only do we care about random arrivals, but we also care about order size. So, when modeling demand, we get a normal-ish distribution stacked on a Poisson-ish distribution. At OSH Cut, the standard deviation on our daily demand grows at 14 times the square root of the mean.

With that data, we can clearly predict how much extra capacity we’d need to turn 90% of orders around within 24 hours. In this context, "extra capacity" means everything we need, from equipment to shop space to people. As the figure shows, the extra capacity required as we scale up eventually drops to zero, or close to it. In some ways, this result is counterintuitive. It means that the busier an on-demand shop gets, the better it can be at turning orders around quickly at low to zero extra cost, all other things being equal.

This isn’t just academic. At OSH Cut, we’ve already benefitted from these scale economies. Our default lead time for laser cutting jobs up to three hours long is now just two business days at no extra cost. We also can turn orders around same day at a higher price, but we just dropped that price by about 70% for most orders. And we are doing this while simultaneously shipping more than ever before, with better than 98% on-time delivery.

There are naturally some important caveats. For starters, operations must support high-mix orders at scale. If production systems aren’t up to the task, then scale will beget confusion, quality issues, and late shipments, instead of statistical efficiency. Our solution to this problem is a combination of custom software and great people. We automate quoting, scheduling, purchasing, receivables, and machine programming. Operations are further simplified with in-house production tools that help our operators know what to do, how, and when.

Before my brother and I started OSH Cut, we were just entrepreneurs looking for parts at a reasonable price and a quick lead time. I wish I could say that we started out with a deep understanding of the economics of speed. We’d have sprinted a little harder to get where we are today. But I’m pleased that we managed to design and stumble our way into a solution.

Black Swans

Big events, like new aggressive tariffs and complex geopolitics, can shift demand in major ways. In an ideal world, a shop always has just the right capacity. Too much capacity means gross margins suffer, and too little means you won’t keep up. When economic upheaval suddenly shifts average demand, like COVID did, then a dialed-in shop might suddenly find itself under or over capacity. When capacity is a function of skilled labor and high capex, these challenges can be difficult indeed.

But frankly, unpredictable economic conditions have always plagued manufacturers. That’s not new. The exciting thing is that the conflict between lead time, capacity, and cost is actually solvable. Any company that aggregates enough scale and designs its systems correctly should enable extremely fast turnarounds at fantastic prices.

This isn’t really the norm today, but mathematics and experience together prove that it’s possible. If manufacturers lean into this reality, it’ll help transform manufacturing in the United States and, ultimately, make us more competitive globally.

Caleb Chamberlain

is co-founder of OSH Cut,

www.oshcut.com

. He is also featured in FMA’s Next-Gen Metal Fab Podcast. Look for new episodes at

www.thefabricator.com/podcast/channel/next-gen-metal-fab

or wherever you get your podcasts.

Tube Bending & Finishing Solutions

Knowledge & Experience Working for You

Profile & Angle Roll Benders

Multiple machine and control configurations

Attachments available for bending angle iron, serpentine shapes, spirals/coils

Up to 8″ Sch. 40 Capacity

CNC Tube Benders

½″ to 10″ Capacity

All-Electric & Hybrid

Draw + Push Roll Bending

Automation Ready

Metal Finishing Machines

Suitable for Straight and Bent workpieces

Auto Loading & Unloading Systems

Deburring, End Finishing, and Tube Notching

J&S Machine, Inc.

Ph: 715-273-3376

E-mail:

sales@ismachine.com

www.jsmachine.com

Machine Sales & Service Since 1998

Trust the leaders in Dust and Fume Extraction

Superior performance. Proper engineering. Sensible pricing.

Get your dust and fume extraction solutions from one of Canada’s most trusted manufacturers with over 30 years of experience.

Industrial Vacuums

Dust Collectors

Wet Collectors

Down draft Tables

Fume Arms

Vac Ready Welding/Tools

Contact us for a quote

1-800-365-DUST (3878)

info@eurovac.com

www.eurovac.com

More efficiency

Innovation and reliability for your success: KASTO

win

More economical:

Ideal cost to performance ratio

More reliability:

Built robust, with high precision as the benchmark

More innovation:

Intelligent control and user friendly operation

More space

Smarter storage for maximum space efficiency: KASTO

ecosfore

More efficiency:

Save time with direct access—no additional lifting equipment needed

More flexibility:

Modular, height-adjustable supports for up to 3 loading heights

More safety:

A robust safety system prevents malfunctions and costly downtime

www.kasto.com